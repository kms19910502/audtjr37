#define F_CPU 16000000UL	//	16MHz
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>

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
unsigned short ReadADC(void);

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
	ADMUX = 0x40;	//	ADC0를 사용할 것이다. 즉, 아두이노의 A0핀을 사용한다.
	ADCSRA = 0x87;	//	0x87 = 0b1000 0111
	
	Init_UART0();
	
	while (1)
	{
		sprintf( p, "light : %d\n", ReadADC() );	//	ADC의 값을 문자열로 변경.
		Puts0( p );
		_delay_ms( 500 );
	}
}

/*	ADC값을 읽어서 리턴하는 함수	*/
unsigned short ReadADC(void)
{
	unsigned char adc_low, adc_high;
	unsigned short value;			//	ADC값은 2바이트로 표현 된다.
	
	//	0x40 = 0b01000000 <- ADCSRA 레지스터의 SDSC의 비트를 '1'로 설정하기 위한 과정  
	ADCSRA |= 0x40;		//	ADC start conversion, ADSC = '1' (비트5)
	
	//	ADCSRA & 0x10을 한 결과는 ADIF의 비트값을 값을 확인하기 위함이다.
	//	데이터가 들어왔다면 ADIF의 비트는 '1'로 설정된다.
	//	 ADIF의 비트는 '1'로 설정되면 while 루프를 빠져나온다.
	while ( ( ADCSRA & 0x10 ) != 0x10 );	//	ADC 변환 완료 검사 (ADIF값을 판단)
	
	/*
		ADC 변환이 완료되면, 그 값을 읽어온다.
	*/
	
	adc_low = ADCL;		//	변환된 Low값 읽어오기
	adc_high = ADCH;	//	변환된 High값 읽어오기
	
	value = ( adc_high << 8 ) | adc_low;	//	value는 high 및 Low 연결. 16비트값
	
	return value;
	
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
	while ( *str != '\0' )
	{
		PutChar0(*str);
		str++;
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