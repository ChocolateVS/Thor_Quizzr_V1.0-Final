import pygame
from pygame import display,movie

FPS = 60

pygame.init()

clock = pygame.time.Clock()
movie = pygame.movie.Movie("resources/animation/vid.mp4")

screen = pygame.display.set_mode(movie.get_size())

movie.set_display(movie_screen)
movie.play()

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    screen.blit(movie_screen, (0,0))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()
