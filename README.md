Bus width: 8b
Address width: 11b

Instructions:
00 - SET [mode]
01 - CPR [addr]
10 - CPM [addr]
11 - JMP [addr]

[mode] can be:
000xxx - ALU mode
   000 - integer add
   001 - integer subtract
   010 - compare greater than
   011 - compare equal
   100 - bitwise AND
   101 - bitwse OR
   110 - bitwise shift
   111 - bitwise index

0010xx - Clock mode
    00 - slow
    01 - fast
    10 - single step/halt
    11 - reset

0011xx - Jump mode
    00 - Unconditional
    01 - ALU result true
    10 - ALU result false
    11 - Relative (*n* steps forward)

01xxxx - Register ID
  0000 - GP A
  0001 - GP B
  0010 - ALU A
  0011 - ALU B
  0100 - ALU result
  0101 - Flags (read-only)
  0110 - GPIO direction A
  0111 - GPIO direction B
  1000 - GPIO A
  1001 - GPIO B
  1010 - I2C A
  1011 - I2C B
  1100 - UART A
  1101 - UART B
  1110 - TI-Link A
  1111 - TI-Link B

1xxxxx - Memory page ID