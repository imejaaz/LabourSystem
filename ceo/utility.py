from labor.models import Labor, Attendance, HourlyAttendance
from ceo.models import Salary, SalaryAdjustment
from datetime import datetime
from django.db.models import Sum
import calendar



def salary_adjustment(salary, month, year):
    adjustment = SalaryAdjustment.objects.get_or_404(
        date__year=year,
        date__month=month
    )
    if adjustment:
        if adjustment.amount and adjustment.type == 'bonus':
            return salary+adjustment_amount
        if adjustment.amount and adjustment.type == 'deduction':
            return salary-adjustment_amount
        if adjustment.percentage and adjustment.percentage == 'bonus':
            return salary+((salary/100)*adjustment.percentage)
        if adjustment.percentage and adjustment.type == 'deduction':
            return salary-((salary/100)*adjustment.percentage)

def calculate_monthly_salary_for_employee(employee, year, month):
    _, total_days_of_month = calendar.monthrange(year, month)
    basic_salary = employee.basic_pay
    per_day_basic_salary = int(basic_salary) / int(total_days_of_month)
    employee_hourly_rate = (per_day_basic_salary/8) + (per_day_basic_salary/8)*0.2
    days_worked = Attendance.objects.filter(
        labor=employee,
        date__year=year,
        date__month=month,
        status='present'
    ).count()
    net_salary = per_day_basic_salary * days_worked

    # Calculate extra hours wages, if any
    extra_hours_wages = 0
    extra_hours = HourlyAttendance.objects.filter(
        attendance__labor=employee,
        attendance__date__year=year,
        attendance__date__month=month
    ).aggregate(total_hours=Sum('hours'))['total_hours']
    if extra_hours:
        extra_hours_wages = extra_hours * employee_hourly_rate


    # Calculate gross salary
    gross_salary = net_salary + extra_hours_wages

    # Create or update the salary record
    Salary.objects.update_or_create(
        labor=employee,
        month=datetime(year, month, 1),
        defaults={
            'basic_salary': basic_salary,
            'gross_salary': gross_salary,
            'days_worked': days_worked,
            'extra_hours_wages': extra_hours_wages,
            # 'adjustment': adjustment_amount,
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

