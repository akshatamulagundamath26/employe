import os

class Employee:
    def __init__(self, name, department, total_days, present_days):
        self.name = name
        self.department = department
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        return (self.present_days / self.total_days) * 100

    def status(self):
        percent = self.attendance_percentage()
        if percent >= 90:
            return "Excellent"
        elif percent >= 75:
            return "Good"
        elif percent >= 50:
            return "Average"
        else:
            return "Poor"


def main():
    if os.getenv("JENKINS_HOME"):
        name = "Akshay"
        dept = "HR"
        total = 100
        present = 90
    else:
        name = input("Enter employee name: ")
        dept = input("Enter department: ")
        total = int(input("Enter total working days: "))
        present = int(input("Enter number of days present: "))

    emp = Employee(name, dept, total, present)

    print("Employee Name :", emp.name)
    print("Department    :", emp.department)
    print("Total Days    :", emp.total_days)
    print("Present Days  :", emp.present_days)
    print(f"Attendance %  : {emp.attendance_percentage():.2f}")
    print("Status        :", emp.status())


if __name__ == "__main__":
    main()
