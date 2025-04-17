import pygame
import sys
import copy

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 600
CELL_SIZE = 10
ERASER_SIZE = 10

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
COLOR_PALETTE = [RED, GREEN, YELLOW,GRAY,WHITE,BLUE]

def create_grid():
    grid = []
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        row = []
        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            row.append({'rect': rect, 'color': BLUE})
        grid.append(row)
    return grid

def draw_grid(screen, grid):
    for row in grid:
        for cell in row:
            pygame.draw.rect(screen, cell['color'], cell['rect'])

def draw_palette(screen, active_color):
    for i, color in enumerate(COLOR_PALETTE):
        rect = pygame.Rect(10 + i * 50, 10, 40, 40)
        pygame.draw.rect(screen, color, rect)
        if color == active_color:
            pygame.draw.rect(screen, (0, 0, 0), rect, 4)  
        else:
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

def save_snapshot(history, grid):
    history.append(copy.deepcopy(grid))
    if len(history) > 50:
        history.pop(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Canvas with Features")

    clock = pygame.time.Clock()

    grid = create_grid()
    undo_stack = []
    redo_stack = []
    color = RED  # Default selected color
    eraser_mode = False  # Start in draw mode
    brush_size = ERASER_SIZE

    save_snapshot(undo_stack, grid)

    running = True
    while running:
        screen.fill(WHITE)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        eraser_rect = pygame.Rect(mouse_x, mouse_y, brush_size, brush_size)

        keys = pygame.key.get_pressed()
        ctrl_held = keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    eraser_mode = not eraser_mode  # Toggle erase/draw mode

                elif event.key == pygame.K_LEFTBRACKET:
                    brush_size = max(10, brush_size - 10)

                elif event.key == pygame.K_RIGHTBRACKET:
                    brush_size = min(100, brush_size + 10)

                elif ctrl_held and event.key == pygame.K_z:
                    if undo_stack:
                        redo_stack.append(copy.deepcopy(grid))
                        grid = undo_stack.pop()

                elif ctrl_held and event.key == pygame.K_y:
                    if redo_stack:
                        undo_stack.append(copy.deepcopy(grid))
                        grid = redo_stack.pop()

            # Color picker
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, palette_color in enumerate(COLOR_PALETTE):
                    palette_rect = pygame.Rect(10 + i * 50, 10, 40, 40)
                    if palette_rect.collidepoint(event.pos):
                        color = palette_color

        # Mouse painting/erasing
        left_pressed, _, _ = pygame.mouse.get_pressed()
        grid_changed = False

        for row in grid:
            for cell in row:
                if eraser_rect.colliderect(cell['rect']):
                    if left_pressed:
                        if eraser_mode and cell['color'] != WHITE:
                            cell['color'] = WHITE
                            grid_changed = True
                        elif not eraser_mode and cell['color'] != color:
                            cell['color'] = color
                            grid_changed = True

        if grid_changed:
            save_snapshot(undo_stack, grid)
            redo_stack.clear()

        draw_grid(screen, grid)
        draw_palette(screen, color)
        pygame.draw.rect(screen, GRAY, eraser_rect, 2)  # Cursor brush border

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
