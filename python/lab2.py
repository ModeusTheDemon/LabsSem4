"""
Записать алгоритмы нахождения точек пересечения двух прямых,
прямой и отрезка, двух отрезков, прямой и окружности, отрезка и
окружности, двух окружностей.
Данные алгоритмы используются при решении следующей задачи:
Дано N точек координатами (X, Y). Выяснить, есть ли в этом
множестве точек координаты вложенных друг в друга треугольников.
"""
import math


def line_intersection(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:  # Прямые параллельны
        return None

    u = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    x = x1 + u * (x2 - x1)
    y = y1 + u * (y2 - y1)
    return x, y


def line_segment_intersection(line, segment):
    (x1, y1), (x2, y2) = line
    (x3, y3), (x4, y4) = segment

    line_pt = line_intersection(line, (segment[0], segment[1]))
    if not line_pt:
        return None

    # Проверка принадлежности точки отрезку
    x, y = line_pt
    if (min(x3, x4) <= x <= max(x3, x4)) and (min(y3, y4) <= y <= max(y3, y4)):
        return x, y
    return None


def segment_intersection(seg1, seg2):
    pt = line_intersection(seg1, seg2)
    if not pt:
        return None

    x, y = pt
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    if (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and
            min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4)):
        return pt
    return None


def line_circle_intersection(line, center, radius):
    (x1, y1), (x2, y2) = line
    h, k = center

    dx = x2 - x1
    dy = y2 - y1
    A = dx ** 2 + dy ** 2
    B = 2 * (dx * (x1 - h) + dy * (y1 - k))
    C = (x1 - h) ** 2 + (y1 - k) ** 2 - radius ** 2

    discriminant = B ** 2 - 4 * A * C
    if discriminant < 0:
        return []

    t1 = (-B + math.sqrt(discriminant)) / (2 * A)
    t2 = (-B - math.sqrt(discriminant)) / (2 * A)

    points = []
    for t in [t1, t2]:
        if 0 <= t <= 1:
            x = x1 + t * dx
            y = y1 + t * dy
            points.append((x, y))
    return points


def segment_circle_intersection(segment, center, radius):
    return line_circle_intersection(segment, center, radius)


def circle_circle_intersection(c1, r1, c2, r2):
    (x1, y1), (x2, y2) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1)

    if d > r1 + r2 or d < abs(r1 - r2):
        return []  # Нет пересечений

    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(r1 ** 2 - a ** 2)

    xm = x1 + a * (x2 - x1) / d
    ym = y1 + a * (y2 - y1) / d

    xs = [
        xm + h * (y2 - y1) / d,
        xm - h * (y2 - y1) / d
    ]
    ys = [
        ym - h * (x2 - x1) / d,
        ym + h * (x2 - x1) / d
    ]
    return list(zip(xs, ys))


def is_point_inside_triangle(p, triangle):
    (x, y) = p
    (x1, y1), (x2, y2), (x3, y3) = triangle

    area = 0.5 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3)
    s = 1 / (2 * area) * (y1 * x3 - x1 * y3 + (y3 - y1) * x + (x1 - x3) * y)
    t = 1 / (2 * area) * (x1 * y2 - y1 * x2 + (y1 - y2) * x + (x2 - x1) * y)
    return s > 0 and t > 0 and (1 - s - t) > 0


def has_nested_triangles(points):
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                tri1 = (points[i], points[j], points[k])
                for l in range(n):
                    if l in [i, j, k]:
                        continue
                    for m in range(l + 1, n):
                        if m in [i, j, k]:
                            continue
                        for o in range(m + 1, n):
                            if o in [i, j, k]:
                                continue
                            tri2 = (points[l], points[m], points[o])

                            # Проверка вложенности tri1 внутри tri2
                            if all(is_point_inside_triangle(p, tri2) for p in tri1):
                                return True
                            # Проверка вложенности tri2 внутри tri1
                            if all(is_point_inside_triangle(p, tri1) for p in tri2):
                                return True
    return False


# Пример данных
points = [(0, 0), (2, 0), (1, 2), (0.5, 0.5), (1.5, 0.5), (1, 1)]

# Проверка на вложенность
print(has_nested_triangles(points))  # Вернет True, если есть вложенные треугольники