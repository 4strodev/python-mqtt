class llum:

    def __init__(self, obert: bool):
        self.obert = obert

    def obrirLlum(self):
        self.obert = True;
        return self.obert

    def tencarLlum(self):
        self.obert = False
        return self.obert