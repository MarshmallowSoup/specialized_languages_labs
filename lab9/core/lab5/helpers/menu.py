from figures.sphere import Sphere
from figures.kube import Kube

class Menu:
    def __init__(self):
        # Default figure = sphere
        self.size = 20
        self.shade = 3
        self.color = "red"
        self.ambient = 0.2
        self.vector = (30, 40, -50)

    def display_menu(self):
        print("1. Create Sphere")
        print("2. Create Cube")
    
    def get_user_choice(self):
        return int(input("Enter your choice (1 for Sphere, 2 for Cube): "))
    
    def ask_write_to_file(self, figure):
        answer = input("Do you want to write this figure to a file? (yes/no): ").lower()
        if answer == 'yes':
            figure.write()

    def create_shape(self):
        self.display_menu()
        choice = self.get_user_choice()

        if choice == 1:
            sphere = self.create_sphere()
            sphere.print()
            self.ask_write_to_file(sphere)
            return sphere
        elif choice == 2:
            kube = self.create_kube()
            kube.print()
            self.ask_write_to_file(kube)
            return 
        else:
            print("Invalid choice. Please choose 1 or 2.")
            return None

    def create_sphere(self):
        self.size = float(input("Enter the size of the sphere: "))
        self.shade = int(input("Enter the shade level (integer): "))
        self.color = input("Enter the color of the sphere: ")
        self.ambient = float(input("Enter the ambient light level (float): "))
        self.vector = tuple(map(float, input("Enter the light direction vector (comma-separated, e.g., 1,0,0): ").split(',')))
        return Sphere(self.size, self.shade, self.color, self.ambient, self.vector)

    def create_kube(self):
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        z = int(input("Enter z: "))
        color = input("Enter color: ")

        return Kube(x, y, z, color)