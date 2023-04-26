class temperatura:

    def __init__(self, graus: int):
        self.graus = graus

    def pujarTemperatura(self,graus):
        self.graus = graus+1;
        return self.graus

    def baixarTemperatura(self,graus):
        self.graus = graus-1;
        return self.graus

    def establirTemperatura(self, temperatura):
        self.graus = temperatura
        return self.graus