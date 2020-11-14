import matplotlib.pyplot as plt
import numpy as np
'''
print("Type your age: ")
age = input()
print("I am " + age + " years old.")


age = int(age)


if age >= 18:
    print("Welcome to work!")
else:
    print("Keep studying!")
'''

#print("Hello world!")

'''
hello = "Hello world!"
hello = 7 + 12
print(hello)
'''

#name = input("Type your name: ")
#print("My name is " + name)

#print(int('5') == 5)
#number = input()
#print(int(number) * 2)

'''
weight = int(input("Какой у тебя вес? "))
print("Ты весишь ", weight)
if weight <= 40:
    print("Ты лёгкий")
else:
    if 40 < weight < 100:
        print("Ты среднего веса")
    else:
        if weight >= 100:
            print ("Ты тяжелый")


temp = float(input("Введите свою температуру: "))
if temp <= 37:
    print("Ты в норме")
else:
    print('Температура повышена')
'''


#masiv = [5, 'slovo', 13, 4.5]
#print(masiv)
#for i in range(0, len(masiv)):
#    print(masiv[i])

#masiv.append('esche odno slovo')
#print(masiv)
#for i in range(0, len(masiv)):
#    print(masiv[i])


'''
x = np.arange(0, 4 * np.pi, 0.01)
sin = np.sin(x)
plt.plot(x,sin)
plt.title('Graphic')
plt.legend(['sin(x)'])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
'''


















'''


matrix = [
 [1, -2, -1, -1],
 [-1, 3, -1, -1],
 [3, -8, 19, 11],
 [2, -3, -2, 9]
         ]

print("Determinant of matrix is ~",np.linalg.det(matrix))

'''

spin = 0
xrotate = 0
yrotate = 0
zrotate = 0

nx, ny, nz = 0, 0, 0

rx, ry, rz = 0, 0, 0
srx, sry, srz = 0, 0, 0


def draw_degree_point(r, degree, z):
    x = r * math.cos(math.radians(degree))
    y = r * math.sin(math.radians(degree))
    # glNormal(x, y, z)
    glVertex3f(x, y, z)


def normal_point(r, degree, z):
    x = r * math.cos(math.radians(degree))
    y = r * math.sin(math.radians(degree))
    return [x, y, z]


def normal_wall(i):
    # V1 = (C - A)
    # V2 = (D - B)

    # normal.x = V1.y * V2.z - V1.z * V2.y
    # normal.y = V2.x * V1.z - V2.z * V1.x
    # normal.z = V1.x * V2.y - V1.y * V2.x

    normal_A = normal_point(3, i * 60, -3)  # A
    normal_B = normal_point(3, (i + 1) * 60, -3)  # B
    normal_C = normal_point(3, (i + 1) * 60, 3)  # C
    normal_D = normal_point(3, i * 60, 3)  # D

    V1 = [normal_C[0] - normal_A[0], normal_C[1] - normal_A[1], normal_C[2] - normal_A[2]]
    V2 = [normal_D[0] - normal_B[0], normal_D[1] - normal_B[1], normal_D[2] - normal_B[2]]

    normalx = V1[1] * V2[2] - V1[2] * V2[1]
    normaly = V2[0] * V1[2] - V2[2] * V1[0]
    normalz = V1[0] * V2[2] - V1[2] * V2[0]

    normal = [normalx, normaly, normalz]
    glNormal(*normal)
    glVertex3f(*normal_A)
    glVertex3f(*normal_B)
    glVertex3f(*normal_C)
    glVertex3f(*normal_D)


def draw_figure():
    glColor3f(.20, .0, .0)
    # glNormal(0, 0, 1)
    glBegin(
        GL_POLYGON)  # GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON
    for i in range(6):
        draw_degree_point(3, i * 60, 3)
    glEnd()

    for i in range(3):
        # glColor3f(.0, .100, .0)
        glBegin(GL_POLYGON)
        normal_wall(i)
        glEnd()

    # glColor3f(.20, .20, .20)
    glBegin(GL_POLYGON)
    glNormal(0, 0, 1)
    for i in range(6):
        draw_degree_point(3, i * 60, -3)
    glEnd()


