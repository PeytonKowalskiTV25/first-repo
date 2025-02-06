import pygame
import sys

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Framed Text")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)

def drawFramedBox(surface, text, rect, color, frameColor):
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, frameColor, rect, 1)
    text = font.render(text, True, BLACK)
    textRect = text.get_rect()
    textRect.center = rect.center
    surface.blit(text, textRect)

def main():
    inputText = ""
    clock = pygame.time.Clock()
    inputBox = pygame
    borderWidth = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(inputText)
                    inputText = ""
                elif event.key == pygame.K_BACKSPACE:
                    inputText = inputText[:-1]
                else:
                    inputText += event.unicode

        window.fill(WHITE)
        drawFramedBox(window, inputText, pygame.Rect(50, 50, 200, 50), RED, BLACK)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()