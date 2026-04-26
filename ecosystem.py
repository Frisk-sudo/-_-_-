from organism import Organism

class Ecosystem:
   def __init__(self):
      self.organisms = []

   def add_organism(self, organism: Organism):
      self.organisms.append(organism)

   def simulate_day(self):
      for org in self.organisms:
         if org.is_alive():
            org.eat(10)
         else:
            print(f"{org.name} мёртв.")