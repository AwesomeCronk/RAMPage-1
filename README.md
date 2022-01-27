### Specs:
* Bus width: `8b`
* Address width: `11b`

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

01xxxx - Active register
  0000 - GP A
  0001 - GP B
  0010 - GP C
  0011 - GP D
  0100 - GP E
  0101 - ALU A
  0110 - ALU B
  0111 - ALU result (read-only)
  1000 - Flags (read-only)
  1001 - GPIO direction A
  1010 - GPIO A 
  1011 - GPIO direction B
  1100 - GPIO B
  1101 - Parallel port
  1110 - I2C A
  1111 - I2C B

1xxxxx - Memory page
```