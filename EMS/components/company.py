from typing import List

from .roles import Role
from .employee import Employee


class Company:
    """
    Represents a company with employees.
    """

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(
        self,
        employee: Employee
    ) -> None:
        self.employees.append(employee)

    def find_employees(
        self,
        role: Role
    ) -> List[Employee]:
        return [employee for employee in self.employees if employee.role is role]