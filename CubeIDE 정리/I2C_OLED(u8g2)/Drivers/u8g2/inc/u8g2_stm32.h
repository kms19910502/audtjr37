/*
 * u8g2_stm32.h
 *
 *  Created on: May 4, 2023
 *      Author: audtj37
 */

#ifndef CMSIS_U8G2_INC_U8G2_STM32_H_
#define CMSIS_U8G2_INC_U8G2_STM32_H_

#define I2C_ADDRESS  0x3C  //어드레스 주소

extern I2C_HandleTypeDef hi2c1;
extern DMA_HandleTypeDef hdma_i2c1_tx;
extern DMA_HandleTypeDef hdma_i2c1_rx;

void u8g2stm32_init(u8g2_t *u8g2);
uint8_t u8x8_byte_stm32hal_hw_i2c(u8x8_t *u8x8,
		uint8_t msg, uint8_t arg_int, void *arg_ptr);
uint8_t stm32_gpio_and_delay_cb(u8x8_t *u8x8,
		uint8_t msg, uint8_t arg_int, void *arg_ptr);

#endif /* CMSIS_U8G2_INC_U8G2_STM32_H_ */
