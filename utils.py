# Вернуть сотрудника по ID
from company import employees


def get_employee_by_id(employee_id):
    for employee in employees:
        if employee.get("id") == employee_id:
            return employee
    return None
# print(get_employee_by_id(3))


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

print("Вернуть по ID - OK")


# Вернуть список работающих сотрудников


def get_active_employees(employees):
    active_employees = []
    for employee in employees:
        if employee.get("fire_year") is None:
            active_employees.append(employee)
    return active_employees


# print(get_active_employees(employees))


assert get_active_employees([{"fire_year": None}]) == [{"fire_year": None}], "Сотрудник уволился"
assert get_active_employees([{"fire_year": 2023}]) == [], "Вернулся уволенный"
assert len(get_active_employees([{"fire_year": None}])) != 0, "Штат пуст"


print("Работающие сотрудники - OK")

# Вернуть список уволенных сотрудников


def get_fired_employees(employees):
    fired_employees = []
    for employee in employees:
        if employee.get("fire_year") is not None:
            fired_employees.append(employee)
    return fired_employees


# print(get_fired_employees(employees))


assert get_fired_employees([{"fire_year": None}]) == [], "Вернулся работающий"
assert get_fired_employees([{"fire_year": 2023}]) == [{"fire_year": 2023}], "Не все уволенные вернулись"
assert len(get_fired_employees([{"fire_year": 2025}])) != 0, "Нет уволенных"


print("Уволенные сотрудники - OK")
