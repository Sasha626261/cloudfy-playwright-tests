import pytest
import os
from datetime import datetime

# Глобальный список для сбора шагов
test_steps = []

def add_step(step_name, status="passed"):
    """Добавить шаг в лог"""
    test_steps.append({
        "step": step_name,
        "status": status,
        "time": datetime.now().strftime("%H:%M:%S")
    })
    print(f"[{status.upper()}] {step_name}")

@pytest.fixture(scope="function", autouse=True)
def step_logger(request):
    """Fixture для логирования шагов"""
    global test_steps
    test_steps = []  # Очистить перед каждым тестом
    
    yield
    
    # После выполнения теста - вывести summary
    if test_steps:
        print("\n" + "="*60)
        print("TEST STEPS SUMMARY:")
        print("="*60)
        for i, step in enumerate(test_steps, 1):
            print(f"{i}. [{step['time']}] {step['step']} - {step['status']}")
        print("="*60)

# Экспортируем функцию для использования в тестах
pytest.add_step = add_step
