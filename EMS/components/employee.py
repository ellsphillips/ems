from abc import ABC, abstractmethod
from dataclasses import dataclass


from ..utilities.errors import VacationDaysShortageError
from ..utilities.constants import FIXED_VACATION_DAYS_PAYOUT
from .roles import Role


@dataclass
class Employee(ABC):
    """
    Basic representation of an employee at the company.
    """

    name: str
    role: Role
    vacation_days: int = 25

    @abstractmethod
    def pay(self) -> None:
        pass

    def take_a_holiday(self) -> None:
        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any holidays left. Now back to work, you!",
            )
        self.vacation_days -= 1
        print(f"Have fun on your holiday, {self.name}! Don't forget to check your emails!")

    def payout_a_holiday(self) -> None:
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise VacationDaysShortageError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="You don't have enough holidays left over for a payout",
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")


@dataclass
class HourlyEmployee(Employee):
    """
    Employee that's paid based on number of hours worked.
    """
    hourly_rate: float = 50
    hours_worked: int = 10

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a hourly rate of \
            ${self.hourly_rate} for {self.hours_worked} hours."
        )


@dataclass
class SalariedEmployee(Employee):
    """
    Employee that's paid based on a fixed monthly salary.
    """
    monthly_salary: float = 5000

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}."
        )
