import EMS


def main() -> None:
    company = EMS.Company()

    company.add_employee(EMS.SalariedEmployee(name="Michael Scott", role=EMS.Role.MANAGER))
    company.add_employee(EMS.SalariedEmployee(name="Pam Beasley", role=EMS.Role.WORKER))
    company.add_employee(EMS.SalariedEmployee(name="Jim Halpert", role=EMS.Role.WORKER))
    company.add_employee(EMS.HourlyEmployee(name="Ryan Howard", role=EMS.Role.INTERN))

    print(company.find_employees(role=EMS.Role.MANAGER))
    print(company.find_employees(role=EMS.Role.WORKER))
    print(company.find_employees(role=EMS.Role.INTERN))

    for employee in company.employees:
        employee.pay()
    
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
