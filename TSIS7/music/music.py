import pygame
pygame.init()
screen = pygame.display.set_mode((1024, 800))
songs = ['Yesterday.wav','All-you-need-is-love.wav','Help.wav']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
paused = False
keys = pygame.key.get_pressed()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_SPACE:
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False
    pygame.display.flip()