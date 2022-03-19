import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.mixer.music.load('lofimario.mp3')
pygame.mixer.music.play(-1)

somcolisao = pygame.mixer.Sound('smw_stomp.wav')
largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)
corfundo = (0,128,128)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')
relogio = pygame.time.Clock()
listacobra = []
comprimento_inicial = 5
morreu = False


def aumenta_cobra(cobramaior):
    for XeY in cobramaior:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, listacobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    listacobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


while True:
    relogio.tick(60)
    tela.fill((corfundo))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra += x_controle
    y_cobra += y_controle
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        somcolisao.play()
        comprimento_inicial += 1

    lista_cabeca = [x_cobra, y_cobra]
    listacobra.append(lista_cabeca)

    if listacobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True)
        mensagem = 'Você perdeu! Pressione [R] para jogar novamente'

        texto = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto.get_rect()

        morreu = True
        while morreu:
            tela.fill((corfundo))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
    if len(listacobra) > comprimento_inicial:
        del listacobra[0]
    aumenta_cobra(listacobra)
    tela.blit(texto, (400, 10))
    pygame.display.update()
