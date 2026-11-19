 # coding=utf-8
import os,sys
import pygame
from pygame.locals import *
from Sprite import *
import Personagem

class GameMenu(object):
    """Menu de escolha de personagens"""
    def __init__(self,jogadores = ["","",[pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,pygame.K_y,pygame.K_u,pygame.K_i],[pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_7,pygame.K_KP8,pygame.K_KP9]]):
        self.inicializa(jogadores)
        
    def inicializa(self,jogadores):
        """Inicializa elementos do menu"""
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        pygame.mixer.Sound(os.path.join('.','Sons',"entradamenu.wav")).play()
        pygame.mixer.music.load(os.path.join('.','Musicas','menu.mp3'))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.font = pygame.font.Font(os.path.join('.','Imagens',"fonte.ttf"), int(self.height*0.08))
        retratos = []
        linha = []
        pos = [self.width*0.2375,self.height*0.45]
        self.postitulo = [self.width*0.32,self.height*0.34]
        self.cor = 120
        self.incrcor = 3
        self.configcontrole = 0
        #define posicoes dos retratos na tela, divididos em paginas
        ytopo = pos[1]
        self.linhasporpagina = 0
        for i in Personagem.listar():
            linha.append(Retrato(i,(pos[0],pos[1])))
            pos[0] = pos[0] + 120
            if (pos[0]+90) >= self.width:
                pos[0] = self.width*0.2375
                retratos.append(linha)
                linha = []
                pos[1] = pos[1] + 160
                #quando a proxima linha nao cabe na tela, ela vai para uma nova pagina
                if (pos[1] + 120) >= self.height:
                    if not self.linhasporpagina: self.linhasporpagina = len(retratos)
                    pos[1] = ytopo

        if len(linha) > 0: retratos.append(linha)
        if not self.linhasporpagina: self.linhasporpagina = len(retratos)
        self.retratos = retratos
        self.numpaginas = (len(retratos) + self.linhasporpagina - 1) // self.linhasporpagina
        self.pagina = 0
        self.fontepagina = pygame.font.Font(os.path.join('.','Imagens',"fonte.ttf"), int(self.height*0.03))
        self.retratos[0][0].seleciona(1)
        self.retratos[0][0].seleciona(2)
        self.selecionadop1 = [0,0]
        self.selecionadop2 = [0,0]
        self.numcolunas = (self.width-50)//120
        self.fundo = Sprite(os.path.join('.','Imagens','menu.png'),(0,0),0,(self.width,self.height))
        self.botoesp1 = jogadores[2]
        self.botoesp2 = jogadores[3]

    #eventos de input
    def input(self,eventos):
        """ Trata eventos de input """
        for event in eventos:
            #Botao de fechar
            if event.type == QUIT:
                return True
            #Eventos de teclado
            elif event.type == KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    return True
                elif (event.key == pygame.K_RETURN):
                    pygame.display.toggle_fullscreen()

                #Controles do P1                    
                elif (event.key == self.botoesp1[3]):
                    if not self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhidop1:
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].deseleciona(1)
                        self.selecionadop1[0] =  (self.selecionadop1[0] + 1) % len(self.retratos[self.selecionadop1[1]])
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].seleciona(1)
                elif (event.key == self.botoesp1[2]):
                    if not self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhidop1:
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].deseleciona(1)
                        self.selecionadop1[0] =  (self.selecionadop1[0] - 1) % len(self.retratos[self.selecionadop1[1]])
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].seleciona(1)
                elif (event.key == self.botoesp1[1]):
                    if not self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhidop1:
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].deseleciona(1)
                        self.selecionadop1[1] =  (self.selecionadop1[1] + 1) % len(self.retratos)
                        if len(self.retratos[self.selecionadop1[1]]) <= self.selecionadop1[0]:
                            self.selecionadop1[0] = len(self.retratos[self.selecionadop1[1]]) - 1
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].seleciona(1)
                elif (event.key == self.botoesp1[0]):
                    if not self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhidop1:
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].deseleciona(1)
                        self.selecionadop1[1] =  (self.selecionadop1[1] - 1) % len(self.retratos)
                        if len(self.retratos[self.selecionadop1[1]]) <= self.selecionadop1[0]:
                            self.selecionadop1[0] = len(self.retratos[self.selecionadop1[1]]) - 1
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].seleciona(1)
                elif (event.key == self.botoesp1[4]):
                    if not self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhidop1:
                        self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhe(1)
                elif (event.key == self.botoesp1[5]):
                    self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].desescolhe(1)

                #Controles do P2                    
                elif (event.key == self.botoesp2[3]):
                    if not self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhidop2:
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].deseleciona(2)
                        self.selecionadop2[0] =  (self.selecionadop2[0] + 1) % len(self.retratos[self.selecionadop2[1]])
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].seleciona(2)
                elif (event.key == self.botoesp2[2]):
                    if not self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhidop2:
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].deseleciona(2)
                        self.selecionadop2[0] =  (self.selecionadop2[0] - 1) % len(self.retratos[self.selecionadop2[1]])
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].seleciona(2)
                elif (event.key == self.botoesp2[1]):
                    if not self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhidop2:
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].deseleciona(2)
                        self.selecionadop2[1] =  (self.selecionadop2[1] + 1) % len(self.retratos)
                        if len(self.retratos[self.selecionadop2[1]]) <= self.selecionadop2[0]:
                            self.selecionadop2[0] = len(self.retratos[self.selecionadop2[1]]) - 1
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].seleciona(2)
                elif (event.key == self.botoesp2[0]):
                    if not self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhidop2:
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].deseleciona(2)
                        self.selecionadop2[1] =  (self.selecionadop2[1] - 1) % len(self.retratos)
                        if len(self.retratos[self.selecionadop2[1]]) <= self.selecionadop2[0]:
                            self.selecionadop2[0] = len(self.retratos[self.selecionadop2[1]]) - 1
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].seleciona(2)
                elif (event.key == self.botoesp2[4]):
                    if not self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhidop2:
                        self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhe(2)
                elif (event.key == self.botoesp2[5]):
                    self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].desescolhe(2)

                elif (event.key == pygame.K_F1) and (self.configcontrole == 0):
                    self.configcontrole=1
                    self.botoesp1 = []
                elif (event.key == pygame.K_F2) and (self.configcontrole == 0):
                    self.configcontrole=2
                    self.botoesp2 = []

        return False
        
    def update(self,dtempo,eventos):
        """Atualiza elementos do menu"""
        self.cor = self.cor + self.incrcor
        if self.cor >= 255:
            self.incrcor = -3
            self.cor = 255
        if self.cor <= 100: self.incrcor = 3
        
        #caso um jogador esteja configurando os controles
        if self.configcontrole == 1:
            for event in eventos:
                if (event.type == KEYDOWN): self.botoesp1.append(event.key)
                if len(self.botoesp1) >= 7:
                    self.botoesp1 = self.botoesp1[:7]
                    self.configcontrole = 0
            return False
        elif self.configcontrole == 2:
            for event in eventos:
                if (event.type == KEYDOWN): self.botoesp2.append(event.key)
                if len(self.botoesp2) >= 7:
                    self.botoesp2 = self.botoesp2[:7]
                    self.configcontrole = 0
            return False
        else:
            self.fundo.update(dtempo)
            for i in self.retratos:
                for n in i:
                    n.update(dtempo)
    
            #Se os 2 jogadores ja escolheram
            if self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].escolhidop1 and self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].escolhidop2:
                return [self.retratos[self.selecionadop1[1]][self.selecionadop1[0]].nome,self.retratos[self.selecionadop2[1]][self.selecionadop2[0]].nome,self.botoesp1,self.botoesp2]
            else:
                antesp1 = self.selecionadop1[:]
                antesp2 = self.selecionadop2[:]
                retorno = self.input(eventos)
                #a pagina mostrada acompanha o ultimo jogador que moveu o cursor
                if self.selecionadop1 != antesp1:
                    self.pagina = self.selecionadop1[1] // self.linhasporpagina
                elif self.selecionadop2 != antesp2:
                    self.pagina = self.selecionadop2[1] // self.linhasporpagina
                return retorno

    def render(self,screen):
        """Renderiza os elementos da tela atual"""
        self.fundo.render(screen,(0,0))
        screen.blit(self.font.render("Faça Sua Matrícula", True, (self.cor,0,0)),(self.postitulo[0],self.postitulo[1]))
        inicio = self.pagina * self.linhasporpagina
        for i in self.retratos[inicio:inicio + self.linhasporpagina]:
            for n in i:
                n.render(screen)

        #indicador de paginas na barra lateral
        if self.numpaginas > 1:
            x = self.width*0.025
            screen.blit(self.fontepagina.render("Página %d/%d" % (self.pagina+1, self.numpaginas), True, (60,60,60)),(x,self.height*0.895))
            screen.blit(self.fontepagina.render("P1: pág. %d" % (self.selecionadop1[1]//self.linhasporpagina+1), True, (200,0,0)),(x,self.height*0.925))
            screen.blit(self.fontepagina.render("P2: pág. %d" % (self.selecionadop2[1]//self.linhasporpagina+1), True, (0,0,200)),(x,self.height*0.955))

        if self.configcontrole:
            superficieescura = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            superficieescura.fill((0,0,0,210))
            screen.blit(superficieescura,(0,0))
            screen.blit(self.font.render("Configurando Controles:", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Configurando Controles:")[0]//2),self.height*0.1))
            screen.blit(self.font.render("Pressione:", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Pressione:")[0]//2),self.height*0.4))
            
            if self.configcontrole == 1:
                screen.blit(self.font.render("Jogador 1", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Jogador 1")[0]//2),self.height*0.2))
                listabotoes = self.botoesp1
            elif self.configcontrole == 2:
                screen.blit(self.font.render("Jogador 2", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Jogador 2")[0]//2),self.height*0.2))
                listabotoes = self.botoesp2

            if len(listabotoes) == 0: screen.blit(self.font.render("Cima", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Cima")[0]//2),self.height*0.5))
            elif len(listabotoes) == 1: screen.blit(self.font.render("Baixo", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Baixo")[0]//2),self.height*0.5))
            elif len(listabotoes) == 2: screen.blit(self.font.render("Esquerda", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Esquerda")[0]//2),self.height*0.5))
            elif len(listabotoes) == 3: screen.blit(self.font.render("Direita", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Direita")[0]//2),self.height*0.5))
            elif len(listabotoes) == 4: screen.blit(self.font.render("Soco", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Soco")[0]//2),self.height*0.5))
            elif len(listabotoes) == 5: screen.blit(self.font.render("Chute", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Chute")[0]//2),self.height*0.5))
            elif len(listabotoes) == 6: screen.blit(self.font.render("Especial", True, (self.cor,0,0)),((self.width//2)-(self.font.size("Especial")[0]//2),self.height*0.5))                
            

    def unload(self,):
        """Descarrega tela"""
        pygame.mixer.music.stop()
        pygame.time.delay(1500)
        pygame.mixer.stop()
        return True

class Retrato(object):
    """ Retrato de personagem na tela de selecao """
    def __init__(self,nome,pos):
        self.sprite = Sprite(Personagem.arquivo(nome,'retrato.png'),(90,120),1.5)
        self.x,self.y = pos
        self.nome = nome
        self.font = pygame.font.Font(os.path.join('.','Imagens',"fonte.ttf"), 20)
        self.selecionadop1 = False
        self.selecionadop2 = False
        self.escolhidop1 = False
        self.escolhidop2 = False
        self.cor = 155
        self.incrcor = 5
        self.somseleciona = pygame.mixer.Sound(os.path.join('.','Sons',"seleciona.wav"))
        self.somescolhejogador = pygame.mixer.Sound(Personagem.arquivo(self.nome,"escolhe.wav"))
        self.somescolhe = pygame.mixer.Sound(os.path.join('.',"Sons","escolhe.wav"))

    def update(self,dtempo):
        """ Atualiza retrato e caixa de selecao """
        self.sprite.update(dtempo)
        self.cor = self.cor + self.incrcor
        if self.cor >= 255:
            self.incrcor = -5
            self.cor = 255
        if self.cor <= 155: self.incrcor = 5

    def render(self,screen):
        """ Renderiza retrato e caixa de selecao """
        self.sprite.render(screen,(self.x,self.y))
        screen.blit(self.font.render(self.nome, True, (155,0,0)),(self.x+45-(self.font.size(self.nome)[0]//2),self.y + 130))
        if (not self.escolhidop1) and (not self.escolhidop2):
            if self.selecionadop1:
                pygame.draw.rect(screen, (self.cor,0,0), pygame.Rect(self.x-5,self.y-5,95,125), 5)
            if self.selecionadop2:
                pygame.draw.rect(screen, (0,0,self.cor), pygame.Rect(self.x-5,self.y-5,95,125), 5)
        elif self.escolhidop1:
            pygame.draw.rect(screen, (255,20,0), pygame.Rect(self.x-5,self.y-5,95,125), 5)
        elif self.escolhidop2:
            pygame.draw.rect(screen, (0,20,255), pygame.Rect(self.x-5,self.y-5,95,125), 5)

    def seleciona(self,player):
        """ define o jogador de determinado numero como seletor do retrato """
        if player == 1: self.selecionadop1 = True
        else: self.selecionadop2 = True

    def deseleciona(self,player):
        """ desmarca o jogador de determinado numero como seletor do retrato """
        if player == 1: self.selecionadop1 = False
        else: self.selecionadop2 = False
        self.somseleciona.play()

    def escolhe(self,player):
        """ define o jogador de determinado numero como seletor do retrato """
        if player == 1: self.escolhidop1 = True
        else: self.escolhidop2 = True
        self.somescolhe.play()
        self.somescolhejogador.play()

    def desescolhe(self,player):
        """ desmarca o jogador de determinado numero como seletor do retrato """
        if player == 1: self.escolhidop1 = False
        else: self.escolhidop2 = False
                

            
