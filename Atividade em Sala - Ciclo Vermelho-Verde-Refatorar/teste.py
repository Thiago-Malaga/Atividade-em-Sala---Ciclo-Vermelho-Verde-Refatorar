#quero usar o padrão strategy pq eh o mais facil de implementar
#peguei a ideia de fazer de frete porque não precisa criar arquivos extras
#vou fazer e testar 3 casos: calcular_frete("normal"), calcular_frete("expresso"), 
#calcular_frete("retirada") e esses teste vao representar a versao da classe com strategy final
# estou usando IA para auxiliar nas minhas duvidas: https://share.gemini.google/s3bBKwuUa24t

import pytest
from programa import calcular_frete

def test_calcular_frete_normal():
    assert calcular_frete("normal") == 10.0  # Exemplo de valor esperado

def test_calcular_frete_expresso():
    assert calcular_frete("expresso") == 20.0  # Exemplo de valor esperado

def test_calcular_frete_retirada():
    assert calcular_frete("retirada") == 0.0  # Exemplo de valor esperado

def test_calcular_frete_invalido():
    with pytest.raises(ValueError):
        calcular_frete("invalido")  # Deve lançar ValueError para tipo de frete inválido
