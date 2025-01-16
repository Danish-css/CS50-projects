from settings import *


class  Cell():
    
    def __init__(self,pos, color):
        self.image = pygame.Surface(SIZE['cell'])
        self.image.fill(color)
        self.rect = self.image.get_frect(topleft = pos)
        # self.image.draw.rect()
        
    def draw(self, surf): 
        surf.blit(self.image, self.rect)
        pygame.display.update()
        
        

class Letter():
    def __init__(self, character, pos, color = COLORS['input text']):
        font = pygame.font.Font(None, 130)
        self.image = font.render(character.upper(), True, color)
        self.rect = self.image.get_frect(center = pos)
        
    def draw(self, surf):
        self.surf = surf
        self.surf.blit(self.image, self.rect)
        pygame.display.update()
        
        
