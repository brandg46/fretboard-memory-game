import pygame 
import random 
import sys 

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guitar Fretboard Quiz")

wood_color = (155, 94, 81)
black = (30, 30, 30)
blue_font = (0, 102, 255)
black, white, red, gray = (0, 0, 0), (255, 255, 255), (255, 0, 0), (200, 200, 200)

standard_tuning = ['E', 'A', 'D', 'G', 'B', 'E']
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

font = pygame.font.SysFont('Arial', 34)
small_font = pygame.font.SysFont('Arial', 22)

FRET_COUNT, STRING_COUNT = 12, 6
FRET_WIDTH, STRING_SPACING = 50, 40
FRETBOARD_X, FRETBOARD_Y = 100, 300

def get_note(string, fret):
    start_index = notes.index(standard_tuning[string])
    return notes [(start_index + fret) % len(notes)]

def draw_fretboard(highlight_string, highlight_fret):
    fretboard_w = FRET_COUNT * FRET_WIDTH
    fretboard_h = (STRING_COUNT - 1) * STRING_SPACING + STRING_SPACING
    pygame.draw.rect(screen, wood_color, (FRETBOARD_X, FRETBOARD_Y, fretboard_w, fretboard_h))

    