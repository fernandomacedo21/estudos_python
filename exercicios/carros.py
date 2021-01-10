class Carro (object):
    def _init_(self,caminho):
        self.caminho = caminho
    def andar (self):
        print ('Andando pela', self.caminho)
