# Напишите программу, которая строит списки смежности для каждой вершины графа на основе его матрицы смежности.
#
# Входные данные
#
# В первой строке вводится количество вершин графа N ( 1≤ N ≤ 1000 ).
# В следующих N строках записано по N чисел, разделённых пробелами – элементы матрицы смежности графа.
#
# Выходные данные
#
# Программа должна вывести списки смежности для каждой вершины графа в порядке возрастания их номеров.
# Номера вершин в каждом списке разделены пробелами. Нумерация начинается с единицы.
# Если из вершины не выходит ни одно ребро, вместо списка нужно вывести число 0.
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjecency_list = defaultdict(list)

    def create_from_matrix(self, matrix, dim):
        for i in range(dim):
            no_edges = True
            for j in range(dim):
                if matrix[i][j] == 1:
                    self.adjecency_list[i].append(j)
                    no_edges = False
            if no_edges:
                self.adjecency_list[i].append(-1)

    def print_adjecency_list(self):
        for i in self.adjecency_list:
            for j in self.adjecency_list[i]:
                if j != -1:
                    print(j+1, end=" ")
                else:
                    print(j+1, end=" ")
            print()


g = Graph()
n = int(input())
m = []
for i in range(n):
    m.append([int(j) for j in input().split()])
g.create_from_matrix(m, n)
g.print_adjecency_list()
