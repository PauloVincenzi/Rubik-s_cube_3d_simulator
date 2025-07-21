from logica_cubo import criar_estado_inicial, rotacionar_camada
from visualizacao import desenhar_estado, atualizar_visualizacao, animar_rotacao, adicionar_marcadores
from vpython import rate, button
from random import choice
import time

def embaralhar(n=50):
    global estado
    for _ in range(n):
        eixo = choice(['x', 'y', 'z'])
        camada_valor = choice([-1, 0, 1])
        sentido = choice(['horario', 'anti-horario'])
        time.sleep(0.03)
        estado = rotacionar_camada(estado, eixo, camada_valor, sentido)
        atualizar_visualizacao(cubos, estado)

def rotacao(info):
    global estado
    if info == "U":
        animar_rotacao(cubos, 'y', 1, 'horario')
        estado = rotacionar_camada(estado, 'y', 1, 'horario')
    elif info == "U'":
        animar_rotacao(cubos, 'y', 1, 'anti-horario')
        estado = rotacionar_camada(estado, 'y', 1, 'anti-horario')
    elif info == "D":
        animar_rotacao(cubos, 'y', -1, 'horario')
        estado = rotacionar_camada(estado, 'y', -1, 'horario')
    elif info == "D'":
        animar_rotacao(cubos, 'y', -1, 'anti-horario')
        estado = rotacionar_camada(estado, 'y', -1, 'anti-horario')
    elif info == "F":
        animar_rotacao(cubos, 'z', 1, 'horario')
        estado = rotacionar_camada(estado, 'z', 1, 'horario')
    elif info == "F'":
        animar_rotacao(cubos, 'z', 1, 'anti-horario')
        estado = rotacionar_camada(estado, 'z', 1, 'anti-horario')
    elif info == "B":
        animar_rotacao(cubos, 'z', -1, 'horario')
        estado = rotacionar_camada(estado, 'z', -1, 'horario')
    elif info == "B'":
        animar_rotacao(cubos, 'z', -1, 'anti-horario')
        estado = rotacionar_camada(estado, 'z', -1, 'anti-horario')
    elif info == "L":
        animar_rotacao(cubos, 'x', -1, 'horario')
        estado = rotacionar_camada(estado, 'x', -1, 'horario')
    elif info == "L'":
        animar_rotacao(cubos, 'x', -1, 'anti-horario')
        estado = rotacionar_camada(estado, 'x', -1, 'anti-horario')
    elif info == "R":
        animar_rotacao(cubos, 'x', 1, 'horario')
        estado = rotacionar_camada(estado, 'x', 1, 'horario')
    elif info == "R'":
        animar_rotacao(cubos, 'x', 1, 'anti-horario')
        estado = rotacionar_camada(estado, 'x', 1, 'anti-horario')
    rate(10)
    atualizar_visualizacao(cubos, estado)

button(text="U", bind=lambda: rotacao("U"))
button(text="U'", bind=lambda: rotacao("U'"))
button(text="D", bind=lambda: rotacao("D"))
button(text="D'", bind=lambda: rotacao("D'"))
button(text="F", bind=lambda: rotacao("F"))
button(text="F'", bind=lambda: rotacao("F'"))
button(text="B", bind=lambda: rotacao("B"))
button(text="B'", bind=lambda: rotacao("B'"))
button(text="L", bind=lambda: rotacao("L"))
button(text="L'", bind=lambda: rotacao("L'"))
button(text="R", bind=lambda: rotacao("R"))
button(text="R'", bind=lambda: rotacao("R'"))

button(text="EMBARALHAR", bind=lambda: embaralhar())

estado = criar_estado_inicial()
cubos = desenhar_estado(estado)
adicionar_marcadores()

while True:
    pass
