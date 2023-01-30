#ifndef UART_H_
#define UART_H_

void USART_Init(void);
unsigned char USART_Receive(void);
void USART_Transmit(unsigned char data);
void strTransmit(char *str);

#endif /* UART_H_ */