class pyElement(element):
    def __init__(self, *args):
        element.__init__(self)
        print(args)

        self.data = ['00000000'] * (2 ** 11)
        self.addrInputs = ['a{}'.format(i) for i in range(11)]
        self.dataInputs = ['i{}'.format(i) for i in range(8)]
        self.dataOutputs = ['o{}'.format(i) for i in range(8)]

        for name in self.addrInputs:
            self.addInput(pin(name))
        for name in self.dataInputs:
            self.addInput(pin(name))
        self.addInput(pin('w'))
        for name in self.dataOutputs:
            self.addOutput(pin(name))

    def update(self):
        addr = '0b'
        inputsOK = True
        for name in self.addrInputs:
            value = self.inputs[name].value
            if value in (0, 1):
                addr += str(value)
            else:
                inputsOK = False
                break

        if not self.inputs['w'].value in (0, 1):
            inputsOK = False
        elif self.inputs['w'].value:
            val = ''
            for name in self.dataInputs:
                val += str(self.inputs[name].value)
            self.data[addr] = val

        if inputsOK:
            addr = int(addr, base=2)
            for i, name in enumerate(self.dataOutputs):
                self.outputs[name].set(int(self.data[addr][i]))
