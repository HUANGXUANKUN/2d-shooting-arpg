import pygame
pygame.init()

class mainPlayer(object):    
    def __init__(self,x,y,width,height,vel,lifeLeft,winSize):
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
        self.collision = False
        self.walkCount = 0
        self.hitbox = (self.x + 17,self.y + 2,31,57)
        self.bullets = []
        self.shootLoop = 0
        self.lifeLeft = lifeLeft 
        self.walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
        self.walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

    def keysPressed(self,isLeftPressed,isRightPressed,isUpPressed,isSpacePressed):
        if isLeftPressed and self.x >= self.vel:
            self.standing = False
            self.left = True
            self.right = False
            self.x -= self.vel

        elif isRightPressed and self.x < winSize[0]:
            self.standing = False
            self.left = False
            self.right = True
            self.x += self.vel
                
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
        if self.shootLoop > 0:
            self.shootLoop += 1
        if self.shootLoop >3:
            shootLoop = 0
            
        if isSpacePressed and len(self.bullets)<10 and self.shootLoop == 0:
            self.bullets.append(projectile(round(self.x + self.width // 2),round(self.y + self.height//2),3,(248,248,255)))
            shootLoop = 1

        for bullet in self.bullets:
            if bullet.x <= winSize[0] - bullet.vel and bullet.x >= bullet.vel:
                bullet.x += bullet.vel
            else:
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
                self.x = 50
                self.y = winSize[1] // 24 * 17
                self.walkCount = 0
                self.Right = True
                i = 0
                while i < 60:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 61
                            pygame.quit()
                self.collision = False
                
            if self.walkCount > 26:
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

            self.hitbox = (self.x + 17,self.y + 2,31,57)
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)
