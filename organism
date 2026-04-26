
class Organism:
    def __init__(self, name: str, energy: float):
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float):
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy} энергии.")

    def is_alive(self) -> bool:
        return self.energy > 0