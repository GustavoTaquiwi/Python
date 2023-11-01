class Computador:
    def __init__(self, nome):
        self.nome = nome
        self.monitores = []
    
    def conectar_monitor(self, monitor):
        self.monitores.append(monitor)
    
    def mostrar_monitor(self):
        for monitor in self.monitores:
            print(f'{monitor.nome} está conectado no computador {self.nome}')

class Monitor:
    def __init__(self, nome):
        self.nome = nome

computador1 = Computador('MICRO-11')
monitor1 = Monitor('Monitor Samsung')

computador1.conectar_monitor(monitor1)

computador1.mostrar_monitor()