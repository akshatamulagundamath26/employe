import pytest
from attendance import Employee

def test_attendance_percentage():
    emp = Employee("Akshay", "HR", 100, 90)
    assert emp.attendance_percentage() == 90

def test_status_excellent():
    emp = Employee("Akshay", "HR", 100, 95)
    assert emp.status() == "Excellent"

def test_status_good():
    emp = Employee("Akshay", "HR", 100, 80)
    assert emp.status() == "Good"

def test_status_average():
    emp = Employee("Akshay", "HR", 100, 60)
    assert emp.status() == "Average"

def test_status_poor():
    emp = Employee("Akshay", "HR", 100, 40)
    assert emp.status() == "Poor"
