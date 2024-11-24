import pygame 
import random 
import sys 

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guitar Notes Game")

wood_color = (155, 94, 81)
black_background = (30, 30, 30)
blue_font = (0, 102, 255)
black, white, red, gray = (0, 0, 0), (255, 255, 255), (255, 0, 0), (200, 200, 200)

standard_tuning = ['E', 'B', 'G', 'D', 'A', 'E']
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

font = pygame.font.SysFont('Arial', 34)
small_font = pygame.font.SysFont('Arial', 22)

FRET_COUNT, STRING_COUNT = 12, 6
FRET_WIDTH, STRING_SPACING = 50, 40
FRETBOARD_X, FRETBOARD_Y = 100, 300

def get_string_num(string_index):
    return string_index + 1

def get_note(string, fret):
    start_index = notes.index(standard_tuning[string])
    return notes[(start_index + fret) % len(notes)]

def draw_fretboard(highlight_string, highlight_fret):
    fretboard_w = FRET_COUNT * FRET_WIDTH
    fretboard_h = (STRING_COUNT - 2) * STRING_SPACING + STRING_SPACING
    pygame.draw.rect(screen, wood_color, (FRETBOARD_X, FRETBOARD_Y, fretboard_w, fretboard_h))

    for i in range(STRING_COUNT):
        y = FRETBOARD_Y + i * STRING_SPACING
        pygame.draw.line(screen, black, (FRETBOARD_X, y), (FRETBOARD_X + fretboard_w, y), 2)
        
        screen.blit(small_font.render(f"{standard_tuning[i]}", True, blue_font), (FRETBOARD_X - 40, y - 12))

    for i in range (FRET_COUNT + 1):
        x = FRETBOARD_X + i * FRET_WIDTH
        pygame.draw.line(screen, black, (x, FRETBOARD_Y), (x, FRETBOARD_Y + fretboard_h), 2)
        
    for fret in [3, 5, 7, 9, 12]:
        x = FRETBOARD_X + fret * FRET_WIDTH - FRET_WIDTH // 2
        y = FRETBOARD_Y + fretboard_h // 2
        pygame.draw.circle(screen, gray, (x, y), 5)

    if highlight_string is not None and highlight_fret is not None: 
        x = FRETBOARD_X + highlight_fret * FRET_WIDTH - FRET_WIDTH // 2
        y = FRETBOARD_Y + highlight_string * STRING_SPACING
        pygame.draw.circle(screen, red, (x, y), 10)

score, attempts = 0, 0
user_guess = ""
string, fret = random.randint(0, 5), random.randint(0, 12)
correct_note = get_note(string, fret)
clock = pygame.time.Clock()

running = True
while running: 
    screen.fill(black_background)

    string_number = get_string_num(string)    
    screen.blit(font.render(f"Guess the note on string {string_number} at fret {fret}", True, blue_font), (50, 50))
    screen.blit(font.render(f"Your guess: {user_guess}", True, blue_font), (50, 150))      
    screen.blit(font.render(f"Score: {score}/{attempts}", True, blue_font), (50, 250))


    draw_fretboard(string, fret)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and user_guess: 
                attempts += 1
                if user_guess.upper() == correct_note:
                    score += 1
                string, fret = random.randint(0, 5), random.randint(0, 12)
                correct_note = get_note(string, fret)
                user_guess = ""
            elif event.key == pygame.K_BACKSPACE:
                user_guess = user_guess[:-1]
            else: 
                user_guess += event.unicode.upper()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

        
       