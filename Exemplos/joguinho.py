import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
MAX_SHIPS = 5
MAX_ATTEMPTS = 5  # Número máximo de cliques permitidos

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Estado do jogo
state = "welcome"  # Pode ser "welcome", "game", "victory", ou "defeat"

# Criação da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Batalha Naval")

# Criação do tabuleiro
board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Número de navios no tabuleiro
ship_count = 0

# Número de tentativas na rodada
attempts = 0

# Cliques permitidos
allowed_clicks = MAX_ATTEMPTS

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = WHITE if board[row][col] == 0 else GRAY
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Função para posicionar os navios aleatoriamente
def place_ships():
    global ship_count
    while ship_count < MAX_SHIPS:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if board[row][col] == 0:
            board[row][col] = 1
            ship_count += 1

# Função para converter as coordenadas do mouse para as coordenadas do tabuleiro
def get_clicked_pos(pos):
    col = pos[0] // CELL_SIZE
    row = pos[1] // CELL_SIZE
    return row, col

# Função para processar os cliques do mouse
def process_click(row, col):
    global state, ship_count, attempts, allowed_clicks
    if board[row][col] == 1:
        print("Você acertou um navio!")
        board[row][col] = 2  # Marca o local do navio como atingido
        ship_count -= 1
        if ship_count == 0:
            state = "victory"
    else:
        print("Você errou!")
        attempts += 1
        allowed_clicks -= 1
        if attempts >= 1:  # Agora, a derrota ocorre após um clique incorreto
            state = "defeat"
            
# Função para mostrar a tela de boas-vindas
def show_welcome_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Batalha Naval - Clique para começar", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Função para mostrar a tela de vitória
def show_victory_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Você venceu! Clique para continuar.", True, GREEN)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(text, text_rect)
    pygame.display.flip()
    
# Função para mostrar a tela de derrota
def show_defeat_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Você perdeu! Clique para reiniciar.", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(text, text_rect)
    pygame.display.flip()
    
# Função para reiniciar o jogo
def reset_game():
    global board, state, ship_count, attempts, allowed_clicks
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    ship_count = 0
    attempts = 0
    allowed_clicks = MAX_ATTEMPTS
    place_ships()
    state = "game"

# Função principal do jogo
def main():
    global state
    place_ships()

    show_ships_timer = pygame.time.get_ticks() + 1000  # Timer para controlar a exibição dos navios por 1 segundo
    hide_ships = False  # Flag para indicar se os navios devem ser escondidos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(mouse_pos)

                if state == "welcome":
                    # Transição da tela de boas-vindas para o jogo
                    reset_game()
                    state = "game"
                elif state == "game":
                    # Processamento de cliques durante o jogo
                    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                        process_click(row, col)
                elif state == "victory" or state == "defeat":
                    # Se estiver nas telas de vitória ou derrota, reinicia o jogo ao clicar
                    reset_game()
                    state = "game"

        if state == "welcome":
            show_welcome_screen()
        elif state == "game":
            screen.fill(BLACK)
            # Verifica se é hora de esconder os navios
            if pygame.time.get_ticks() >= show_ships_timer and not hide_ships:
                # Tornar os navios brancos
                for i in range(GRID_SIZE):
                    for j in range(GRID_SIZE):
                        if board[i][j] == 1:
                            board[i][j] = 3  # Usando 3 para representar os navios brancos
                hide_ships = True
            draw_board()
            pygame.display.flip()
        elif state == "victory":
            show_victory_screen()
        elif state == "defeat":
            show_defeat_screen()

if __name__ == "__main__":
    main()