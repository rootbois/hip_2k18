-- ADC reader: reads data from ADXL345

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity g_reader is port (
	clk_50: in std_logic;	-- 50 MHz clock
	
	reset_n : in std_logic; -- reset signal (active low)

	-- SPI interface
	CS_N : out std_logic;   -- connected to chip select of g sensor
	SCLK : out std_logic;   -- spi clock
	SDIO : inout std_logic; -- spi data (bidirectional)
		
	-- data output
	dataX : out std_logic_vector(12 downto 0);
	dataY : out std_logic_vector(12 downto 0);
	dataZ : out std_logic_vector(12 downto 0)
);
end g_reader;


architecture behavior of g_reader is
	
begin



if (SCLK'event and SCLK = '0')
	-- states:
	-- init0 -> Register 0x31:
	--				Set SELF_TEST bit to 0:	disables self-test force
	-- 			Set SPI bit to 1: 		sets device to 3-wire SPI mode
	--				Set INT_INVERT bit to 0:sets interrupts to active high
	--				Set Justify bit to 0:	selects right-justified mode with sign extension
	--				Set FULL_RES bit to 1:	device is in full resolution mode, output res increaseswith g range +-2g (Given by Rangebits)
	--	init1 ->	Register 0x24:
	--				Set threshold value for detecting activity to 2 (with scale factor of 62.5 mg/LSB)
	-- init2 -> Register 0x2C:
	-- 			Set LOW_POWER bit to 0:	select normal operation, not reduced power
	--				Set Rate bits to 1001:	Output Data Rate (Hz) -> 50; Bandwidth (Hz) -> 25
	--	init3 -> Register 0x2E:
	--				Set Activity bit to 1:	enables Activity Function to generate interrupts
	--				Set other bits to 0:		disables DATA_READY, SINGLE_TAP, DOUBLE_TAP, Inactivity, FREE_FALL, Watermark, Overrun functions from generating interrupts
	--	init4 -> Register 0x2D:
	--				Set Link bit to 0:		inactivity and activity functions are concurrent
	--				Set AUTO_SLEEP bit to 0:disables automatic switching to sleep mode
	-- 			Set Measure bit to 1:	Places Part into measurement mode
	--				Set Sleep bit to 0:		Puts Part into normal mode
	--				Set Wakeup bits to '00':frequency readings in Sleep Mode set to 8 Hz

	if (state = init0)
		SDIO <= '0011000101001000';
		transmission_count = tranmission_count + 1;
	elsif (state = init1)
		SDIO <= '0010010000000010';
		transmission_count = tranmission_count + 1;
	elsif (state = init2)
		SDIO <= '0010110000001001';
		transmission_count = tranmission_count + 1;
	elsif (state = init3)
		SDIO <= '0010111000010000';
		transmission_count = tranmission_count + 1;
	elsif (state = init4)
		SDIO <= '0010110100001000';
		transmission_count = tranmission_count + 1;
	elsif (state = readX)
		SDIO <= '11110010';
		SDIO <= 'Z';
		transmission_count = tranmission_count + 1;
	elsif (state = readY)
		SDIO <= '11110100';
		SDIO <= 'Z';
		transmission_count = tranmission_count + 1;
	elsif (state = readZ)
		SDIO <= '11110110';
		SDIO <= 'Z';
		transmission_count = tranmission_count + 1;
	elsif (state = pause)
		SDIO <= 'Z';
		transmission_count = 0;
		
	end if
end if
	
end behavior;

