import pygame
from time import time
from PIL import Image, ImageDraw
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
from algorithms.jps import jps

def main():
        # Load the maze image
    image = Image.open("map1.png")
    pixels = image.load()
    width, height = image.size
    maze = [[0 if pixels[i, j] == (229, 229, 229, 255) else 1 for j in range(height)] for i in range(width)]

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pathfinding Demo")

    # Initialize variables
    start = None
    end = None
    algorithm = None

    # Define the colors used for the path and start/end points
    PATH_COLOR = (255, 0, 0)
    START_COLOR = (0, 255, 0)
    END_COLOR = (0, 0, 255)

    # Define the font used for displaying text
    font = pygame.font.Font(None, 30)

    # Create the pathfinding objects
    dijkstra = Dijkstra(maze)
    a_star = AStar(maze)

    # Define the main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks
                if start is None:
                    start = event.pos
                elif end is None:
                    end = event.pos
                else:
                    start = None
                    end = None
            elif event.type == pygame.KEYDOWN:
                # Handle key presses
                if event.key == pygame.K_d:
                    algorithm = dijkstra
                elif event.key == pygame.K_a:
                    algorithm = a_star
                elif event.key == pygame.K_j:
                    algorithm = jps

        # Draw the maze
        for i in range(width):
            for j in range(height):
                color = (255, 255, 255) if maze[i][j] == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (i, j, 1, 1))

        # Draw the start and end points
        if start is not None:
            pygame.draw.circle(screen, START_COLOR, start, 5)
        if end is not None:
            pygame.draw.circle(screen, END_COLOR, end, 5)

        # Find and draw the path
        if start is not None and end is not None and algorithm is not None:
            start_time = time()
            if algorithm == jps:
                operations, path = algorithm(start, end, maze)
            if algorithm == dijkstra:
                path = algorithm.dijkstra(start, end)
                operations = algorithm.operations
            if algorithm == a_star:
                path = algorithm.a_star(start, end)
                operations = algorithm.operations
            end_time = time()

            if path is not None:
                path = [(y, x) for x, y in path]
                draw = ImageDraw.Draw(image)
                draw = draw.line(path, fill=PATH_COLOR, width=2)
                del draw
                image.save("path.png")

                for i, j in path:
                    pygame.draw.rect(screen, PATH_COLOR, (j, i, 1, 1)) 

            # Display the number of operations and the time taken
            operations_text = font.render("Operations: " + str(operations), True, (255, 255, 255))
            time_text = font.render("Time: " + str(round(end_time - start_time, 2)) + "s", True, (255, 255, 255))

            screen.blit(operations_text, (0, 0))
            screen.blit(time_text, (0, 30))




        # Update the display
        pygame.display.update()

    # Quit the game
    pygame.quit()

if __name__ == "__main__":
    main()
 