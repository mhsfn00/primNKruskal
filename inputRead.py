"""
entrada:    A B C D
            A B 1
            B C 1
            C D 1
            D A 1

não precisa verificar a entrada

saida:  C B 1
        B A 1
        A D 1
        D C 1
        custo_total = 4

duas saídas: saida.pri saida.kru
"""

#Gerar arvore mínima utilizando os dois algoritmos (prim e kruskal)
#No algoritmo de prim pode começar pela aresta de menor peso ou por qualquer vertice
#des de que apartir desse vertice seja escolhido a menor aresta disponível. Esses dois
#inícios geram a mesma árvore porém com ordens diferentes.

entrada = [
    {"v1": ["A", "B", 1]},
    {"v2": ["B", "C", 1]},
    {"v3": ["C", "D", 1]},
    {"v4": ["D", "E", 1]},
]

arvore_saida = [
    {"v2" : ["B", "C", 1]},
    {"v1" : ["A", "B", 1]},
    {"v5" : ["A", "D", 1]}
]

#Ordenar o grafo de acordo com os peosos
def sort_graph_merge(graph):
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    leftSide = array[:middle]
    rightSide = array[middle:]
    leftSide = merge_sort(leftSide)
    rightSide = merge_sort(rightSide)

    return merge(leftSide, rightSide)

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    
    while leftIndex < len(left):
        result.append(left[leftIndex])
        leftIndex += 1
    while rightIndex < len(right):
        result.append(right[rightIndex])
        rightIndex += 1
    
    return result