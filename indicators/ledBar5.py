class pyElement(element):
    def __init__(self, colorR, colorG, colorB, posX, posY):
        element.__init__(self)

        self.litColor = (int(colorR), int(colorG), int(colorB))
        self.dimColor = (int(self.litColor[0] / 2), int(self.litColor[1] / 2), int(self.litColor[2] / 2))
        self.pos = vec2(int(posX), int(posY))

        self.widget = widget()
        self.widget.setMode(widget.containerMode)
        self.widget.moveTo(vec2(0, 2))
        for i in range(5):
            self.widget.addWidget(widget())
            self.widget.widgets[i].resize(vec2(1,1))
            self.widget.widgets[i].moveTo(self.pos + vec2(i, 0))
            self.widget.widgets[i].setMode(widget.textMode)
            self.widget.widgets[i].setText(' ')
            self.widget.widgets[i].setBGColor(self.dimColor)
            self.addInput(pin('i{}'.format(i)))

    def update(self):
        for i, pin in enumerate(self.inputs.values()):
            if pin.value:
                self.widget.widgets[i].setBGColor(self.litColor)
            else:
                self.widget.widgets[i].setBGColor(self.dimColor)
