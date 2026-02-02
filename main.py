import pygame
import random
from ui.display import Visualizer
from algorithms.sorts import bubble_sort, quick_sort

def main():
    # Setup
    n_elements = 100
    data = [random.randint(10, 450) for _ in range(n_elements)]
    
    view = Visualizer()
    clock = pygame.time.Clock()
    
    # We choose the algorithm here
    # Note: quick_sort is a recursive generator, we initialize it differently
    sorting_generator = quick_sort(data, 0, len(data) - 1)
    
    running = True
    sorting = True
    
    while running:
        clock.tick(60) # Cap at 60 FPS for smooth rendering
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if sorting:
            try:
                # Get the next state from our generator
                # 'active_indices' are the elements currently being compared/swapped
                data, *active_indices = next(sorting_generator)
                view.draw_bars(data, active_indices)
            except StopIteration:
                sorting = False
                # Final draw to show completion in Cyan
                view.draw_bars(data)

    pygame.quit()

if __name__ == "__main__":
    main()