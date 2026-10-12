#usando o padrao strategy pra fazer um programa simples de escolha de frete
#etapa red - o programa da errado
#etapa green - o programa da certo mas não é o ideal
from abc import ABC, abstractmethod

# Padrão de Projeto: Strategy
# Participante: Strategy (Interface)
class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass

# Participante: ConcreteStrategy
class FreteNormal(EstrategiaFrete):
    def calcular(self) -> float:
        return 10.00

# Participante: ConcreteStrategy
class FreteExpresso(EstrategiaFrete):
    def calcular(self) -> float:
        return 20.00

# Participante: ConcreteStrategy
class FreteRetirada(EstrategiaFrete):
    def calcular(self) -> float:
        return 0.00

# Participante: Context
class CalculadoraDeFrete:
    def __init__(self, estrategia: EstrategiaFrete):
        self._estrategia = estrategia

    def calcular(self) -> float:
        return self._estrategia.calcular()

def calcular_frete(modalidade: str) -> float:
    estrategias = {
        "normal": FreteNormal(),
        "expresso": FreteExpresso(),
        "retirada": FreteRetirada()
    }
    
    estrategia_escolhida = estrategias.get(modalidade)
    
    if not estrategia_escolhida:
        raise ValueError("Modalidade de frete invalida")
        
    contexto = CalculadoraDeFrete(estrategia_escolhida)
    return contexto.calcular()

#autoavlaiação:
#com menos pressão e mais tempo eu consegui entender melhor o que eu estava fazendo
#consegui completar o programa e os testes, e seguir o red green e refactor e entender eles
#usei IA para me auxiliar e nao deu problemas: https://share.gemini.google/s3bBKwuUa24t
