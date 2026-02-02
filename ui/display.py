import pygame

# Constants for a professional look
WHITE = (255, 255, 255)
DARK_GREY = (30, 30, 30)
CYAN = (0, 255, 255)
RED = (255, 80, 80)

class Visualizer:
    def __init__(self, width=800, height=500):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Algorithm Benchmarking Suite")
        self.width = width
        self.height = height

    def draw_bars(self, data, active_indices=()):
        self.screen.fill(DARK_GREY)
        bar_width = self.width // len(data)
        
        for i, val in enumerate(data):
            color = CYAN
            if i in active_indices:
                color = RED # Highlight elements being compared
                
            # Normalize height to fit screen
            norm_height = (val / max(data)) * (self.height - 50)
            pygame.draw.rect(self.screen, color, 
                             (i * bar_width, self.height - norm_height, bar_width - 1, norm_height))
        
        pygame.display.update()