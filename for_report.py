
REPOSITORY_URL = "https://github.com/Frisk-sudo/-_-_-"
"""
Модуль с классами организмов для симулятора экосистемы.
"""

class Organism:
    """
    Базовый класс для всех организмов в экосистеме.

    Attributes:
        name (str): Название организма
        energy (float): Уровень энергии организма
    """

    def __init__(self, name: str, energy: float):
        """
        Инициализация организма.

        Args:
            name (str): Название организма
            energy (float): Начальный уровень энергии
        """
        self.name = name
        self.energy = energy

    def eat(self, food_energy: float) -> None:
        """
        Организм получает энергию от пищи.

        Args:
            food_energy (float): Количество энергии от пищи
        """
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy} энергии.")

    def consume_energy(self, amount: float) -> None:
        """
        Организм тратит энергию на жизнедеятельность.

        Args:
            amount (float): Количество расходуемой энергии
        """
        self.energy -= amount
        print(f"{self.name} потратил {amount} энергии на жизнедеятельность.")

    def is_alive(self) -> bool:
        """
        Проверяет, жив ли организм.

        Returns:
            bool: True, если организм жив (энергия > 0), иначе False
        """
        return self.energy > 0

    def __str__(self) -> str:
        """
        Строковое представление организма.

        Returns:
            str: Информация об организме
        """
        return f"{self.name} (энергия: {self.energy})"
    
import random

"""
Модуль с классом экосистемы для симулятора.
"""

class Ecosystem:
    """
    Класс, представляющий экосистему с организмами и их взаимодействием.

    Attributes:
        organisms (list): Список организмов в экосистеме
        day (int): Текущий день симуляции
    """

    def __init__(self):
        """Инициализация экосистемы."""
        self.organisms = []
        self.day = 0

    def add_organism(self, organism: Organism) -> None:
        """
        Добавляет организм в экосистему.

        Args:
            organism (Organism): Организм для добавления
        """
        self.organisms.append(organism)
        print(f"В экосистему добавлен {organism.name}")

    def remove_dead(self) -> None:
        """Удаляет всех мёртвых организмов из экосистемы."""
        dead_count = len([org for org in self.organisms if not org.is_alive()])
        self.organisms = [org for org in self.organisms if org.is_alive()]
        if dead_count > 0:
            print(f"Удалено {dead_count} мёртвых организмов")

    def get_event(self) -> str | None:
        """
        Генерирует случайное событие в экосистеме.

        Returns:
            str | None: Название события или None
        """
        events = [None, "Засуха", "Высокая урожайность", "Дождь", "Плохая погода"]
        chances = [65, 5, 5, 18, 7]
        return random.choices(events, weights=chances, k=1)[0]

    def apply_event_effects(self, event: str | None) -> None:
        """
        Применяет эффекты события к организмам.

        Args:
            event (str | None): Название события
        """
        if event == "Засуха":
            for org in self.organisms:
                org.consume_energy(5)
            print("Засуха: все организмы потеряли 5 энергии")
        elif event == "Высокая урожайность":
            for org in self.organisms:
                org.eat(15)
            print("Высокая урожайность: все организмы получили 15 энергии")
        elif event == "Дождь":
            for org in self.organisms:
                org.eat(8)
            print("Дождь: все организмы получили 8 энергии")
        elif event == "Плохая погода":
            for org in self.organisms:
                org.consume_energy(3)
            print("Плохая погода: все организмы потеряли 3 энергии")

    def simulate_day(self) -> None:
        """
        Симулирует один день в экосистеме.
        """
        self.day += 1
        print(f"\n--- День {self.day} ---")

        # Генерируем и применяем событие
        event = self.get_event()
        if event:
            self.apply_event_effects(event)

        # Организмы тратят энергию на жизнедеятельность
        for org in self.organisms:
            if org.is_alive():
                org.consume_energy(2)
            else:
                print(f"{org.name} мёртв.")

        # Удаляем мёртвых организмов
        self.remove_dead()

        # Выводим текущее состояние экосистемы
        self.print_status()

    def print_status(self) -> None:
        """Выводит текущее состояние экосистемы."""
        if not self.organisms:
            print("В экосистеме нет живых организмов.")
            return

        print("Текущее состояние экосистемы:")
        for org in self.organisms:
            print(f"  {org}")

"""
Модуль контроллера для управления симуляцией экосистемы.
"""

class Controller:
    """
    Контроллер для управления симуляцией экосистемы.
    """

    def __init__(self):
        """Инициализация контроллера."""
        self.ecosystem = Ecosystem()

    def setup_initial_population(self) -> None:
        """Создаёт начальную популяцию организмов."""
        rabbit = Organism("Заяц", 20)
        fox = Organism("Лиса", 30)
        plant = Organism("Растение", 30)

        self.ecosystem.add_organism(rabbit)
        self.ecosystem.add_organism(fox)
        self.ecosystem.add_organism(plant)

    def run_simulation(self, days: int = 10) -> None:
        """
        Запускает симуляцию на заданное количество дней.

        Args:
            days (int): Количество дней для симуляции (по умолчанию 10)
        """
        print("Запуск симуляции экосистемы!")
        self.setup_initial_population()

        for _ in range(days):
            self.ecosystem.simulate_day()

        print(f"\nСимуляция завершена. Прошло {days} дней.")

"""
Точка входа в приложение симулятора экосистемы.
"""

from controller import Controller

def main():
    """Основная функция приложения."""
    controller = Controller()
    controller.run_simulation(days=5)  # Симуляция на 5 дней

if __name__ == "__main__":
    main()
