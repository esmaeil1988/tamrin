class Employee:
    def __init__(self, n, f, a, emp_id):
        self.name = n
        self.family = f
        self.age = a
        self.emp_id = emp_id

    def chap(self):
        print(self.name + "|" + self.family + "|", self.age, self.emp_id)

class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__("Mohammad", "Malekpour", 26, 153)
        self.hour = int(input("Enter hour:"))

    def hr_rate(self):
        print(3000 * self.hour)

class MonthlyEmployee(Employee):
    def __init__(self):
        super().__init__("Ali", "Sadeghi", 29, 198)

hourly_emp = HourlyEmployee()
hourly_emp.hr_rate()

monthly_emp = MonthlyEmployee()
monthly_emp.chap()
