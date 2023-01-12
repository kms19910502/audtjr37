#define F_CPU 16000000UL	//	16MHz
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>

/*	���� �ϳ��� �����ϴ� �Լ�	*/
void PutChar0(char c);

/*	���ڿ��� �����ϴ� �Լ�	*/
void Puts0(char* str);

/*	���ڿ��� �����ϴ� �Լ�	*/
char Gets0(void);

void Init_UART0(void)
{
	//	UCSR0B�� Tx, Rx�� �����Ѵ�. Tx(08), Rx(10)���� ����
	UCSR0B = 0x18;		//	Tx�� Rx�� �����Ѵ�. ��/���� �����ϵ��� ����
	UCSR0C = 0x06;		//	8bit data, no parity(0), 1 stop bit(0) ����
	
	//	�ٿ�� ����Ʈ ����. 9600baud rate�� ����. 115200baud rate�� 8�� ����
	UBRR0H = 0;
	UBRR0L = 103;
}

/*	ADC���� �о �����ϴ� �Լ�	*/
unsigned short ReadADC(void);

int main(void)
{
	char p[12];
	/*
	ADMUX |= 0x40;						//	AVCC�� ������������ ����
	ADCSRA |= 0x07;						//	���ֺ� 128�� ����
	ADCSRA |= ( 1 << ADEN );			//	ADC Ȱ��ȭ
	ADCSRA |= ( 1 << ADATE );			//	�ڵ� Ʈ���� ���
	ADMUX |= ( ( ADMUX & 0xE0 ) | 0 );	//	ä�� ����
	ADCSRA |= ( 1 << ADSC );			//	��ȯ����
	*/
	
	//	���� ������ �� ���� ó���� ������ �Ʒ��� �� ����
	ADMUX = 0x40;	//	ADC0�� ����� ���̴�. ��, �Ƶ��̳��� A0���� ����Ѵ�.
	ADCSRA = 0x87;	//	0x87 = 0b1000 0111
	
	Init_UART0();
	
	while (1)
	{
		sprintf( p, "light : %d\n", ReadADC() );	//	ADC�� ���� ���ڿ��� ����.
		Puts0( p );
		_delay_ms( 500 );
	}
}

/*	ADC���� �о �����ϴ� �Լ�	*/
unsigned short ReadADC(void)
{
	unsigned char adc_low, adc_high;
	unsigned short value;			//	ADC���� 2����Ʈ�� ǥ�� �ȴ�.
	
	//	0x40 = 0b01000000 <- ADCSRA ���������� SDSC�� ��Ʈ�� '1'�� �����ϱ� ���� ����  
	ADCSRA |= 0x40;		//	ADC start conversion, ADSC = '1' (��Ʈ5)
	
	//	ADCSRA & 0x10�� �� ����� ADIF�� ��Ʈ���� ���� Ȯ���ϱ� �����̴�.
	//	�����Ͱ� ���Դٸ� ADIF�� ��Ʈ�� '1'�� �����ȴ�.
	//	 ADIF�� ��Ʈ�� '1'�� �����Ǹ� while ������ �������´�.
	while ( ( ADCSRA & 0x10 ) != 0x10 );	//	ADC ��ȯ �Ϸ� �˻� (ADIF���� �Ǵ�)
	
	/*
		ADC ��ȯ�� �Ϸ�Ǹ�, �� ���� �о�´�.
	*/
	
	adc_low = ADCL;		//	��ȯ�� Low�� �о����
	adc_high = ADCH;	//	��ȯ�� High�� �о����
	
	value = ( adc_high << 8 ) | adc_low;	//	value�� high �� Low ����. 16��Ʈ��
	
	return value;
	
}

/*	���� �ϳ��� �����ϴ� �Լ�	*/
void PutChar0(char c)
{
	//	5��° ��Ʈ�� �������� ������ while���� ���� �ݺ��ϴµ�
	//	5��° ��Ʈ�� ������ ������ while ������ �������ͼ� �����͸� �����ϴ� ����
	
	//	�����Ͱ� ������ �ʾҴٸ� while�� �ݺ�
	while ( !( UCSR0A & 0x20 ) );	//	5��° bit�� ���
	
	//	�����͸� ����
	UDR0 = c;
}

/*	���ڿ��� �����ϴ� �Լ�	*/
void Puts0(char* str)
{
	while ( *str != '\0' )
	{
		PutChar0(*str);
		str++;
	}
}

/*	���ڿ��� �����ϴ� �Լ�	*/
char Gets0(void)
{
	//	�����Ͱ� ������ �ʾҴٸ� while�� �ݺ�
	while ( !( UCSR0A & 0x80 ) );	//	RXC�� Set(8��° �ڸ�)�Ǿ� �־�� �Ѵ�.
	
	//	�����͸� ����
	return UDR0;
}