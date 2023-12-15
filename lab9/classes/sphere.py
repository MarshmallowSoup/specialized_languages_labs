from render import Renderer
import math
from termcolor import COLORS, colored

class Sphere:
    def __init__(self, size, shade, color,ambient, vector):
        renderer_init = Renderer()
        self.size = size
        self.shade = shade
        self.ambient = ambient
        self.light = renderer_init.normalize(vector)
        self.render = renderer_init.return_shades()
        self.color = color


    def draw_sphere(self):
        size, shade, ambient, light, renders = self.size, self.shade, self.ambient, self.light, self.render
        result = []
        renderer_init = Renderer()
        for i in range(int(math.floor(-size)),int(math.ceil(size)+1)):
            x = i + 0.5
            line = ''

            for j in range(int(math.floor(-2*size)),int(math.ceil(2*size)+1)):
                y = j/2 + 0.5
                if x*x + y*y <= size*size:
                    vec = renderer_init.normalize((x,y,math.sqrt(size*size - x*x - y*y)))
                    b = renderer_init.dot(light,vec)**shade + ambient
                    intensity = int((1-b)*(len(renders)-1))
                    line += renders[intensity] if 0 <= intensity < len(renders) else renders[0]
                else:
                    line += ' '

            result.append(line)
        return result
    
    def print(self):
        sphere = self.draw_sphere()
        for item in sphere:
            print(colored(item, self.color))

    def write(self):
        sphere = self.draw_sphere()
        with open("output.txt", "w") as file:
            for item in sphere:
                file.write(item + "\n")