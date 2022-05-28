import numpy as np


class Polyhedron(object):
    points = None
    edges_specifications = None

    @classmethod
    def polysmith(cls, figure):
        return cls(figure)

    def __init__(self, figure):
        self.matrix = self.__build_matrix()
        self.figure = figure
        self.update_figure()

    def __to_array(self, point):
        return np.array([point[0], point[1], point[2], [1]])

    def __build_matrix(self):
        return np.hstack([self.__to_array(point) for point in self.points])

    def __build_figure(self):
        ax = self.figure.gca(projection='3d')

        for i in range(1, len(self.points) + 1):
            ax.scatter(*getattr(self, f'p{i}'), c='b')
            ax.text(*getattr(self, f'p{i}'), f'P{i}', size=12, zorder=1, color='k')

        for p in self.edges_specifications.keys():
            for pl in self.edges_specifications[p]:
                _p = getattr(self, f'p{p}')
                _pl = getattr(self, f'p{pl}')
                ax.plot([_p[0], _pl[0]], [_p[1], _pl[1]], [_p[2], _pl[2]], c='r')

    def update_figure(self):
        for index in range(1, len(self.points) + 1):
            setattr(self, f'p{index}', [])

        for n, eixo in enumerate(self.matrix):
            if n == len(self.matrix) - 1:
                continue
            for index, value in enumerate(eixo):
                getattr(self, f'p{index+1}').append(value)
        self.__build_figure()

    def translation3D(self, dx, dy, dz):
        return np.array([[1, 0, 0, dx],
                         [0, 1, 0, dy],
                         [0, 0, 1, dz]
                         [0, 0, 0, 1]])


class TenPointPolyhedron(Polyhedron):
    edges_specifications = {
        1: [2, 3, 5],
        2: [4, 6],
        3: [4, 5],
        4: [6],
        5: [6, 7, 8],
        6: [9, 10],
        7: [8, 9],
        8: [10],
        9: [10]
    }

    points = [
        ([0], [0], [0]),
        ([0], [0], [-4]),
        ([2], [0], [0]),
        ([2], [0], [-4]),
        ([1], [-1], [0]),
        ([1], [-1], [-4]),
        ([0], [-2], [0]),
        ([2], [-2], [0]),
        ([0], [-2], [-4]),
        ([2], [-2], [-4]),
    ]

    @classmethod
    def create(cls, figure):
        return cls.polysmith(figure)
