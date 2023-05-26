################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/u8g2_stm32f4.c 

OBJS += \
./Core/u8g2_stm32f4.o 

C_DEPS += \
./Core/u8g2_stm32f4.d 


# Each subdirectory must supply rules for building sources it contributes
Core/%.o Core/%.su Core/%.cyclo: ../Core/%.c Core/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F429xx -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -I../Drivers/ssd1306 -I"C:/Users/audtj/STM32CubeIDE/workspace_1.12.1/OLED_SPI/Lib" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core

clean-Core:
	-$(RM) ./Core/u8g2_stm32f4.cyclo ./Core/u8g2_stm32f4.d ./Core/u8g2_stm32f4.o ./Core/u8g2_stm32f4.su

.PHONY: clean-Core

