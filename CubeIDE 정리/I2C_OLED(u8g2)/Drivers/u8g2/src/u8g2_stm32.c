/*
 * u8g2_stm32.c
 *
 *  Created on: May 4, 2023
 *      Author: audtj37
 */

#include "main.h"
#include "u8g2.h"
#include "u8x8.h"
#include "u8g2_stm32.h"
void u8g2stm32_init(u8g2_t *u8g2)
{
	u8g2_Setup_ssd1306_i2c_128x64_noname_f(u8g2, U8G2_R0,
			u8x8_byte_stm32hal_hw_i2c, stm32_gpio_and_delay_cb);
	u8g2_SetI2CAddress(u8g2, I2C_ADDRESS << 1);
	u8g2_InitDisplay(u8g2);
	u8g2_SetPowerSave(u8g2,0);
	u8g2_ClearDisplay(u8g2);
	u8g2_SetDrawColor(u8g2, 1);
}
uint8_t u8x8_byte_stm32hal_hw_i2c(u8x8_t *u8x8,
		uint8_t msg, uint8_t arg_int, void *arg_ptr)
{
	static uint8_t buffer[32];
	static uint8_t buf_idx;
	uint8_t *data;
	switch(msg)
	{
	case U8X8_MSG_BYTE_SEND:
	{
		data = (uint8_t *)arg_ptr;
		while(arg_int > 0)
		{
			buffer[buf_idx++] = *data;
			data++;
			arg_int--;
		}
	}
		break;
	case U8X8_MSG_BYTE_INIT:
		break;
	case U8X8_MSG_BYTE_SET_DC:
		break;
	case U8X8_MSG_BYTE_START_TRANSFER:
	{
		buf_idx = 0;
	}
		break;
	case U8X8_MSG_BYTE_END_TRANSFER:
	{
		uint8_t iaddress = I2C_ADDRESS;
		volatile uint16_t i;
		HAL_I2C_Master_Transmit_DMA(&hi2c1, (uint16_t)iaddress <<1,
				&buffer[0], buf_idx);
		for(i=1 ; i <= 5000 ; i++);  //5000은 STM32F4 84MHz 기준
	}
		break;
	default:
		return 0;
	}
	return 1;
}
uint8_t stm32_gpio_and_delay_cb(u8x8_t *u8x8,
		uint8_t msg, uint8_t arg_int, void *arg_ptr)
{
	switch(msg)
	{
	case U8X8_MSG_GPIO_AND_DELAY_INIT:
		break;
	case U8X8_MSG_DELAY_NANO:
	{
		volatile uint32_t i;
		for(i = 1 ; i <= arg_int *10 ; i++ );
	}
		break;
	case U8X8_MSG_DELAY_10MICRO:   /* not used*/
		break;
	case U8X8_MSG_DELAY_100NANO:   /* not used*/
		break;
	case U8X8_MSG_DELAY_MILLI:
		HAL_Delay(arg_int);
		break;
	default:
		u8x8_SetGPIOResult(u8x8,1);
		break;
	}
	return 1;
}
