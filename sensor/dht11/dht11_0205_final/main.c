#define F_CPU 16000000UL
#include <stdio.h>
#include <string.h>
#include <avr/io.h>
#include <util/delay.h>
#include "dht11.h"
#include "uart.h"

int main(){
	uint8_t data = 0;
	char buf[40] = {0,};
	USART_Init();
	
	while (1){
		dht11_getdata(0, &data);
		sprintf(buf, "Temp:%d", data);
		strTransmit(buf);
		memset(buf, 0x00, 40);
		_delay_ms(1000);
		
		dht11_getdata(1, &data);
		sprintf(buf, "//Humi:%d", data);
		strTransmit(buf);
		memset(buf, 0x00, 40);
		_delay_ms(1000);
	}
	
}