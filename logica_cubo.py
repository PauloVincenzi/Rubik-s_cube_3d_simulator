from copy import deepcopy

# Define as cores iniciais de cada face do cubo
FACES = {
    'x+': 'B',  # Direita - Blue
    'x-': 'G',  # Esquerda - Green
    'y+': 'Y',  # Cima - Yellow
    'y-': 'W',  # Baixo - White
    'z+': 'R',  # Frente - Red
    'z-': 'O',  # Trás - Orange
}

# Mapeamentos de direção para vetor e vice-versa
direcao_para_vetor = {
    'x+': (1, 0, 0),
    'x-': (-1, 0, 0),
    'y+': (0, 1, 0),
    'y-': (0, -1, 0),
    'z+': (0, 0, 1),
    'z-': (0, 0, -1)
}
vetor_para_direcao = {v: k for k, v in direcao_para_vetor.items()}

def criar_estado_inicial():
    estado = {}
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                if x == y == z == 0:
                    continue
                faces = {}
                if x == 1: faces['x+'] = FACES['x+']
                if x == -1: faces['x-'] = FACES['x-']
                if y == 1: faces['y+'] = FACES['y+']
                if y == -1: faces['y-'] = FACES['y-']
                if z == 1: faces['z+'] = FACES['z+']
                if z == -1: faces['z-'] = FACES['z-']
                estado[(x, y, z)] = faces
    return estado

# Rotaciona posição de um bloco no espaço 3D
def rotacionar_coordenada(pos, eixo, sentido):
    x, y, z = pos
    if eixo == 'x':
        return (x, -z, y) if sentido == 'horario' else (x, z, -y)
    elif eixo == 'y':
        return (z, y, -x) if sentido == 'horario' else (-z, y, x)
    elif eixo == 'z':
        return (-y, x, z) if sentido == 'horario' else (y, -x, z)

# Rotaciona um vetor de direção no espaço 3D
def rotacionar_vetor(v, eixo, sentido):
    x, y, z = v
    if eixo == 'x':
        return (x, -z, y) if sentido == 'horario' else (x, z, -y)
    elif eixo == 'y':
        return (z, y, -x) if sentido == 'horario' else (-z, y, x)
    elif eixo == 'z':
        return (-y, x, z) if sentido == 'horario' else (y, -x, z)

# Rotaciona a direção de uma face
def rotacionar_direcao(direcao, eixo, sentido):
    if direcao not in direcao_para_vetor:
        return direcao  # ignorar direções não padrão
    v = direcao_para_vetor[direcao]
    v_rot = rotacionar_vetor(v, eixo, sentido)
    return vetor_para_direcao[v_rot]

# Rotaciona todas as faces de um bloco
def rotacionar_faces(faces, eixo, sentido):
    novas = {}
    for direcao, cor in faces.items():
        nova_direcao = rotacionar_direcao(direcao, eixo, sentido)
        novas[nova_direcao] = cor
    return novas

# Rotaciona uma camada do cubo, atualizando posições e orientações das faces
def rotacionar_camada(estado, eixo, camada_valor, sentido):
    novos = {}

    for pos, faces in estado.items():
        x, y, z = pos
        if (eixo == 'x' and x == camada_valor) or \
           (eixo == 'y' and y == camada_valor) or \
           (eixo == 'z' and z == camada_valor):
            nova_pos = rotacionar_coordenada(pos, eixo, sentido)
            nova_faces = rotacionar_faces(faces, eixo, sentido)
            novos[nova_pos] = nova_faces
        else:
            novos[pos] = deepcopy(faces)

    return novos
