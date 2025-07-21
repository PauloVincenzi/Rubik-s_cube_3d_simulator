from logica_cubo import rotacionar_camada
from vpython import box, vector, color, scene
from vpython import rate, radians, label

CORES = {
    'R': color.red,
    'G': color.green,
    'B': color.blue,
    'Y': color.yellow,
    'W': color.white,
    'O': color.orange,
}

DESLOCAMENTOS = {
    'x+': vector(0.51, 0, 0),
    'x-': vector(-0.51, 0, 0),
    'y+': vector(0, 0.51, 0),
    'y-': vector(0, -0.51, 0),
    'z+': vector(0, 0, 0.51),
    'z-': vector(0, 0, -0.51),
}

def apagar_cubos(cubos):
    for dados in cubos.values():
        dados['cubo'].visible = False
        for face in dados['faces']:
            face.visible = False

def animar_rotacao(cubos, eixo, camada_valor, sentido):
    ANGULO_TOTAL = radians(90)
    PASSOS = 30
    delta = ANGULO_TOTAL / PASSOS
    angulo_por_passo = delta if sentido == 'horario' else -delta

    # Eixo de rotação
    eixo_vpython = vector(1, 0, 0) if eixo == 'x' else \
                   vector(0, 1, 0) if eixo == 'y' else \
                   vector(0, 0, 1)

    # Seleciona blocos da camada
    blocos = []
    for pos, dados in cubos.items():
        if (eixo == 'x' and pos[0] == camada_valor) or \
           (eixo == 'y' and pos[1] == camada_valor) or \
           (eixo == 'z' and pos[2] == camada_valor):
            blocos.append(dados)

    # Centro da rotação
    centro = vector(0, 0, 0)

    # Anima a rotação
    for _ in range(PASSOS):
        rate(60)
        for bloco in blocos:
            bloco['cubo'].rotate(angle=angulo_por_passo, axis=eixo_vpython, origin=centro)
            for face in bloco['faces']:
                face.rotate(angle=angulo_por_passo, axis=eixo_vpython, origin=centro)

def desenhar_estado(estado):
    cubos = {}
    for pos, faces in estado.items():
        x, y, z = pos
        cubo = box(pos=vector(x, y, z), size=vector(0.98, 0.98, 0.98), color=color.black)
        cubos[pos] = {'cubo': cubo, 'faces': []}

        # Adiciona faces coloridas
        for face, cor in faces.items():
            desloc = DESLOCAMENTOS[face]
            face_colorida = box(pos=vector(x, y, z) + desloc,
                                size=vector(0.05 if 'x' in face else 0.9,
                                            0.05 if 'y' in face else 0.9,
                                            0.05 if 'z' in face else 0.9),
                                color=CORES[cor])
            cubos[pos]['faces'].append(face_colorida)
    return cubos

# Atualiza visualização após rotação
def atualizar_visualizacao(cubos, novo_estado):
    novos_cubos = {}

    for nova_pos, faces in novo_estado.items():
        # Pega o cubo visual antigo que estava na posição anterior
        # Isto funciona pois o dicionário cubos usa como chave a posição atual
        if nova_pos in cubos:
            bloco = cubos[nova_pos]
        else:
            # O cubo mudou de posição, então precisamos encontrar onde ele estava antes
            # Como alternativa segura, vamos iterar para encontrar
            for pos_antiga, dados in cubos.items():
                if 'migrado' not in dados:
                    bloco = dados
                    dados['migrado'] = True
                    break

        # Move cubo para nova posição
        bloco['cubo'].pos = vector(*nova_pos)

        # Remove faces antigas
        for face in bloco['faces']:
            face.visible = False

        # Adiciona novas faces
        bloco['faces'] = []
        for face, cor in faces.items():
            desloc = DESLOCAMENTOS[face]
            face_colorida = box(pos=vector(*nova_pos) + desloc,
                                size=vector(0.05 if 'x' in face else 0.9,
                                            0.05 if 'y' in face else 0.9,
                                            0.05 if 'z' in face else 0.9),
                                color=CORES[cor])
            bloco['faces'].append(face_colorida)

        novos_cubos[nova_pos] = bloco

    # Limpa marcação temporária
    for dados in cubos.values():
        dados.pop('migrado', None)

    cubos.clear()
    cubos.update(novos_cubos)

def adicionar_marcadores():
    marcadores = {
        'F': vector(0, 0, 7),
        'B': vector(0, 0, -7),
        'U': vector(0, 7, 0),
        'D': vector(0, -7, 0),
        'L': vector(-7, 0, 0),
        'R': vector(7, 0, 0),
    }
    for letra, pos in marcadores.items():
        label(pos=pos, text=letra, height=20, box=False, opacity=0, color=color.white)
