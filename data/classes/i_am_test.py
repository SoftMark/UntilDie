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
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_figure(shape, surface):
	if shape == "Sphere":
		draw_sphere(surface)
	elif shape == "Teapot":
		draw_teapot(surface)
	else:
		glBegin(GL_LINE_LOOP)
		glVertex2f(2,2)
		glVertex2f(-2,2)
		glVertex2f(-2,-2)
		glVertex2f(2,-2)
		glEnd()

def draw_sphere(surface):
	if surface == "Solid":
		glutSolidSphere(2,100,100)
	elif surface == "Wire":
		glutWireSphere(8,100,100)

def draw_teapot(surface):
	if surface == "Solid":
		glutSolidTeapot(3)
	elif surface == "Wire":
		glutWireTeapot(3)

def build_projection():
	glOrtho(-5, 5, -5, 5, -5, 5)

def draw_scene():
	glColor3f(.8,.4,.1)
	draw_figure("Teapot", "Wire")
	glutSwapBuffers()

glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Lab1")

build_projection()
glutDisplayFunc(draw_scene)
glutMainLoop()
'''


x = np.arange(0, 4 * np.pi, 0.01)
sin = np.sin(x)
plt.plot(x,sin)
plt.title('Graphic')
plt.legend(['sin(x)'])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()