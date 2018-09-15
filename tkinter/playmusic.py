import time
import pygame

music_file_path = "test.mp3"
pygame.mixer.init()

track = pygame.mixer.music.load(music_file_path)

pygame.mixer.music.play()

time.sleep(10)
# pygame.mixer.music.pause()
pygame.mixer.music.stop()
