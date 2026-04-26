
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
