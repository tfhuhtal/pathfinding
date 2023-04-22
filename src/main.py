from time import time
from PIL import Image, ImageDraw
from algorithms.dijkstra import Dijkstra
from algorithms.astar import AStar
from algorithms.jps import JumpPointSearch

def main():

    image = Image.open("orz702d.png")
    pixels = image.load()
    width, height = image.size
    matrix = [[pixels[j, i] for j in range(width)] for i in range(height)]
    maze = [[0 if matrix[i][j] == (229, 229, 229, 255) \
             else 1 for j in range(width)] for i in range(height)]

    dijkstra = Dijkstra(maze)
    a_star = AStar(maze)
    jps = JumpPointSearch(maze)

    start =  (height//9, width//4) #(height//9 + 60, width//2 - 155)
    end = (height//2 +170, width//2 + 125) #(height - 28, width//2 - 340)


    #start_time = time()
    #path = dijkstra.dijkstra(start, end)
    #end_time = time()
    #opr = dijkstra.operations
    #length = dijkstra.distances[end[0]][end[1]]
    #print(f"Dijkstra: Path length: {length} Time taken: {(end_time - start_time)*1000:.2f} ms Operations: {opr}")

    start_time = time()
    path = a_star.a_star(start, end)
    end_time = time()
    opr = a_star.operations
    length = a_star.distances[end[0]][end[1]]
    print(f"A*: Path length: {length} Time taken: {(end_time - start_time)*1000:.2f} ms Operations: {opr}")

    start_time = time()
    path = jps.search(start, end)
    end_time = time()
    opr = jps.operations
    length = jps.distances[end[0]][end[1]]
    print(f"JPS: Path length: {length} Time taken: {(end_time - start_time)*1000:.2f} ms Operations: {opr}")

    path = [(x, y) for y, x in path]

    draw = ImageDraw.Draw(image)
    draw.point(path, fill=(255,0,0))
    image.save("path_normal_jps.png")


if __name__ == "__main__":
    main()
 