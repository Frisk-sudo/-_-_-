"""
Модуль контроллера для управления симуляцией экосистемы.
"""
from ecosystem import Ecosystem
from organism import Organism

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