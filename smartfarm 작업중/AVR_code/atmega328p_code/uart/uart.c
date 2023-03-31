#include <avr/io.h>
#include "uart.h"


void USART_Init(void)
{
	UCSR0A=0x00; // clear
	UCSR0B=(1<<RXEN0) | (1<<TXEN0); // Rx, Tx Enable
	UCSR0C=(0<<UCSZ02) | (1<<UCSZ01) | (1<<UCSZ00); // Tx data len : 8-bit
	
	UBRR0H=0;
	UBRR0L=103; // baudrate 9600bps
}

unsigned char USART_Receive(void)
{
	while(!(UCSR0A & (1<<RXC0))); // Wait for data to be received
	return UDR0; // Get and return received data form buffer
}

void USART_Transmit(unsigned char data)
{
	while(!(UCSR0A & (1<<UDRE0))); // Wait for empty transmit buffer
	UDR0=data; // Put data into buffer, sends the  data
}

void strTransmit(char *str) {
	while (*str) {
		USART_Transmit(*str);
		str++;
	}
	USART_Transmit(10); // 개행문자
}