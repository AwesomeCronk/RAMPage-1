controlLines = [
    'MP_In',
    'MA_In',
    'MD_In',
    'MD_Out',
    'AR_In',
    'AR_Out',
    'PC_Inc',
    'PC_In',
    'PC_Out',
    'SC_Res',
    'IR_In',
    'IR_Out',
    'Set',
    '',
    '',
    ''
]
steps = 8

fetch = [
    ['PC_Out', 'MA_In'],
    ['MD_Out', 'IR_In']
]

SET = [
    *fetch,
    ['IR_Out', 'Set'],
    ['PC_Inc', 'SC_Res'],
    [],
    [],
    [],
    []
]
CPR = [
    *fetch,
    ['IR_Out', 'MA_In'],
    ['MD_Out', 'AR_In'],
    ['PC_Inc', 'SC_Res'],
    [],
    [],
    []
]
CPM = [
    *fetch,
    ['IR_Out', 'MA_In'],
    ['AR_Out', 'MD_In'],
    ['PC_Inc', 'SC_Res'],
    [],
    [],
    []
]
JMP = [
    *fetch,
    [],
    [],
    [],
    [],
    [],
    []
]

instructions = {'SET': SET, 'CPR': CPR, 'CPM': CPM, 'JMP': JMP}

if __name__ == '__main__':
    binary = []
    for instructionName in instructions.keys():
        print(instructionName)
        instruction = instructions[instructionName]
        instructionBinary = []
        for s, step in enumerate(instruction):
            stepBinary = [0] * len(controlLines)
            for line in step:
                assert line in controlLines
                stepBinary[controlLines.index(line)] = 1
            print('{}: {} - {}'.format(s, ', '.join(step).ljust(20), ''.join([str(bit) for bit in stepBinary])))
            instructionBinary += stepBinary
        binary += instructionBinary


    with open('Microcode.bin', 'wb') as microcodeFile:
        number = 0
        for bit in binary:
            number *= 2
            number += bit
        microcodeFile.write(int.to_bytes(number, len(binary) // 8, 'big'))
        print(bytearray(int.to_bytes(number, len(binary) // 8, 'big')).hex())