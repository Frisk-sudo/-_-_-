from ecosystem import Ecosystem
from organism import Organism

def main():
   eco = Ecosystem()
   rabbit = Organism("Заяц", 20)
   fox = Organism("Лиса", 30)

   eco.add_organism(rabbit)
   eco.add_organism(fox)

   eco.simulate_day()

if __name__ == "__main__":
   main()
