# Importando biblioteca numpy e json.
import numpy as np

# Inicializando uma função 'calculate' que recebe como parâmtro uma lista 'values'.
def calculate(values):
    # Verificando se a lista contém o número necessário de elementos
    if len(values) < 9: 
        print("ValueError: List must contain nine numbers.")
    else:
        # Criando um array numpy e transforma-o em uma matriz 3x3.
        uniArray = np.array(values)
        array = np.reshape(uniArray, (3, 3))

        # Utilizando métodos do numpy para calcular os valores necessários em cada eixo.
        meanArray = [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean().tolist()]
        varianceArray = [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var().tolist()]
        stdArray = [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std().tolist()]
        maxArray = [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max().tolist()]
        minArray = [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min().tolist()]
        sumArray = [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum().tolist()]

        # Criando o objeto a ser retornado como resposta.
        result = {
            'mean': meanArray,
            'variance': varianceArray,
            'standard deviation': stdArray,
            'max': maxArray,
            'min': minArray,
            'sum': sumArray
        }
        print(result)

# Teste
calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])