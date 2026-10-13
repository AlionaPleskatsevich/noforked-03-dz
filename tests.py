from utils import get_employee_by_id, get_active_employees, get_fired_employees

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


print("Все тесты успешно пройдены")
