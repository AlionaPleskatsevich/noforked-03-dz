from utils import get_employee_by_id, get_active_employees, get_fired_employees, get_department_employees
from company import employees

# Вернуть сотрудника по ID


def test_get_employee_by_id():
    assert get_employee_by_id(666) is None, "Ид не существует"
    assert get_employee_by_id(0) is None, "ИД должен быть >0"
    assert get_employee_by_id(-3) is None, "Ид не может быть отрицательным"
    assert get_employee_by_id(6) == {
        "id": 6,
        "name": "Ольга Мороз",
        "department": "Sales",
        "age": 27,
        "hire_year": 2023,
        "fire_year": None,
        "history": [
            {"year": 2023, "salary": 2800, "projects": 2},
            {"year": 2024, "salary": 3200, "projects": 3},
            {"year": 2025, "salary": 3700, "projects": 4},
            {"year": 2026, "salary": 4300, "projects": 4}
        ]
    }, "Информация устарела"
    assert get_employee_by_id("а") is None, "Корректное значение ИД - число"
    assert get_employee_by_id("@") is None, "Корректное значение ИД - число"  # лучше реализовать через исключение
# Вернуть список работающих сотрудников


def test_get_active_employees():
    assert get_active_employees([{"fire_year": None}]) == [{"fire_year": None}], "Сотрудник уволился"
    assert get_active_employees([{"fire_year": 2023}]) == [], "Вернулся уволенный"
    assert len(get_active_employees([{"fire_year": None}])) != 0, "Штат пуст"

# Вернуть список уволенных сотрудников


def test_get_fired_employees():
    assert get_fired_employees([{"fire_year": None}]) == [], "Вернулся работающий"
    assert get_fired_employees([{"fire_year": 2023}]) == [{"fire_year": 2023}], "Не все уволенные вернулись"
    assert len(get_fired_employees([{"fire_year": 2025}])) != 0, "Нет уволенных"

# Вернуть список сотрудников указанного отдела


def test_get_department_employees():
    assert get_department_employees(employees, "Dev") == [], "Devов взяли в штат"
    assert len(get_department_employees(employees, "HR")) != 0, "Уволены все HRы"
    assert len(get_department_employees(employees, "Finance")) == 3, "Количество финансистов изменилось"
    assert len(get_department_employees(employees, "IT")) == 4, "Сотрудников IT было 4"
    assert get_department_employees(employees, "Sales") == [{'id': 6, 'name': 'Ольга Мороз', 'department': 'Sales', 'age': 27, 'hire_year': 2023, 'fire_year': None, 'history': [{'year': 2023, 'salary': 2800, 'projects': 2}, {'year': 2024, 'salary': 3200, 'projects': 3}, {'year': 2025, 'salary': 3700, 'projects': 4}, {'year': 2026, 'salary': 4300, 'projects': 4}]}, {'id': 14, 'name': 'Юлия Краснова', 'department': 'Sales', 'age': 31, 'hire_year': 2019, 'fire_year': None, 'history': [{'year': 2023, 'salary': 3700, 'projects': 5}, {'year': 2024, 'salary': 4000, 'projects': 6}, {'year': 2025, 'salary': 4300, 'projects': 6}, {'year': 2026, 'salary': 4600, 'projects': 7}]}], "Список продажников изменился"
    assert get_department_employees(employees, "3") == [], "Неверное значение отдела"


test_get_employee_by_id()


test_get_active_employees()
test_get_fired_employees()
test_get_department_employees()


print("Все тесты успешно пройдены")
