
"""
Модуль с классом экосистемы для симулятора.
"""
import random

from organism import Organism


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