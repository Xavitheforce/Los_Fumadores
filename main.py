import threading
import time
from agente import Agente
from fumador import Fumador

class Simulacion:
    def __init__(self):
        self.agente = Agente()
        self.fumadores = [Fumador('1', 'tabaco', self.agente), Fumador('2', 'papel', self.agente), Fumador('3', 'cerillas', self.agente)]

    def iniciar(self):
        for fumador in self.fumadores:
            threading.Thread(target=fumador.esperar_ingrediente).start()
        while True:
            self.agente.poner_ingredientes()
            time.sleep(2)

simulacion = Simulacion()
simulacion.iniciar()