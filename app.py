from EMS.components.roles import Role
from EMS.components.employee import HourlyEmployee, SalariedEmployee
from EMS.components.company import Company


def main() -> None:
    company = Company()

    company.add_employee(SalariedEmployee(name="Michael Scott", role=Role.MANAGER))
    company.add_employee(SalariedEmployee(name="Pam Beasley", role=Role.WORKER))
    company.add_employee(SalariedEmployee(name="Jim Halpert", role=Role.WORKER))
    company.add_employee(HourlyEmployee(name="Ryan Howard", role=Role.INTERN))

    print(company.find_employees(role=Role.MANAGER))
    print(company.find_employees(role=Role.WORKER))
    print(company.find_employees(role=Role.INTERN))

if __name__ == "__main__":
    main()
