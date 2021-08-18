class pyElement(element):
    def __init__(self, *args):
        self.args = args
        element.__init__(self)

        self.data = ['00000000'] * (2 ** 11)
        with open(self.args[0], 'rb') as file:
            fileData = file.read()

        for i in range(2 ** 11):
            try:
                self.data[i] = bin(fileData[i])[2:].zfill(8)
            except IndexError:
                break

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
        element.update(self)

        addr = '0b'
        for name in self.addrInputs:
            addr += str(self.inputs[name].value)
        addr = int(addr, base=2)

        if self.inputs['w'].value:
            val = ''
            for name in self.dataInputs:
                val += str(self.inputs[name].value)
            self.data[addr] = val

        for i, name in enumerate(self.dataOutputs):
            self.outputs[name].set(int(self.data[addr][i]))
