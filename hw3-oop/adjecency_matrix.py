# Напишите программу, которая строит матрицу смежности графа на основе списков смежности для каждой вершины.
#
# Входные данные
#
# В первой строке вводится количество вершин графа N ( 1≤ N ≤1000 ).
# В следующих N строках записаны списки смежности для каждой вершины – номера вершин, в которые существуют исходящие рёбра из данной вершины.
#
# Выходные данные
#
# Программа должна вывести матрицу смежности для заданного графа.


class Graph:
    def __init__(self):
        self.adj_matrix = []

    def create_from_list(self, adj_list, dim):
        self.adj_matrix = [[0 for j in range(dim)] for i in range(dim)]
        for i in range(dim):
            for j in adj_list[i]:
                if j != 0:
                    self.adj_matrix[i][j-1] = 1

    def print_matrix(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                print(self.adj_matrix[i][j], end=' ')
            print()


g = Graph()
n = int(input())
m = []
for i in range(n):
    m.append([int(j) for j in input().split()])
g.create_from_list(m, n)
g.print_matrix()
