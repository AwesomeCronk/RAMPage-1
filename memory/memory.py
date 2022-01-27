import logging
log = logging.getLogger('memory.py')

class pyElement(element):
    def __init__(self, *args):
        element.__init__(self)

        self.data = [0] * (2 ** 11)
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
        addr = 0
        for name in self.addrInputs:
            value = self.inputs[name].value
            # log.debug(value)
            addr *= 2
            if value == 1:
                addr += 1

        # log.debug('addr: {}'.format(addr))
        
        if self.inputs['w'].value == 1:
            val = 0
            for name in self.dataInputs:
                value = self.inputs[name].value
                val *= 2
                if value == 1:
                    val += value
            self.data[addr] = val
            # log.debug('wrote {} at {}'.format(val, addr))
            # log.debug('read back {}'.format(self.data[addr]))
        
        bits = [int(i) for i in bin(self.data[addr])[2:].zfill(8)]
        for i, name in enumerate(self.dataOutputs):
            self.outputs[name].set(bits[i])
