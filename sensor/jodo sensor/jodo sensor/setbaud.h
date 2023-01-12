#ifndef BAUD
#error BAUD is not defined
#endif

#include <util/setbaud.h>

#ifndef F_CPU
#error F_CPU is not defined
#endif

#if USE_2X
#define UART_BAUD_RATE ((F_CPU / (8UL * BAUD)) - 1)
#else
#define UART_BAUD_RATE ((F_CPU / (16UL * BAUD)) - 1)
#endif

#define UBRR_VALUE ((UART_BAUD_RATE >> 8) & 0xff)
#define UBRRL_VALUE (UART_BAUD_RATE & 0xff)
#define UBRRH_VALUE UBRR_VALUE