
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