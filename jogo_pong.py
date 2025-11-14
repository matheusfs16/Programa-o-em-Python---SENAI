import pygame



pygame.init()

# Display
tela  = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pong")
font = pygame.font.SysFont(None, 50)

# Cores
branco = (255,255,255)
preto = (0,0,0)

# Cordenadas Bola
xbola, ybola = 250, 250
bola_altura = 10
bola = (tela, 'white',(xbola,ybola), 30, 0)

# Velocidade Bola
xvel, yvel = 0.05, 0.04

# Pontuação Jogadores
player1 = 0
player2 = 0

# Variaveis Raquete
raqx1, raqy1= 50,225
raqx2, raqy2= 450,225
altura = 100
comprimento = 20
velRaq = 0.6

# Movimento Raquete
# def MovimentoRaquete():
#     key = pygame.key.get_pressed()
#     if pygame.key.get_pressed() == pygame.K_UP:
#         raqy1 += 10
#     if pygame.key.get_pressed() == pygame.K_DOWN:
#        raqy1 -= 10 

def desenhar():
    tela.fill('grey')
    
    pygame.draw.circle(tela, branco, (xbola,ybola),bola_altura,0)
    pygame.draw.rect(tela, branco, (raqx1,raqy1,comprimento,altura))
    pygame.draw.rect(tela, branco, (raqx2,raqy2,comprimento,altura))
    placar = font.render(f'{player1}   x   {player2}',True,preto)
    tela.blit(placar,(195,20))

    
    pygame.display.flip()




run = True
while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run  = False
    
    
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and raqy1 > 0:
        raqy1 -= velRaq
    if key[pygame.K_s] and raqy1 < 500 - altura:
       raqy1 += velRaq 



    if key[pygame.K_UP] and raqy2 > 0:
        raqy2 -= velRaq
    if key[pygame.K_DOWN] and raqy2 < 500 - altura:
       raqy2 += velRaq 
    
    xbola += xvel
    ybola += yvel

    if ybola <= 0 or ybola >=500 - bola_altura:
        yvel = -yvel

    if ( raqx1 < xbola < raqx1 + comprimento) and (raqy1 < ybola < raqy1 + comprimento):
        xbola = -xbola

    if ( raqx2 < xbola < raqx2 + comprimento) and (raqy2 < ybola < raqy2 + comprimento):
        xbola = -xbola

    if xbola <= 0:
        player2 += 1
        xbola = 250
    if xbola >= 500:
        player1 += 1
        xbola = 250
    
    
    desenhar()
    pygame.display.update
pygame.quit() 

