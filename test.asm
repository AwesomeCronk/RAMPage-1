#ruledef
{
    set {value: u6} => 0b00 @ value
    cpr {value: u6} => 0b01 @ value
    cpm {value: u6} => 0b10 @ value
    jmp {value: u6} => 0b11 @ value
}

entry:
    set 0b000000
    set 0b010101
    cpr a
    set 0b010110
    cpr b
    set 0b010111
    cpm q

a:
    #d8 0b00001101
b:
    #d8 0b01000101
q:
    #d8 0b00000000