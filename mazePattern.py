from turtle import *
import random

setup(500, 500)

# Triângulo
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)


def tiling(s, l, mode="staight", x=0, y=0):
    # O nível final da recursão foi atingido
    if l == 0:
        if mode == "straight":
            if random.random() < 0.5:
                # Desenhar uma linha vertical
                penup()
                goto(x, y - s)
                pendown()
                goto(x, y + s)

            else:
                # Desenhar uma linha horizontal
                penup()
                goto(x - s, y)
                pendown()
                goto(x + s, y)

        elif mode == "diagonal":
            if random.random() < 0.5:
                # Desenhar uma linha diagonal da esquerda para a direita
                penup()
                goto(x - s, y + s)
                pendown()
                goto(x + s, y - s)

            else:
                # Desenhar uma linha direita da esquerda para a diagonal
                penup()
                goto(x - s, y - s)
                pendown()
                goto(x + s, y + s)

        else:
            raise ValueError("Invalid Mode. It can be either Straight or Diagonal")
    # Dividir a tela e partir para o próximo nível de recursão
    else:
        s /= 2
        l -= 1
        tiling(s, l, mode, x - s, y + s)
        tiling(s, l, mode, x + s, y + s)
        tiling(s, l, mode, x - s, y - s)
        tiling(s, l, mode, x + s, y - s)


hideturtle()
tracer(False)
width(3)
tiling(220, 5, "diagonal")
tracer(True)
exitonclick()
