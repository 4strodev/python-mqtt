class persiana:

    def __init__(self, obert: bool):
        self.obert = obert

    def obrirPersiana(self):
        self.obert = True;
        return self.obert

    def tencarPersiana(self):
        self.obert = False
        return self.obert