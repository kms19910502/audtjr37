#define F_CPU 16000000UL	//	16MHz
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <string.h>
#include "dht11/dht11.h"
#include "uart/uart.h"




/*	문자 하나를 전송하는 함수	*/
void PutChar0(char c);

/*	문자열을 전송하는 함수	*/
void Puts0(char* str);

/*	문자열을 수신하는 함수	*/
char Gets0(void);

void Init_UART0(void)
{
	//	UCSR0B는 Tx, Rx를 설정한다. Tx(08), Rx(10)으로 설정
	UCSR0B = 0x18;		//	Tx와 Rx를 설정한다. 송/수신 가능하도록 설정
	UCSR0C = 0x06;		//	8bit data, no parity(0), 1 stop bit(0) 설정
	
	//	바운드 레이트 설정. 9600baud rate로 설정. 115200baud rate는 8로 설정
	UBRR0H = 0;
	UBRR0L = 103;
}



/*	ADC값을 읽어서 리턴하는 함수	*/
unsigned short ReadADC1(void);
unsigned short ReadADC2(void);

int main(void)
{
	char p[12];
	/*
	ADMUX |= 0x40;						//	AVCC를 기준전압으로 설정
	ADCSRA |= 0x07;						//	분주비를 128로 설정
	ADCSRA |= ( 1 << ADEN );			//	ADC 활성화
	ADCSRA |= ( 1 << ADATE );			//	자동 트리거 모드
	ADMUX |= ( ( ADMUX & 0xE0 ) | 0 );	//	채널 선택
	ADCSRA |= ( 1 << ADSC );			//	변환시작
	*/
	
	//	위의 설정을 한 번에 처리한 문장이 아래의 두 문장
	
	ADCSRA = 0x87;	//	0x87 = 0b1000 0111
	
	uint8_t data = 0;
	char buf[40] = {0,};
	USART_Init();
	Init_UART0();
	DDRB = 0xFF;
	PORTB = 0x00;
	DDRD = 0x08; //PD3 환풍기
	PORTD = 0x00;
	DDRD = 0x10; //PD4 LED
	PORTD = 0x00;
	int temperature;
	int humidity;
	
	while (1)
	{
		
	dht11_getdata(0, &data);
	temperature=data;
	sprintf(buf, "temperature:%d", temperature); //temperature:
	strTransmit(buf);
	memset(buf, 0x00, 40);
	_delay_ms(1000);
	
	
	dht11_getdata(1, &data);
	humidity=data;
	sprintf(buf, "humidity: %d", humidity); ////humidity:
	strTransmit(buf);
	memset(buf, 0x00, 40);
	_delay_ms( 1000 );
	
		
	 
	
		
		
		
		
	sprintf( p, "light : %d", ReadADC1() ); // ADC1의 값을 문자열로 변경. 채널3   //light : 
	Puts0( p );
	_delay_ms( 2000 );
	
	sprintf( p, "soil : %d", ReadADC2() ); // ADC2의 값을 문자열로 변경. 채널2  //soil : 
	Puts0( p );
	_delay_ms( 2000 );
	
	
	
	if(ReadADC2()<100){PORTB = 0b00101011;}    //수중펌프 동작관련
	else if(ReadADC2()>=600){PORTB = 0x00;}
	
		
	if(humidity>40){PORTD = PORTD | (1<<PORTD3);}   //환기팬 관련
	else{PORTD &= ~(1<<PORTD3);}
		
		
	if(ReadADC1()<100){PORTD = PORTD | (1<<PORTD4);} //LED 관련
	else{PORTD &= ~(1<<PORTD4);}
	
	}
	
	
}



/*  ADC channel 3값을 읽어서 리턴하는 함수 */
unsigned short ReadADC1(void)
{
	ADMUX = 0x43; // ADC3를 사용할 것이다.
	ADCSRA |= (1 << ADSC); // 변환시작
	while (ADCSRA & (1 << ADSC));
	return ADC;
}

/*  ADC channel 2값을 읽어서 리턴하는 함수 */
unsigned short ReadADC2(void)
{
	ADMUX = 0x42; // ADC2를 사용할 것이다.
	ADCSRA |= (1 << ADSC); // 변환시작
	while (ADCSRA & (1 << ADSC));
	return ADC;
}

/*	문자 하나를 전송하는 함수	*/
void PutChar0(char c)
{
	//	5번째 비트가 켜져있지 않으면 while문이 무한 반복하는데
	//	5번째 비트가 켜지는 순간에 while 루프를 빠져나와서 데이터를 전송하는 원리
	
	//	데이터가 들어오지 않았다면 while문 반복
	while ( !( UCSR0A & 0x20 ) );	//	5번째 bit를 사용
	
	//	데이터를 전송
	UDR0 = c;
}

/*	문자열을 전송하는 함수	*/
void Puts0(char* str)
{
	while(*str)
	{
		while(!(UCSR0A & (1 << UDRE0)));
		UDR0 = *str++;
	}
}

/*	문자열을 수신하는 함수	*/
char Gets0(void)
{
	//	데이터가 들어오지 않았다면 while문 반복
	while ( !( UCSR0A & 0x80 ) );	//	RXC가 Set(8번째 자리)되어 있어야 한다.
	
	//	데이터를 리턴
	return UDR0;
}