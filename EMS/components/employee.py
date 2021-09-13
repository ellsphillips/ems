from abc import ABC, abstractmethod
from dataclasses import dataclass

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
            print("No days left to take.")
            return
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    def payout_a_holiday(self) -> None:
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            print("Not enough days left to take.")
            return
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")