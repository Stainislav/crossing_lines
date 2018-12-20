'''
Запуск программы:

1. Вводим в консоли: python3 crossing_lines.py

2. Вводим три строки с координатами точек.

3. Жмём два раза "Enter".


Алгоритм:

1. Получаем на вход координаты 12-ти точек.

2. Создаём 6 точек.

3. Создаём 3 прямые.

4. Находим точки пересечения этих прямых.

5. Если три прямые пересекаются более, чем в одной точке,
значит они образуют треугольник.

   Вычисляем площадь треугольника.

'''


import math


def main():

    coordinates = ""
    stop_sym = ""

    while True:

        line = input() 
        if line.strip() == stop_sym:
            break

        coordinates = coordinates + " " + line
    
    coordinates = coordinates.split()
    crossing_lines(coordinates)
    
    return 0


class Point:
    def __init__(self, x, y):
        self.x = float(x)        
        self.y = float(y)        
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)


class Line:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point
                                                                                                                                      

def crossing_lines(coordinates):

    if len(coordinates) != 12:
        print("Количество координат должно быть равно 12!")
        return 1

    # Создаём точки.
    A1 = Point(coordinates[0], coordinates[1])
    A2 = Point(coordinates[2], coordinates[3])

    B1 = Point(coordinates[4], coordinates[5])
    B2 = Point(coordinates[6], coordinates[7])

    C1 = Point(coordinates[8], coordinates[9])
    C2 = Point(coordinates[10], coordinates[11])

    # Создаём прямые.
    A = Line(A1, A2)
    B = Line(B1, B2)
    C = Line(C1, C2)
          
    # Находим точки пересечения прямых.
    AB_cross_point = get_cross_point(A, B)
    AC_cross_point = get_cross_point(A, C)
    BC_cross_point = get_cross_point(B, C)
    
    triangle_square = 0

    if AB_cross_point == 0 and AC_cross_point == 0:
        answer = "a || b || c"

    elif AB_cross_point == 0:
        answer = "a || b"

    elif AC_cross_point == 0:
        answer = "a || c"

    elif BC_cross_point == 0:
        answer = "b || c"

    elif AB_cross_point and AC_cross_point and BC_cross_point:
        answer = "a /\ b /\ c"

        # Если две точки пересечения не совпадают, значит прямые образуют треугольник.
        if AB_cross_point != AC_cross_point:
            triangle_square = get_triangle_square(AB_cross_point, BC_cross_point, AC_cross_point)

    print(answer)
    print(triangle_square)


def get_cross_point(first_line, second_line):
        
        # Получаем координаты точек для первой прямой.
        a_x1 = first_line.first_point.x
        a_y1 = first_line.first_point.y

        a_x2 = first_line.second_point.x
        a_y2 = first_line.second_point.y

        # Получаем координаты точек для второй прямой.
        b_x1 = second_line.first_point.x
        b_y1 = second_line.first_point.y
    
        b_x2 = second_line.second_point.x
        b_y2 = second_line.second_point.y

        # Вычисляем постоянные для первой прямой.
        A1 = a_y1 - a_y2
        B1 = a_x2 - a_x1
        C1 = a_x1 * a_y2 - a_x2 * a_y1

        # Вычисляем постоянные для второй прямой.
        A2 = b_y1 - b_y2
        B2 = b_x2 - b_x1
        C2 = b_x1 * b_y2 - b_x2 * b_y1
    
        # Находим точку пересечения.
        if B1*A2 - B2*A1 and A1:
            y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            x = (-C1 - B1*y) / A1

            point = Point(x, y)
            return point

        elif B1*A2 - B2*A1 and A2:
            y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
            x = (-C2 - B2*y) / A2

            point = Point(x, y)
            return point

        # Нет точек пересечения.
        else:
            return 0


def get_triangle_square(first_point, second_point, third_point):

    # Получаем стороны треугольника.
    a = get_distance(first_point, third_point)
    b = get_distance(first_point, second_point)
    c = get_distance(second_point, third_point)
    
    # Находим полупериметр.
    p = (a + b + c) / 2

    # Находим площадь треугольника по формуле Герона.
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
  
    triangle_square = round(s, 2)
     
    return triangle_square
    

def get_distance(first_point, second_point):

    x1 = first_point.x
    y1 = first_point.y
 
    x2 = second_point.x
    y2 = second_point.y

    return math.hypot(x2 - x1, y2 - y1)


if __name__ == "__main__":
    main()
