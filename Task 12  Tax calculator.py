from datetime import datetime, date, time, timedelta

class Employee():
    def __init__(self, Employee_name, date2):
        self.Employee_name = Employee_name
        self.date2 = date2

    def overtime(self,Hours_worked,Second_Overtime_rate,standard_work_hours_per_month,Overtime_hours_firs_range,First_Overtime_rate):
        self.Overtime_hours_firs_range = Overtime_hours_firs_range
        self.Hours_worked = Hours_worked
        self.Second_Overtime_rate = Second_Overtime_rate
        self.standard_work_hours_per_month = standard_work_hours_per_month
        self.First_Overtime_rate = First_Overtime_rate
        if self.Hours_worked > self.standard_work_hours_per_month:
            first_range = (self.Overtime_hours_firs_range - self.standard_work_hours_per_month)*self.First_Overtime_rate
            second_range = (self.Hours_worked - self.Overtime_hours_firs_range) * self.Second_Overtime_rate
            totalOvertime = first_range+second_range
            return totalOvertime
        else:
            return 0
        


    def gross_pay(self,totalOvertime,Hourly_rate,):
        self.Hourly_rate = Hourly_rate
        self.totalOvertime = totalOvertime
        if self.Hours_worked < self.standard_work_hours_per_month:
            gross_pay = self.Hours_worked * self.Hourly_rate
            return gross_pay
        else:
            gross_pay = self.totalOvertime + (self.standard_work_hours_per_month * self.Hourly_rate)
            return gross_pay
    def Tax_deducted(self,gross_pay,tax_deduct):
        self.tax_deduct = tax_deduct
        self.gross_pay = gross_pay
        if tax_deduct == "yes":
            return (self.gross_pay / 100) * 22
        elif tax_deduct == "no":
            return (self.gross_pay / 100) * 25

    def National_insurance_deducted (self,gross_pay):
        self.gross_pay = gross_pay
        return (gross_pay/100)*7
    def Net_pay (self,gross_pay,National_insurance_deducted,tax_deducted):
        self.National_insurance_deducted = National_insurance_deducted
        self.gross_pay = gross_pay
        self.tax_deducted = tax_deducted
        return self.gross_pay - self.National_insurance_deducted - self.tax_deducted
    def display(self, Net_pay):
        self.Net_pay= Net_pay
        
        print(f'Employee name: {self.Employee_name}')
        print(f'Date: {self.date2}')
        print(f'Hourly rate: {self.Hourly_rate}')
        print(f'Overtime rate for first range: {self.First_Overtime_rate}')
        print(f'Overtime rate for second range: {self.Second_Overtime_rate}')
        print(f'Hours worked: {self.Hours_worked}')
        if self.Hours_worked < self.standard_work_hours_per_month:
            print(f'Overtime hours worked: 0')
        else:
            Overtime_hours_worked = self.Hours_worked - self.standard_work_hours_per_month
            print(f'Overtime hours worked: {round((Overtime_hours_worked),2)}')
        print(f'Pay at overtime rate: {round(self.totalOvertime,2)}')
        if self.Hours_worked < self.standard_work_hours_per_month:
            print(f'Pay at normal rate: {round((self.Hours_worked * self.Hourly_rate),2)}')
        else:
            print(f'Pay at normal rate: {round((self.standard_work_hours_per_month * self.Hourly_rate),2)}')
        print(f'Gross pay: {round(self.gross_pay,2)}')
        print(f'National insurance deducted: {round(self.National_insurance_deducted,2)}')
        print(f'Tax deducted: {round(self.tax_deducted,2)}')
        print(f'Net pay: {round(self.Net_pay,2)}')



def data_employee(): # function calls main class
    Employee_name = str(input("Enter please Employee name ")) # input with float, because walls size would be different sizes.
    date2 = date.today()
    Hours_worked = float(input("Enter please Hours worked "))
    while Hours_worked < 0:
        print("It has to be a positive number")
        Hours_worked = float(input("Enter please Hours worked "))
    standard_work_hours_per_month = int(input("Enter please standard work hours per week "))
    Hourly_rate = float(input("Enter please Hourly rate "))
    Overtime_hours_firs_range = float(input("Can you put the hour that is border between range first overtime rate and second overtime rate?  "))
    First_Overtime_rate = float(input("Enter please Overtime rate for first range above your standard hours "))
    Second_Overtime_rate = float(input("Enter please Overtime rate for second overtime range above your standard hours "))
    e = Employee(Employee_name,date2)
    totalOvertime = e.overtime(Hours_worked,Second_Overtime_rate,standard_work_hours_per_month,Overtime_hours_firs_range,First_Overtime_rate)
    gross_pay = e.gross_pay(totalOvertime,Hourly_rate)
    tax_deduct = str(input("Are you marred? yes/no "))
    tax_deducted = e.Tax_deducted(gross_pay,tax_deduct)
    National_insurance_deducted = e.National_insurance_deducted(gross_pay)
    Net_pay = e.Net_pay(gross_pay,National_insurance_deducted,tax_deducted)
    e.display(Net_pay)


while True:

    x = 10
    while x >= 10 and x <= 19:
        data_employee()
        x += 1
        print(f"Now {x} employees")
        if x == 15:
            print(f"I need to alert you, here {x} employees")
            continue
    break
try:
    quit()  # Quit by raising SystemExit
except SystemExit:  # Handle SystemExit gracefully
    print("It is maximum number of employees")
