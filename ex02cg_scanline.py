import pygame, sys

# Macros para cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Preencher um polígono usando o algoritmo Scanline
def scanline(superficie, pontos, cor):
    
    # Encontre os limites superior e inferior do polígono
    y_min = min(ponto[1] for ponto in pontos)
    y_max = max(ponto[1] for ponto in pontos)

    tabela_todas_arestas = [[] for _ in range(y_max - y_min + 1)]

    for i in range(len(pontos)):
        # Ponto inicial e final da aresta
        ponto_inicio = pontos[i]
        ponto_fim = pontos[(i + 1) % len(pontos)]

        # Pular as arestas horizontais
        if ponto_inicio[1] == ponto_fim[1]:
            continue

        # Determinar os y mínimo e máximo da aresta
        y_comeco = min(ponto_inicio[1], ponto_fim[1])
        y_fim = max(ponto_inicio[1], ponto_fim[1])

        # Calcular Delta X/Delta Y
        deltaX_deltaY = (ponto_fim[0] - ponto_inicio[0]) / (ponto_fim[1] - ponto_inicio[1])

        tabela_todas_arestas[y_comeco - y_min].append((y_fim, ponto_inicio[0], deltaX_deltaY))

    arestas_ativas = []

    # Processar linha por linha
    for scanline, edges in enumerate(tabela_todas_arestas):
        
        # Adicionar novas arestas à lista de arestas ativas
        arestas_ativas.extend(edges)

        # Remover aresas cujo y máximo é menor que o y mínimo da atual scanline
        arestas_ativas = [edge for edge in arestas_ativas if edge[0] > scanline]

        # Ordenar bordas ativas pelo valor de x
        arestas_ativas.sort(key=lambda x: x[1])

        # Preencher os pixels 
        for i in range(0, len(arestas_ativas), 2):
            x_start = int(arestas_ativas[i][1])
            x_end = int(arestas_ativas[i + 1][1])

            pygame.draw.line(superficie, cor, (x_start, scanline + y_min), (x_end, scanline + y_min))

            # Verificar se há pelo menos três elementos em active_edges[i] antes de acessar active_edges[i][2]
            if len(arestas_ativas[i]) >= 3:
                arestas_ativas[i] = (arestas_ativas[i][0], arestas_ativas[i][1] + arestas_ativas[i][2])
            if len(arestas_ativas[i + 1]) >= 3:
                arestas_ativas[i + 1] = (arestas_ativas[i + 1][0], arestas_ativas[i + 1][1] + arestas_ativas[i + 1][2])

# Inicialização do Pygame
pygame.init()

width, height = 800, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algoritmo Scanline")

# Loop principal do Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tela branca
    window.fill(WHITE)

    quadrado = [(100, 100), (200, 100), (200, 200), (100, 200)]
    scanline(window, quadrado, BLACK)

    triangulo = [(250, 250), (350, 250), (300, 150)]
    scanline(window, triangulo, GREEN)

    pygame.display.flip()

pygame.quit()
sys.exit()
