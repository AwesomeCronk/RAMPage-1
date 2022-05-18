#include "RAMPage-1.asm"

; clk halts at end of each block to prevent them from rolling over into each other

entry:
    set 0b010000    ; ar gp_a
    set 0b001101    ; jmp alu_true
    set 0b001001    ; clk step
    cpr all_ones
    cpr zero
    jmp end
    cpr one
    cpr two
    cpr three
    cpr four
    cpr five

end:
    cpr all_ones
    set 0b001000    ; clk halt

zero:
    #d8 0b00000000
one:
    #d8 0b00000001
two:
    #d8 0b00000010
three:
    #d8 0b00000011
four:
    #d8 4
five:
    #d8 5
all_ones:
    #d8 0b11111111