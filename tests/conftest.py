import pytest
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook для добавления информации в отчет"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        if test_steps:
            # Формируем красивую таблицу
            summary = "\n## Test Execution Steps:\n\n"
            summary += "| # | Time | Step | Status |\n"
            summary += "|---|------|------|--------|\n"
            
            for i, step in enumerate(test_steps, 1):
                status_emoji = "✅" if step['status'] == 'passed' else "❌"
                summary += f"| {i} | {step['time']} | {step['step']} | {status_emoji} {step['status']} |\n"
            
            # Добавляем summary к отчету
            if not hasattr(report, 'sections'):
                report.sections = []
            report.sections.append(('Test Steps', summary))

# Экспортируем функцию
pytest.add_step = add_step
