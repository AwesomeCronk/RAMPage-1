#ruledef
{
    set {value: u6} => 0b00 @ value
    cpr {value: u6} => 0b01 @ value
    cpm {value: u6} => 0b10 @ value
    jmp {value: u6} => 0b11 @ value
}

entry:
    cpr data

data:
    #d8 0b00101010