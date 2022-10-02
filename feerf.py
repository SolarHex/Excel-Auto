import pygame

w = 500
h = 500

win = pygame.display.set_mode((w,h))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self,x,y, w, h, color):
        self.x = x 
        self.y = y
        self.w = w
        self.h = h
        self.color = color 
        self.rect = (x,y,w,h)
        self.vel = 3
        
        #draw a rectangle
    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)
#how they move we check it there 
    def move(self):
        keys = pygame.keys.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            
        if keys[pygame.K_UP]:
            self.y -= self.vel
            
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            

def redrawWindow():
    
    win.fill((255,255,255))
    pygame.display.update()
    
def main():
    run =True
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        redrawWindow()