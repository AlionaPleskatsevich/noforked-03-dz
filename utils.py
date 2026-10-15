# Вернуть сотрудника по ID
from company import employees


def get_employee_by_id(employee_id):
    for employee in employees:
        if employee.get("id") == employee_id:
            return employee
    return None
# print(get_employee_by_id(3))


# Вернуть список работающих сотрудников


def get_active_employees(employees):
    active_employees = []
    for employee in employees:
        if employee.get("fire_year") is None:
            active_employees.append(employee)
    return active_employees


# print(get_active_employees(employees))

# Вернуть список уволенных сотрудников


def get_fired_employees(employees):
    fired_employees = []
    for employee in employees:
        if employee.get("fire_year") is not None:
            fired_employees.append(employee)
    return fired_employees


# print(get_fired_employees(employees))

# Вернуть список сотрудников указанного отдела

def get_department_employees(employees, department):
    dep_employees = []
    for employee in employees:
        if employee.get("department") == department:
            dep_employees.append(employee)
    return dep_employees


# print(get_department_employees(employees, "Sales"))
