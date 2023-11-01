class Cabeça:
    def __init__(self):
        pass
    
    def conectada(self):
        print('A cabeça está no boneco')
    
class Boneco:
    def __init__(self):
        self.cabeça = Cabeça()
    
    def verificar(self):
        print('Verificando cabeça...')
        self.cabeça.conectada()

boneco_de_pano = Boneco()

boneco_de_pano.verificar()