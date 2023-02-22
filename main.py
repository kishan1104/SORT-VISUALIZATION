import pygame
import random
from setting import *

pygame.font.init()

#space to start the algorithm


WIN = pygame.display.set_mode((WIDTH,HEIGHT+CONTROLS))
left = 0
random_rect = {
    'height' : 0,
    "width" : SIZE,
    "top" : 0
    
}

START = pygame.font.SysFont('comicsans', 30)

G_ARR = []


def controls():
    start = 'start/stop : SPACE'
    reset = 'reset: R'
    fps = 'FPS: UP/DOWN arrow'
    start_text = START.render(start, 1, WHITE)
    reset_text = START.render(reset, 1, WHITE)
    fps_text = START.render(fps, 1, WHITE)
    
    WIN.blit(start_text, (50,HEIGHT))
    WIN.blit(reset_text, (350,HEIGHT))
    WIN.blit(fps_text, (500,HEIGHT))
    
def initialize_rect():
    for i in range(COL):
        G_ARR.append(random_rect.copy())
        call = random.randint(0, HEIGHT)
        G_ARR[i]["height"] = call
        G_ARR[i]['top'] = HEIGHT -call
    
            
            
def col_grid():
    for x in range(0,WIDTH,SIZE):
        pygame.draw.line(WIN, WHITE, (x,0), (x,HEIGHT))

    
def draw_dis():
    for i in range(0,WIDTH,SIZE):
        k = i//SIZE
        if k<COL:
            # G_ARR[i//SIZE]['left'] = i
            pygame.draw.rect(WIN,WHITE,pygame.Rect(i, G_ARR[i//SIZE]['top'], SIZE, G_ARR[i//SIZE]['height']))        
    
    
def bubble_sort():
    for i in range(len(G_ARR)):
        for j in range(0,len(G_ARR)-i-1):
            if G_ARR[j]['height'] > G_ARR[j+1]['height']:
                G_ARR[j],G_ARR[j+1] = G_ARR[j+1],G_ARR[j]
                return
            
def insersion_sort():# this algorithm won't work sry any update is appreciated 
    for i in range(len(G_ARR)):
    # Find the minimum element in remaining 
    # unsorted array
        min_idx = i
        for j in range(i+1, len(G_ARR)):
            if G_ARR[min_idx]['height'] > G_ARR[j]['height']:# this is giving an error int object is not subscriptable
                min_idx = j
             
    # Swap the found minimum element with 
    # the first element        
        G_ARR[i], G_ARR[min_idx] = G_ARR[min_idx], G_ARR[i]
        print("yes")
        return
        
        
def draw(run):
    WIN.fill(BLACK)
    col_grid()
    # h_rect()
    if run:
        bubble_sort()
    # insersion_sort()
    controls()
    draw_dis()
    
    pygame.display.update()

def main():
    global FPS
    clock = pygame.time.Clock()
    run = True
    initialize_rect()
    run_sort = False
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_sort = not run_sort
                if event.key == pygame.K_r:
                    initialize_rect()
                if event.key == pygame.K_UP:
                    if FPS < 60:
                        FPS +=5
                if event.key == pygame.K_DOWN:
                    if FPS >11:
                        FPS -=5
                
        draw(run_sort)
        
        
    pygame.quit()


if __name__ == "__main__":
    
    main()
    