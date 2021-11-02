Bus width: `8b`
Address width: `11b`

### Instructions:
```
00 - SET [mode]
01 - CPR [addr]
10 - CPM [addr]
11 - JMP [addr]
```

### `[mode]` can be:
```
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
  0010 - GP B
  0011 - GP C
  0100 - GP D
  0101 - GP E
  0110 - ALU A
  0111 - ALU B
  1000 - ALU result
  1001 - Flags (read-only)
  1010 - GPIO direction A
  1011 - GPIO direction B
  1100 - GPIO A
  1101 - GPIO B
  1110 - I2C A
  1111 - I2C B

1xxxxx - Memory page ID
```