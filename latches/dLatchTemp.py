class pyElement(element):
    def __init__(self):
        element.__init__(self)
        self.addInput(pin('in'))
        self.addInput(pin('w'))
        self.addOutput(pin('out'))
        self.value = 0

    def update(self):
        if None in [pin.value for pin in self.inputs.values()]:
            self.outputs['out'].set(None)
        else:
            if self.inputs['w'].value:
                self.value = self.inputs['in'].value
            self.outputs['out'].set(self.value)
