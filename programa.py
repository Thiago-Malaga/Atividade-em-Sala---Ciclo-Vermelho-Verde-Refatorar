#usando o padrao strategy pra fazer um programa simples de escolha de frete
#etapa red - o programa da errado
#etapa green - o programa da certo mas não é o ideal

def calcular_frete(tipo_frete):
    if tipo_frete == "normal":
        return 10.0  # Valor do frete normal
    elif tipo_frete == "expresso":
        return 20.0  # Valor do frete expresso
    elif tipo_frete == "retirada":
        return 0.0   # Valor do frete para retirada
    else:
        raise ValueError("Tipo de frete inválido")
    
