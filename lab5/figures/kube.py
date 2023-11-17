from termcolor import colored, COLORS

class Kube:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color


    def print(self):
        kube = self.draw()
        for item in kube:
            print(item)

    def write(self):
        kube = self.draw()
        with open("output.txt", "w") as file:
            for item in kube:
                file.write(item + "\n")
                
    def generate_kube(self, n, x, y, cde):
        output = colored(
            f"{str(cde[0]).rjust(n + 1)}" +
            f"{cde[1] * (9 * x - 1)}" +
            f"{cde[0]}" +
            f"{str(cde[2]).rjust(y + 1) if len(cde) > 2 else ''}"
        , self.color)
        return output

    def draw(self):
        result = [self.generate_kube(self.y + 1, self.x, 0, '+-')]

        for i in range(1, self.y):
            result.append(self.generate_kube(self.y - i + 1, self.x, i - 1, '/ |'))

        result.append(self.generate_kube(0, self.x, self.y, '+-|'))

        for _ in range(4 * self.z - self.y - 3):
            result.append(self.generate_kube(0, self.x, self.y, '| |'))

        result.append(self.generate_kube(0, self.x, self.y, '| +'))

        for i in range(self.y - 1, 0, -1):
            result.append(self.generate_kube(0, self.x, i, '| /'))

        result.append(self.generate_kube(0, self.x, 0, "+-\n"))

        return result