from labor.models import Labor, Attendance, HourlyAttendance
from ceo.models import Salary, SalaryAdjustment
from datetime import datetime
import calendar
from datetime import date
import decimal
from django.db.models import Sum
from django.shortcuts import get_object_or_404

def salary_adjustment(salary):
    today = date.today()
    month = today.month
    year = today.year
    try:
        adjustment = SalaryAdjustment.objects.get(date__year=year, date__month=month)
        print('Adjustment found:', adjustment)
    except SalaryAdjustment.DoesNotExist:
        print('No adjustment found for the current month')
        return None, None

    if adjustment.amount is not None:
        if adjustment.type == 'bonus':
            adjusted_salary = decimal.Decimal(adjustment.amount)
        elif adjustment.type == 'deduction':
            adjusted_salary = -decimal.Decimal(adjustment.amount)
    elif adjustment.percentage is not None:
        if adjustment.type == 'bonus':
            adjusted_salary = salary * decimal.Decimal(adjustment.percentage / 100)
        elif adjustment.type == 'deduction':
            adjusted_salary = -(salary * decimal.Decimal(adjustment.percentage / 100))
    else:
        return None, None

    return adjusted_salary, adjustment


def calculate_monthly_salary_for_employee(employee, year, month):
    _, total_days_of_month = calendar.monthrange(year, month)
    basic_salary = decimal.Decimal(employee.basic_pay)
    per_day_basic_salary = basic_salary / decimal.Decimal(total_days_of_month)
    employee_hourly_rate = (per_day_basic_salary / decimal.Decimal(8)) + (per_day_basic_salary / decimal.Decimal(8)) * decimal.Decimal(0.2)

    days_worked = Attendance.objects.filter(
        labor=employee,
        date__year=year,
        date__month=month,
        status='present'
    ).count()
    net_salary = per_day_basic_salary * decimal.Decimal(days_worked)

    # Calculate extra hours wages, if any
    extra_hours_wages = decimal.Decimal(0)
    extra_hours = HourlyAttendance.objects.filter(
        attendance__labor=employee,
        attendance__date__year=year,
        attendance__date__month=month
    ).aggregate(total_hours=Sum('hours'))['total_hours']
    if extra_hours:
        extra_hours_wages = decimal.Decimal(extra_hours) * employee_hourly_rate

    adjustment_amount, adjustment = salary_adjustment(net_salary)
    print('adjustment_amount:', adjustment_amount)
    print('adjustment:', adjustment)
    if adjustment_amount is None:
        print('Adjustment amount is None')
    else:
        print('Adjustment amount:', adjustment_amount)
    if adjustment is None:
        print('Adjustment is None')
    else:
        print('Adjustment:', adjustment)

    gross_salary = net_salary + extra_hours_wages
    if adjustment_amount is not None:
        gross_salary += adjustment_amount

    # Create or update the salary record
    Salary.objects.update_or_create(
        labor=employee,
        month=datetime(year, month, 1),
        defaults={
            'basic_salary': basic_salary,
            'gross_salary': gross_salary,
            'days_worked': days_worked,
            'extra_hours_wages': extra_hours_wages,
            'adjustment': adjustment if adjustment is not None else None,
            'status': 'pending'
        }
    )
    return True

def register_labor(applicant, pay=33000, post=None):

    try:
        obj = Labor(
        date_of_birth = applicant.dob,
        user = applicant.user,
        first_name = applicant.first_name,
        last_name=applicant.last_name,
        cnic = applicant.cnic,
        phone = applicant.phone,
        gender = applicant.gender,
        address = applicant.address,
        basic_pay = pay,
        post = post
        )
        obj.save()
        return obj
    except Exception as e:
        print(f'unable to save labor, due to: {e}')
        return None

