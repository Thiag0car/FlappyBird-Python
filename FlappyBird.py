import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png'))) 
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))



pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)
FONTE_GAMEOVER = pygame.font.SysFont('arial', 70)
FONTE_REINICIAR = pygame.font.SysFont('arial', 30)
FONTE_RECORDE = pygame.font.SysFont('arial', 15)

class Passaro:
    IMAGENS_PASSARO_1 = [
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
    ]

    IMAGENS_PASSARO_2 = [
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bobesponja1.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bobesponja2.png'))),
        pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bobesponja1.png')))
    ]

    #animações da rotação
    ROTAÇAO_MAXIMA = 25
    VELOCIDADE_ROTAÇAO = 20
    TEMPO_ANIMAÇAO = 5
    
    def __init__(self, x, y, imgs=IMAGENS_PASSARO_1):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.set_imagens(imgs)

    def set_imagens(self, imgs):
        self.IMGS = imgs
        self.imagem = self.IMGS[0]
    
    def pular(self):
        self.velocidade= -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
    
        #restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento
      
        #angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTAÇAO_MAXIMA:
                self.angulo = self.ROTAÇAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTAÇAO
    
    def desenhar(self, tela):
        # definir qual imagem do pássaro vai ser usado
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMAÇAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMAÇAO*2: 
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMAÇAO*3: 
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMAÇAO*4: 
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem >= self.TEMPO_ANIMAÇAO*4 + 1: 
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # se o pássaro estiver caindo a asa não vai bater
        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMAÇAO*2

        # desenhar imagem
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)
                              
class Cano:
    DISTANCIA = 217
    VELOCIDADE = 5
    
    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True) 
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA
    
    def mover(self):
        self.x -= self.VELOCIDADE

    def desenhar(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask=  pygame.mask.from_surface(self.CANO_TOPO)
        base_mask=  pygame.mask.from_surface(self.CANO_BASE)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False


class Chao:
    VELOCIDADE = 5 
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA    
     
    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1 , self.y))
        tela.blit(self.IMAGEM, (self.x2 , self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos, recorde, game_over_flag):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    # Verifica se o jogo está em andamento ou se está no Game Over
    if not game_over_flag:
        texto_pontos = FONTE_PONTOS.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
        texto_recorde = FONTE_RECORDE.render(f'Recorde: {recorde}', 1, (255, 255, 255))
        tela.blit(texto_pontos, (TELA_LARGURA - 10 - texto_pontos.get_width(), 10))
        tela.blit(texto_recorde, (TELA_LARGURA - 10 - texto_recorde.get_width(), 70))

    if game_over_flag:
        mensagem_gameover = FONTE_GAMEOVER.render("Game Over", 1, (255, 255, 255))
        mensagem_reiniciar = FONTE_REINICIAR.render("Aperte Enter para Recomeçar", 1, (255, 255, 255))

        # Centralizar as mensagens de "Game Over" e "Aperte Enter para Reiniciar"
        pos_x_gameover = TELA_LARGURA // 2 - mensagem_gameover.get_width() // 2
        pos_y_gameover = TELA_ALTURA // 2 - mensagem_gameover.get_height() // 2
        pos_x_reiniciar = TELA_LARGURA // 2 - mensagem_reiniciar.get_width() // 2
        pos_y_reiniciar = TELA_ALTURA // 2 + mensagem_gameover.get_height() + 30

        tela.blit(mensagem_gameover, (pos_x_gameover, pos_y_gameover))
        tela.blit(mensagem_reiniciar, (pos_x_reiniciar, pos_y_reiniciar))

        # Centralizar as mensagens de "Pontuação" e "Recorde" na tela de Game Over
        texto_pontos = FONTE_RECORDE.render(f'Pontuação: {pontos}', 1, (255, 255, 255))
        texto_recorde = FONTE_RECORDE.render(f'Recorde: {recorde}', 1, (255, 255, 255))
        pos_x_pontos = TELA_LARGURA // 2 - texto_pontos.get_width() // 2
        pos_y_pontos = TELA_ALTURA // 2 + mensagem_gameover.get_height() // 2 + 10
        pos_x_recorde = TELA_LARGURA // 2 - texto_recorde.get_width() // 2
        pos_y_recorde = TELA_ALTURA // 2 + mensagem_gameover.get_height() // 2 + texto_pontos.get_height() + 20

        tela.blit(texto_pontos, (pos_x_pontos, pos_y_pontos))
        tela.blit(texto_recorde, (pos_x_recorde, pos_y_recorde))

    chao.desenhar(tela)
    pygame.display.update()


def tela_selecao_passaro(tela):
    opcao = None

    while opcao not in ('1', '2'):
        tela.fill((0, 0, 0))
        texto_escolha = FONTE_PONTOS.render("Escolha o passaro: 1 ou 2", True, (255, 255, 255))
        texto_aperte_tecla = FONTE_RECORDE.render("Aperte a tecla equivalente para começar", True, (255, 255, 255))
        tela.blit(texto_escolha, (TELA_LARGURA // 2 - texto_escolha.get_width() // 2, TELA_ALTURA // 2 - 30))
        tela.blit(texto_aperte_tecla, (TELA_LARGURA // 2 - texto_aperte_tecla.get_width() // 2, TELA_ALTURA // 2 + 30))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    opcao = '1'
                elif evento.key == pygame.K_2:
                    opcao = '2'

    return opcao


def game_over(pontos, recorde):
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Reiniciar o jogo
                    main()

def carregar_recorde():
    if os.path.isfile('recorde.txt'):
        with open('recorde.txt', 'r') as arquivo:
            return int(arquivo.read())
    else:
        return 0

def salvar_recorde(recorde):
    with open('recorde.txt', 'w') as arquivo:
        arquivo.write(str(recorde))



def main():
    pygame.init()
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pygame.display.set_caption('Flappy Bird')

    opcao_passaro = tela_selecao_passaro(tela)

    if opcao_passaro == '1':
        passaros = [Passaro(230, 350, imgs=Passaro.IMAGENS_PASSARO_1)]
    else:
        passaros = [Passaro(230, 350, imgs=Passaro.IMAGENS_PASSARO_2)]

    chao = Chao(730)
    canos = [Cano(700)]
    pontos = 0
    recorde = carregar_recorde()
    relogio = pygame.time.Clock()
    game_over_flag = False

    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if not game_over_flag:
                        for passaro in passaros:
                            passaro.pular()
                if evento.key == pygame.K_RETURN and game_over_flag:
                    game_over_flag = False
                    pontos = 0
                    passaros = [Passaro(230, 350)]
                    canos = [Cano(700)]
        
        if not game_over_flag:
            for passaro in passaros:
                passaro.mover()
            chao.mover()

            adicionar_cano = False
            remover_canos = []
            for cano in canos:
                for i, passaro in enumerate(passaros):
                    if cano.colidir(passaro):
                        game_over_flag = True
                        if pontos > recorde:
                            recorde = pontos
                            salvar_recorde(recorde)
                    if not cano.passou and passaro.x > cano.x:
                        cano.passou = True
                        adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.append(cano)

            if adicionar_cano:
                pontos += 1
                canos.append(Cano(600))
            for cano in remover_canos:
                canos.remove(cano)

            for i, passaro in enumerate(passaros):
                if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                    game_over_flag = True
                    if pontos > recorde:
                        recorde = pontos
                        salvar_recorde(recorde)
        
        desenhar_tela(tela, passaros, canos, chao, pontos, recorde, game_over_flag)

        if game_over_flag:
            game_over(pontos, recorde)

if __name__ == '__main__':
    main()




