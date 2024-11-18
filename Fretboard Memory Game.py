import pygame 
import random 
import sys 

pygame.init()

WIDTH, HEIGHT = 800, 600 
FPS = 60 
FONT_SIZE = 36

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

standard_tuning = ['E', 'A', 'D', 'G', 'B', 'E']
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

font = pygame.font.SysFont('Arial', FONT_SIZE)
small_font = pygame.font.SysFont('Arial', 24)

def get_note_on_fret(string, fret):
    starting_note = standard_tuning[string]
    start_index = notes.index(starting_note)
    note_index = (start_index + fret) % len(notes)
    return notes[note_index]

    