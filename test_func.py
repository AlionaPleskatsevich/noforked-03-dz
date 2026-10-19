import pytest
from utils import get_employee_by_id


@pytest.mark.parametrize(
         "employee_id,result",
         [
             (666, None),
             (0, None),
             (-3, None),
             ("a", None),
             ("@", None),
             (6, {
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
                     {"year": 2026, "salary": 4300, "projects": 4}]})])
def test_get_employee_by_id(employee_id, result):
    assert get_employee_by_id(employee_id) == result
