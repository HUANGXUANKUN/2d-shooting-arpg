import pygame, os
pygame.init()

winSize = (640,480)
win = pygame.display.set_mode(winSize)
pygame.display.set_caption('Game of Thrones: Into the New World')

black = pygame.image.load(os.path.join("screenshot/abc", "lalaland.png"))

bgMode = pygame.image.load('modeChoose.png')
bg1 = pygame.image.load('bg1.png')
bg2 = pygame.image.load('bg2.png')
bg3 = pygame.image.load('bg3.png')
bg1Lost = pygame.image.load('bg1_Lost.png')
bg2Lost = pygame.image.load('bg2_Lost.png')
bg3Lost = pygame.image.load('bg3_Lost.png')
bgWin = pygame.image.load('Win.png')
bgWinHard = pygame.image.load('WinHard.png')
bgWisdomWinPath = pygame.image.load('WisdomWinPath.png')
bgWisdomWin = pygame.image.load('WisdomWin.png')
bgWisdomWinPathHard = pygame.image.load('WisdomWinPathHard.png')
bgWisdomWinHard = pygame.image.load('WisdomWinHard.png')
bgPerfectWinPath = pygame.image.load('PerfectWinPath.png')
bgPerfectWin = pygame.image.load('PerfectWin.png')
bgPerfectWinPathHard = pygame.image.load('PerfectWinPathHard.png')
bgPerfectWinHard = pygame.image.load('PerfectWinHard.png')
bgPeaceWinPath = pygame.image.load('PeaceWinPath.png')
bgPeaceWin = pygame.image.load('PeaceWin.png')

heartImage = pygame.image.load('heart.png')

playerWalkLeft = [pygame.image.load('L01.png'), pygame.image.load('L02.png'), pygame.image.load('L03.png'), pygame.image.load('L04.png'), pygame.image.load('L05.png'), pygame.image.load('L06.png'), pygame.image.load('L07.png'), pygame.image.load('L08.png'), pygame.image.load('L09.png')]
playerWalkRight = [pygame.image.load('R01.png'), pygame.image.load('R02.png'), pygame.image.load('R03.png'), pygame.image.load('R04.png'), pygame.image.load('R05.png'), pygame.image.load('R06.png'), pygame.image.load('R07.png'), pygame.image.load('R08.png'), pygame.image.load('R09.png')]
globinWalkLeft = [pygame.image.load('globinL01.png'), pygame.image.load('globinL02.png'), pygame.image.load('globinL03.png'), pygame.image.load('globinL04.png'), pygame.image.load('globinL05.png'), pygame.image.load('globinL06.png'), pygame.image.load('globinL07.png'), pygame.image.load('globinL08.png'), pygame.image.load('globinL09.png')]
globinWalkRight = [pygame.image.load('globinR01.png'), pygame.image.load('globinR02.png'), pygame.image.load('globinR03.png'), pygame.image.load('globinR04.png'), pygame.image.load('globinR05.png'), pygame.image.load('globinR06.png'), pygame.image.load('globinR07.png'), pygame.image.load('globinR08.png'), pygame.image.load('globinR09.png')]
ghostFaceLeft = [pygame.image.load('ghostL1.png'), pygame.image.load('ghostL2.png'), pygame.image.load('ghostL3.png'), pygame.image.load('ghostL4.png'), pygame.image.load('ghostL5.png'), pygame.image.load('ghostL6.png'), pygame.image.load('ghostL7.png'), pygame.image.load('ghostL8.png')]
ghostFaceRight = [pygame.image.load('ghostR1.png'), pygame.image.load('ghostR2.png'), pygame.image.load('ghostR3.png'), pygame.image.load('ghostR4.png'), pygame.image.load('ghostR5.png'), pygame.image.load('ghostR6.png'), pygame.image.load('ghostR7.png'), pygame.image.load('ghostR8.png')]
monsterFaceLeft = [pygame.image.load('monsterL1.png'), pygame.image.load('monsterL2.png'), pygame.image.load('monsterL3.png'), pygame.image.load('monsterL4.png'), pygame.image.load('monsterL5.png'), pygame.image.load('monsterL6.png'), pygame.image.load('monsterL7.png'), pygame.image.load('monsterL8.png')]
monsterTurning = [pygame.image.load('monsterTurn1.png'), pygame.image.load('monsterTurn2.png'), pygame.image.load('monsterTurn3.png'), pygame.image.load('monsterTurn4.png'), pygame.image.load('monsterTurn5.png'), pygame.image.load('monsterTurn6.png'), pygame.image.load('monsterTurn7.png'), pygame.image.load('monsterTurn8.png')]
bossAWalkLeft =  [pygame.image.load('BossAL01.png'), pygame.image.load('BossAL02.png'), pygame.image.load('BossAL03.png'), pygame.image.load('BossAL04.png'), pygame.image.load('BossAL05.png'), pygame.image.load('BossAL06.png'), pygame.image.load('BossAL07.png'), pygame.image.load('BossAL08.png')]
bossAWalkRight = [pygame.image.load('BossAR01.png'), pygame.image.load('BossAR02.png'), pygame.image.load('BossAR03.png'), pygame.image.load('BossAR04.png'), pygame.image.load('BossAR05.png'), pygame.image.load('BossAR06.png'), pygame.image.load('BossAR07.png'), pygame.image.load('BossAR08.png')]
bossBWalkLeft =  [pygame.image.load('BossBL01.png'), pygame.image.load('BossBL02.png'), pygame.image.load('BossBL03.png'), pygame.image.load('BossBL04.png'), pygame.image.load('BossBL05.png'), pygame.image.load('BossBL06.png'), pygame.image.load('BossBL07.png'), pygame.image.load('BossBL08.png')]
bossBWalkRight = [pygame.image.load('BossBR01.png'), pygame.image.load('BossBR02.png'), pygame.image.load('BossBR03.png'), pygame.image.load('BossBR04.png'), pygame.image.load('BossBR05.png'), pygame.image.load('BossBR06.png'), pygame.image.load('BossBR07.png'), pygame.image.load('BossBR08.png')]
bulletA = pygame.image.load('BulletA.png')
bulletB = pygame.image.load('BulletB.png')

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
font1 = pygame.font.SysFont('comicsans',32,True,True)




class mainPlayer(object):
    def __init__(self, x, y, width, height, vel, lifeLeft, walkLeft,walkRight,bulletImage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.standing = True
        self.jumpPow = 10
        self.isJumping = False
        self.left = False
        self.right = False
        self.facing = 1
        self.collision = False
        self.walkCount = 0
        self.hitbox = (round(self.x + self.width * 0.02), round(self.y + self.width * 0.02), round(self.width * 0.96), round(self.height*0.96))
        self.bullets = []
        self.lifeLeft = lifeLeft
        self.fullHealth = lifeLeft
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.shootLoop = 0
        self.bulletImage = bulletImage
        self.rebornLoc = (x,y)

    def keysPressed(self,isLeftPressed,isRightPressed,isUpPressed,isSpacePressed):
        if isLeftPressed and self.x >= self.vel:
            self.standing = False
            self.left = True
            self.right = False
            self.x -= self.vel
            self.facing = -1

        elif isRightPressed and self.x < winSize[0]:
            self.standing = False
            self.left = False
            self.right = True
            self.x += self.vel
            self.facing = 1 
                
        else:
            self.standing = True
            self.walkCount = 0

        '''Jumping activation'''
        if not self.isJumping:
            if isUpPressed :
                self.isJumping = True
                self.walkCount = 0

        else:
            if self.jumpPow >= -10:
                neg = 1
                if self.jumpPow < 0:
                    neg = -1
                    
                self.y -= (self.jumpPow ** 2) * 0.5 * neg 
                self.jumpPow -= 1
            
            else:
                self.isJumping = False
                self.jumpPow = 10

        '''Shooting activated'''
        if self.shootLoop >= 1 and self.shootLoop <= 8:
            self.shootLoop += 1
        else:
            self.shootLoop = 0
    
        if isSpacePressed and self.shootLoop == 0 and self.x >= 100:
            bulletSound.play()
            self.bullets.append(projectile(round(self.x + self.width // 2),round(self.y + self.height//2),5,8 * self.facing, self.bulletImage))
            self.shootLoop = 1

        for bullet in self.bullets:
            if not(bullet.x <= winSize[0] - 8 and bullet.x >= 8):
                self.bullets.pop(self.bullets.index(bullet))        
                           
    def draw(self,win):

        if self.lifeLeft >= 1:
            keys = pygame.key.get_pressed()
            self.keysPressed(keys[pygame.K_LEFT],keys[pygame.K_RIGHT],keys[pygame.K_UP],keys[pygame.K_SPACE])
            for bullet in self.bullets:
                bullet.draw(win)
            if self.collision == True:
                self.lifeLeft -= 1
                self.isJumping = False
                self.jumpPow = 10
                self.x = self.rebornLoc[0]
                self.y = self.rebornLoc[1]
                self.walkCount = 0
                self.Right = True
                i = 0
                while i < 60:
                    pygame.time.delay(10)
                    i += 1
    
                self.collision = False
                
            if self.walkCount >= len(self.walkLeft) * 3:
                self.walkCount = 0

            if self.standing:
                if self.left:
                    win.blit(self.walkLeft[0],(self.x,self.y))
                else:
                    win.blit(self.walkRight[0],(self.x,self.y))
            else:
                if self.left:
                    win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1           
                else:
                    win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                    self.walkCount += 1
            

            self.hitbox = (round(self.x + self.width * 0.02), round(self.y + self.width * 0.02), round(self.width * 0.96), round(self.height * 0.96))
##            pygame.draw.rect(win,(255,0,0),self.hitbox,2)


class projectile(object):
    def __init__(self,x,y,radius,vel,bulletImage):
        self.x = x 
        self.y = y 
        self.radius = radius
        self.vel = vel
        self.bulletImage = bulletImage
        
    def draw(self,win):
        self.x += self.vel
        win.blit(self.bulletImage,(self.x - self.radius, self.y - self.radius))         


class enemy1(object):
    def __init__(self,x,y,width,height,leftEnd,rightEnd,facing,vel,health,walkLeft,walkRight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.leftEnd = leftEnd
        self.rightEnd = rightEnd
        self.walkCount = 0
        self.vel = vel
        '''facing = 1 or -1, determines the walking direction of the object'''
        self.facing = facing
        self.hitbox = (round(self.x + self.width * 0.1), round(self.y + self.width * 0.1), round(self.width * 0.8), round(self.height * 0.8))
        self.health = health
        self.fullHealth = health
        self.isDefeated = False
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        

    def move(self):
        if self.x + self.width + self.vel >= self.rightEnd:
            self.facing = -1
            self.walkCount = 0
            
        elif self.x - self.vel <= self.leftEnd:
            self.facing = 1
            self.walkCount = 0

        self.x += self.vel * self.facing
        self.walkCount +=1
    
    def hit(self):
        if self.health >= 1 and player.lifeLeft >= 1:
            for bullet in player.bullets:
                '''When the edge of the bullet is perfectly within the hitbox of the enemy ''' 
                
                if bullet.y - bullet.radius < self.hitbox[1] + self.hitbox[3] and bullet.y + bullet.radius > self.hitbox[1]:
                    if bullet.x + bullet.radius > self.hitbox[0] and bullet.x - bullet.radius < self.hitbox [0] + self.hitbox[2]:
                        hitSound.play()
                        player.bullets.pop(player.bullets.index(bullet))
                        self.health -= 1
                                                    

    def ifCollide(self):
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                player.collision = True

        
    def draw(self,win):

        if self.health >= 1:
            self.ifCollide()
            self.move()
            self.hit()
                              
            if self.walkCount >= len(self.walkLeft) * 3:
                self.walkCount = 0
                
            if self.facing == 1:
                win.blit(self.walkRight[self.walkCount //3],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3],(self.x,self.y))
                self.walkCount += 1


            self.hitbox =(round(self.x + self.width * 0.1), round(self.y + self.width * 0.1), round(self.width * 0.8), round(self.height * 0.8))
            pygame.draw.rect(win,(250,0,0),(self.hitbox[0] - 10,self.hitbox[1]-10,self.hitbox[2] + 20,8)) 
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0] - 10,self.hitbox[1]-10,round(self.health / self.fullHealth * (self.hitbox[2]+ 20)) ,8))    
##            pygame.draw.rect(win,(255,0,0),(self.hitbox),2)

class enemy2(object):
        def __init__(self,x,y,width,height,topEnd,bottomEnd,facing,vel,health,walkLeft,walkRight):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.topEnd = topEnd
            self.bottomEnd = bottomEnd
            self.walkCount = 0
            self.vel = vel
            '''facing = 1 or -1, determines the walking direction of the object'''
            self.facing = facing
            self.hitbox = (round(self.x + self.width * 0.1), round(self.y + self.width * 0.1), round(self.width * 0.8), round(self.height * 0.8))
            self.health = health
            self.isDefeated = False
            self.walkUp = walkLeft
            self.walkDown = walkRight

        def move(self):
            if self.y - self.vel <= self.topEnd:
                self.facing = 1
                self.walkCount = 0
                
            elif self.y + self.height + self.vel >= self.bottomEnd:
                self.facing = -1
                self.walkCount = 0

            self.y += self.vel * self.facing
            self.walkCount +=1
        
        def hit(self):
            if self.health >= 1 and player.lifeLeft >= 1:
                for bullet in player.bullets:
                    '''When the edge of the bullet is perfectly within the hitbox of the enemy '''                  
                    if bullet.y - bullet.radius < self.hitbox[1] + self.hitbox[3] and bullet.y + bullet.radius > self.hitbox[1]:
                        if bullet.x + bullet.radius > self.hitbox[0] and bullet.x - bullet.radius < self.hitbox [0] + self.hitbox[2]:
                            hitSound.play()
                            player.bullets.pop(player.bullets.index(bullet))
                                                                                   

        def ifCollide(self):
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
                    player.collision = True

            
        def draw(self,win):
            if self.health >= 1:
                self.ifCollide()
                self.move()
                self.hit()
                                  
                if self.walkCount >= len(self.walkUp) * 3:
                    self.walkCount = 0
                    
                if self.facing == 1:
                    win.blit(self.walkDown[self.walkCount //3],(self.x,self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkUp[self.walkCount //3],(self.x,self.y))
                    self.walkCount += 1
  
                self.hitbox = (round(self.x + self.width * 0.1), round(self.y + self.width * 0.1), round(self.width * 0.8), round(self.height * 0.8))
##                pygame.draw.rect(win,(255,0,0),(self.hitbox),2)
        

class boss1(object):
    
    def __init__(self,x,y,width,height,facing,health,walkLeft,walkRight,bulletVel,bulletImage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        '''facing = 1 or -1, determines the facing direction of the object'''
        self.facing = facing
        self.hitbox =(round(self.x + self.width * 0.05), round(self.y + self.width * 0.05), round(self.width * 0.9), round(self.height * 0.9))
        self.health = health
        self.fullHealth = health
        self.bullets = []
        self.isDefeated = False
        self.shootLoop = 0
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.bulletVel = bulletVel
        self.bulletImage = bulletImage
        
    def ifShot(self):
        for bullet in player.bullets:
            '''When the edge of the bullet is perfectly within the hitbox of the enemy '''                 
            if bullet.y - bullet.radius < self.hitbox[1] + self.hitbox[3] and bullet.y + bullet.radius > self.hitbox[1]:
                if bullet.x + bullet.radius > self.hitbox[0] and bullet.x - bullet.radius < self.hitbox [0] + self.hitbox[2]:
                    hitSound.play()
                    player.bullets.pop(player.bullets.index(bullet))
                    self.health -= 1
                                                

    def ifCollide(self):
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                player.collision = True

    def shoot(self):
        if self.shootLoop >= 1 and self.shootLoop < 30:
            self.shootLoop += 1
        else:
            self.shootLoop = 0
        
        if self.shootLoop == 0:
            self.bullets.append(projectile(round(self.x + self.width // 2),round(self.y + self.height - player.height//2),10,self.bulletVel * self.facing, self.bulletImage))
            self.shootLoop = 1

        for bullet in self.bullets:
            if (bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > player.hitbox[1]) and (bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox [0] + player.hitbox[2]):
                hitSound.play()
                player.collision = True
                self.bullets.pop(self.bullets.index(bullet))
                
            elif not (bullet.x <= winSize[0] - bullet.vel and bullet.x >= bullet.vel + 100):
                self.bullets.pop(self.bullets.index(bullet))
                
                
                
    def draw(self,win):
        if self.health >= 1:
            self.ifCollide()
            self.shoot()
            self.ifShot()
                                      
            if self.walkCount >= len(self.walkLeft) * 3:
                self.walkCount = 0
                
            if self.facing == 1:
                win.blit(self.walkRight[self.walkCount //3],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3],(self.x,self.y))
                self.walkCount += 1
                

            for bullet in self.bullets:
                bullet.draw(win)
                
            self.hitbox =(round(self.x + self.width * 0.05), round(self.y + self.width * 0.05), round(self.width * 0.9), round(self.height * 0.9))
            pygame.draw.rect(win,(250,0,0),(self.hitbox[0] - 10,self.hitbox[1]-10,self.hitbox[2] + 20,8)) 
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0] - 10,self.hitbox[1]-10,round(self.health / self.fullHealth * (self.hitbox[2]+ 20)) ,8))    
##            pygame.draw.rect(win,(255,0,0),(self.hitbox),2)

            
class boss2(object):
    def __init__(self,x,y,width,height,leftEnd,rightEnd,facing,health, acceleration, walkLeft,walkRight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.leftEnd = leftEnd
        self.rightEnd = rightEnd
        self.walkCount = 0
        self.vel = 0
        '''facing = 1 or -1, determines the walking direction of the object'''
        self.facing = facing
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.health = health
        self.fullHealth = health
        self.acceleration = acceleration
        self.isDefeated = False
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        
        
    def move(self):

        if self.x + self.width + self.vel >= self.rightEnd:
            self.vel = 0
            self.facing = -1
            self.walkCount = 0
            
        elif self.x - self.vel <= self.leftEnd:
            self.facing = 1
            self.walkCount = 0
            self.vel = 0
            
        if self.vel < 14:
            self.vel += 1 * self.acceleration

        self.x += self.vel * self.facing
        self.walkCount += 1

    def ifShot(self):
        for bullet in player.bullets:
            '''When the edge of the bullet is perfectly within the hitbox of the enemy '''                 
            if bullet.y - bullet.radius < self.hitbox[1] + self.hitbox[3] and bullet.y + bullet.radius > self.hitbox[1]:
                if bullet.x + bullet.radius > self.hitbox[0] and bullet.x - bullet.radius < self.hitbox [0] + self.hitbox[2]:
                    hitSound.play()
                    player.bullets.pop(player.bullets.index(bullet))
                    self.health -= 1
                                                


    def ifCollide(self):
        if player.hitbox[1] < self.hitbox[1] + self.hitbox[3] and player.hitbox[1] + player.hitbox[3] > self.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > self.hitbox[0] and player.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                player.collision = True

        
    def draw(self,win):

        if self.health >= 1:
            self.ifCollide()
            self.move()
            self.ifShot()

                              
            if self.walkCount + 1 >= 24:
                self.walkCount = 0
                
            if self.facing == 1:
                win.blit(self.walkRight[self.walkCount //3],(self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3],(self.x,self.y))
                self.walkCount += 1

            self.hitbox =(round(self.x + self.width * 0.05), round(self.y + self.width * 0.05), round(self.width * 0.9), round(self.height * 0.9))
            pygame.draw.rect(win,(250,0,0),(self.hitbox[0] - 10,self.hitbox[1]-10,self.hitbox[2] + 20,8)) 
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0] - 10,self.hitbox[1]-10,round(self.health / self.fullHealth * (self.hitbox[2]+ 20)) ,8))    
##            pygame.draw.rect(win,(255,0,0),(self.hitbox),2)

            
def setModeEasy():
    global player_health, enemy1_vel, enemy2A_vel,enemy2B_vel,enemy2C_vel,enemy2D_vel, bossA_bulletVel,bossB_health, bossB_acceleration
    player_health = 5
    enemy1_vel = 4
    enemy2A_vel = 10
    enemy2B_vel = 5
    enemy2C_vel = 12
    enemy2D_vel = 10
    bossA_bulletVel = 4
    bossB_health = 15
    bossB_acceleration = 1

def setModeHard():
    global player_health, enemy1_vel, enemy2A_vel,enemy2B_vel,enemy2C_vel, enemy2D_vel, bossA_bulletVel,bossB_health
    player_health = 3
    enemy1_vel = 8
    enemy2A_vel = 12
    enemy2B_vel = 6
    enemy2C_vel = 14
    enemy2D_vel = 14
    bossA_bulletVel = 6
    bossB_health = 30
    bossB_acceleration = 3


def defineFigures():
    setModeEasy()
    global player, enemyA, enemyB, enemyC, enemyD, enemyE, enemyF, enemyG, enemyH, enemyI, bossA, bossB 
    player = mainPlayer(20, 400 -48, 25, 48, 5, player_health, playerWalkLeft, playerWalkRight, bulletA)
    enemyA = enemy1(500, 400 - 52, 30 , 52, 100, 400, -1, enemy1_vel, 3, globinWalkLeft, globinWalkRight)
    enemyB = enemy1(300 ,400 - 52, 30,52,100,590,1,enemy1_vel,3, globinWalkLeft, globinWalkRight)
    enemyC = enemy2(350 ,200,57,86,60,400,-1,enemy2A_vel,10, monsterFaceLeft, monsterTurning)
    enemyD = enemy2(450 ,200,57,86,60,400,1,enemy2A_vel,10, monsterFaceLeft, monsterTurning)
    enemyE = enemy2(150 ,200,87,110,60,400,-1,enemy2B_vel,10, ghostFaceLeft, ghostFaceRight)
    enemyF = enemy2(250 ,200,57,86,60,400,1,enemy2C_vel,10, monsterFaceLeft, monsterTurning)
    enemyG = enemy2(350 ,200,87,110,60,400,-1,enemy2B_vel,10, ghostFaceLeft, ghostFaceRight)
    enemyH = enemy2(450 ,200,57,86,60,400,1,enemy2C_vel,10, monsterFaceLeft, monsterTurning)
    enemyI = enemy2(550 ,200,87,110,60,400,-1,enemy2D_vel,10, ghostFaceLeft, ghostFaceRight)
    bossA = boss1(630 - 180, 400 - 200, 180, 200, -1, 20, bossAWalkLeft, bossAWalkRight,bossA_bulletVel, bulletB)
    bossB = boss2(630 - 72,400 - 80, 72, 80, 100, 630 - 72, -1, bossB_health, bossB_acceleration, bossBWalkLeft, bossBWalkRight)

def __init__figures():
    player.__init__(20, 400 -48, 25, 48, 5, player_health, playerWalkLeft, playerWalkRight, bulletA)
    enemyA.__init__(500, 400 - 52, 30, 52, 100, 400, -1, enemy1_vel, 3, globinWalkLeft, globinWalkRight)
    enemyB.__init__(300 ,400 - 52, 30, 52,100,590,1,enemy1_vel,3, globinWalkLeft, globinWalkRight)
    enemyC.__init__(350 , 200, 57, 86, 60, 400,-1,enemy2A_vel,10, monsterFaceLeft, monsterTurning)
    enemyD.__init__(450 , 200, 57, 86, 60, 400,1,enemy2A_vel,10, monsterFaceLeft, monsterTurning)
    enemyE.__init__(150 , 200, 87, 110, 60, 400,-1,enemy2B_vel,10, ghostFaceLeft, ghostFaceRight)
    enemyF.__init__(250 , 200, 57, 86, 60, 400,1,enemy2C_vel,10, monsterFaceLeft, monsterTurning)
    enemyG.__init__(350 , 200, 87, 110, 60, 400,-1,enemy2B_vel,10, ghostFaceLeft, ghostFaceRight)
    enemyH.__init__(450 , 200, 57, 86, 60, 400,1,enemy2C_vel,10, monsterFaceLeft, monsterTurning)
    enemyI.__init__(550 , 200, 87, 110, 60, 400,-1,enemy2D_vel,10, ghostFaceLeft, ghostFaceRight)
    bossA.__init__(630 - 180, 400 - 200, 180, 200, -1, 20, bossAWalkLeft, bossAWalkRight,bossA_bulletVel, bulletB)
    bossB.__init__(630 - 72,400 - 80, 72, 80, 100, 630 - 72, -1, bossB_health, bossB_acceleration, bossBWalkLeft, bossBWalkRight)

    
def drawGameWindow():
    global roundNo,mode,isLost,isWin,isWisdomWin,isPerfectWin,isPeaceWin
                        
    if mode == 0:
        win.blit(bgMode,(0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            mode = 1
            setModeEasy()
            __init__figures()
        elif keys[pygame.K_h]:
            mode = 2
            setModeHard()
            __init__figures()
    
    elif not isWin and not isLost:
        if roundNo == 1:
            win.blit(bg1,(0,0))
            player.draw(win)
            enemyA.draw(win)
            enemyB.draw(win)
            enemyC.draw(win)
            enemyD.draw(win)

        elif roundNo == 2:
            win.blit(bg2,(0,0))
            player.draw(win)
            enemyE.draw(win)
            enemyF.draw(win)
            enemyG.draw(win)
            enemyH.draw(win)
            enemyI.draw(win)

        elif roundNo == 3:
            win.blit(bg3,(0,0))
            player.draw(win)
            bossA.draw(win)
            if bossA.health < 1:
                bossB.draw(win)

        elif roundNo == 4:
            if enemyA.health > 0 and enemyB.health > 0:
                isPeaceWin = True

            if bossB.health > 0: 
                isWisdomWin = True
                
            if player.lifeLeft == player.fullHealth:
                isPerfectWin = True

            if not (isPeaceWin or isWisdomWin or isPerfectWin):
                isWin = True
##                print('normal win at round4')

        if isPeaceWin or isWisdomWin or isPerfectWin:
            if roundNo == 4:
                if isPeaceWin:
                    win.blit(bgPeaceWinPath,(0,0))
                    player.draw(win)
##                    print('isPeaceWin = True, RoundNo = 4')
                else:
                    if isWisdomWin:
                        roundNo += 1
                    else:
                        roundNo += 2

            if roundNo == 5:
                if isWisdomWin:
                    if mode == 1:
                        win.blit(bgWisdomWinPath,(0,0))
                    else:
                        win.blit(bgWisdomWinPathHard,(0,0))
                    player.draw(win)
##                    print('isWisdomWin = True, RoundNo = 5')
                else:
                    if isPerfectWin:
                        roundNo += 1
                    else:
                        isWin = True
##                        print('isWin at round 5')

            if roundNo == 6:
                if isPerfectWin:
                    if mode == 1:
                        win.blit(bgPerfectWinPath,(0,0))
                    else:
                        win.blit(bgPerfectWinPathHard,(0,0))
                    player.draw(win)
##                    print('isPerfect = True, RoundNo = 6')
                else:
                    isWin = True
##                    print('isWin at round6')

            if roundNo == 7:
                isWin = True
##                print('is win at round 7')

        if player.x + player.vel > winSize[0]:
            roundNo += 1
##            print('roundNo' + str(roundNo))
            player.x = player.rebornLoc[0]
            player.bullets = []

        if player.lifeLeft < 1:
            isLost = True

        win.blit(heartImage,(25,35))
        lifeLeftText = font1.render(' X '+ str(player.lifeLeft),1,(255,250,250))
        win.blit(lifeLeftText,(45,35))

    else:
        if isLost:
            if roundNo == 1:
                win.blit(bg1Lost,(0,0))
            if roundNo == 2:
                win.blit(bg2Lost,(0,0))
            if roundNo == 3:
                win.blit(bg3Lost,(0,0))
        else:
            if mode == 1:
                if isPerfectWin:
                    win.blit(bgPerfectWin,(0,0))
                elif isWisdomWin:
                    win.blit(bgWisdomWin,(0,0))
                elif isPeaceWin:
                    win.blit(bgPeaceWin,(0,0))
                else:
                    win.blit(bgWin,(0,0))
                    
            else:
                if isPerfectWin:
                    win.blit(bgPerfectWinHard,(0,0))
                elif isWisdomWin:
                    win.blit(bgWisdomWinHard,(0,0))
                elif isPeaceWin:
                    win.blit(bgPeaceWin,(0,0))
                else:
                    win.blit(bgWinHard,(0,0))
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            mode = 0
            roundNo = 1
            isLost = False
            isWin = False
            isWisdomWin = False
            isPerfectWin = False
            isPeaceWin = False

##mainloop 
clock = pygame.time.Clock()
roundNo = 1
mode = 0
isLost = False
isWin = False
isWisdomWin = False
isPerfectWin = False
isPeaceWin = False
run = True
defineFigures()

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(black,(0,0))
    drawGameWindow()
    pygame.display.update()
  

pygame.quit()


