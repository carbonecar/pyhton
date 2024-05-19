import pygame,sys

pygame.init()


screen_with=1200
screen_height=600


screen= pygame.display.set_mode((screen_with,screen_height))
pygame.display.set_caption("Pong")

clock=pygame.time.Clock()

# game loop
# display sourface
# surface is a rectangular object on which we can draw
# rectange is used for collision detection

ball = pygame.Rect(0,0,30,30) # this is the ball on the top left corner
ball.center=(screen_with/2,screen_height/2)

cpu=pygame.Rect(0,0,20,100)
cpu.centery=screen_height/2

player=pygame.Rect(0,0,20,100)
player.midright=(screen_with,screen_height/2)


ball_speed_x=6
ball_speed_y=6
player_speed=0
cpu_speed=7
cpu_points,player_points=0,0

score_font=pygame.font.Font(None,100)

def point_won(winner):
    global cpu_points,player_points

    if winner=="cpu":
        cpu_points+=1
    if winner=="player":
        player_points+=1
    ball.center=(screen_with/2,screen_height/2)
    
    

def animateBall():
    global ball_speed_x, ball_speed_y
    
    if ball.bottom >= screen_height or ball.top <=0:
        ball_speed_y *= -1
      
    
    if ball.left <=0: 
        point_won("player")
    if ball.right >= screen_with:
       point_won("cpu")

     #move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # if collides with another player o r cpy change the direction
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1
    
    
def animatePlayer():
    player.y += player_speed    
           
    if player.top <=0:
        player.top=0
    if player.bottom >= screen_height:
        player.bottom=screen_height

def animtateCpu():
    global cpu_speed
    cpu.y += cpu_speed
    if ball.centery <= cpu.centery: 
        cpu_speed = -6
    if ball.centery >=cpu.centery:
        cpu_speed = 6
        
    if cpu.top <=0:
        cpu.top=0
    if cpu.bottom >= screen_height:
        cpu.bottom=screen_height

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
               player_speed = 6
            if event.key==pygame.K_UP:
                player_speed = -6
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player_speed = 0
            if event.key==pygame.K_UP:
                player_speed = 0    
       
    animateBall()
    animatePlayer()
    animtateCpu()
    
    
    #Draw
    screen.fill('black') #hack to clear the screen insted of clear some part of it. 
    
    
    cpu_score_surfact=score_font.render(str(cpu_points),True,'white')
    screen.blit(cpu_score_surfact,(screen_with/4,screen_height/4))
    
    player_score_surfact=score_font.render(str(player_points),True,'white')
    screen.blit(player_score_surfact,(screen_with/1.5,screen_height/4))
    
    pygame.draw.aaline(screen,'white',(screen_with/2,0),(screen_with/2,screen_height))        
    pygame.draw.ellipse(screen,'white',ball)
    pygame.draw.rect(screen,'white',cpu)
    pygame.draw.rect(screen,'white',player)
    
    pygame.display.update()
    clock.tick(60) # how fast the game will run. 60 fps
    
    
    