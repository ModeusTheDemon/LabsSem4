"""
Graham(Q)
1) Пусть p 0  — точка из множества Q с минимальной координатой y или самая левая из таких точек при наличии совпадений
2) Пусть < p 1 , p 2 , … , p m >  — остальные точки множества Q, отсортированные в порядке
возрастания полярного угла, измеряемого против часовой стрелки относительно точки p 0
     (если полярные углы нескольких точек совпадают, то по расстоянию до точки p 0 )
3) Push( p 0,S)
4) Push( p 1,S)
5) for i = 2 to m do
6)     while угол, образованный точками NextToTop(S),Top(S) и p i, образуют не левый поворот
            (при движении по ломаной, образованной этими точками, мы движемся прямо или вправо)
7)       do Pop(S)
8)    Push( p i ,S)
9) return S
"""
from typing import List, Tuple
from math import atan


def distance_from_lowest(dot: Tuple[int, int], lowest: Tuple[int, int]) -> float:
    return (abs(lowest[0] - dot[0])**2 + (lowest[1] - dot[1])**2)**0.5


def polar_angle(dot: Tuple[int, int]) -> float:
    if dot[0] == 0: dot = (dot[0] + 0.001, dot[1])
    if dot[1] == 0: dot = (dot[0], dot[1] + 0.001)
    return atan(dot[1]/dot[0])


def graham(q: List[Tuple[int, int]]) -> List[Tuple[int, int]]: # q - множество всех координат точек
    s = [] # Стек чисел
    p0 = sorted(q, key=lambda x: x[1])[0] # Минимальная из точек (по y) или самая левая из них
    q.remove(p0)

    q.sort(key=lambda x: distance_from_lowest(x, p0)) # Сортировка списка точек по расстоянию до минимальной
    q.sort(key=lambda x: polar_angle(x)) # Сортировка списка точек по полярному углу отн. минимальной

    s.append(p0)
    s.append(q[0])

    for i in range(1, len(q)):
        #  условие левого угла: u x v y − u y v x ⩾ 0, где u = { b x − a x , b y − a y } , v = { c x − b x , c y − b y }
        u = (s[-1][0] - s[-2][0], s[-1][1] - s[-2][1])
        v = (q[i][0] - s[-1][0], q[i][1] - s[-1][1])
        while u[0] * v[1] - u[1] * v[0] < 0:
            s.pop()
            u = (s[-1][0] - s[-2][0], s[-1][1] - s[-2][1])
            v = (q[i][0] - s[-1][0], q[i][1] - s[-1][1])
        s.append(q[i])

    return s


Dots = [(4, 2), (6, 4), (10, 4), (6, 6), (2, 8), (8, 10), (8, 2), (0, 4), (2, 6), (8, 7.5)]

print(graham(Dots))
