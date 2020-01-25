import sys
import datetime
from dateutil import relativedelta

def getinfo():
    monthly_pay = int(input('Monthly Payment: $'))
    return monthly_pay
def calPaymentCalendar(amount, monthly_payment, apr):
    months = []
    monthCount = 0
    date = datetime.date.today() 
    while(amount > 0):
        monthCount += 1
        date = date + relativedelta.relativedelta(months=1)
        interest = amount * apr / 12
        if amount < monthly_payment:
            monthly_payment = amount + interest 
        pay_principle = monthly_payment - interest
        amount = amount - pay_principle
        # format values to printable string
        f_month = f'({monthCount}) {date.strftime("%m/1/%y")}'
        f_monthly_payment = f'${format(monthly_payment,".2f")}'
        f_pay_principle = f'${format(pay_principle,".2f")}'
        f_interest = f'${format(interest,".2f")}'
        f_amount = f'${format(amount,".2f")}'
        months.append((f_month,f_monthly_payment,f_pay_principle, f_interest, f_amount))
    return months

def getArgv():
    try:
        loan_amount = sys.argv[1]
        loan_apr = sys.argv[2]
        return (float(loan_amount), float(loan_apr))
    except:
        print('usage: python3 cal.py <loan_principle> <loan_aprt>')
        return exit() #closes the app

    # horizontal line ----------
def h_line(len):
    # [ expression for item in list if conditional ]
    return print(''.join(['-' for item in range(len)]))
def boxify(content):
    WIDTH = 40
    h_line(WIDTH)
    for line in content:
        formated_line = line.ljust(WIDTH - 2, ' ')
        print(f'|{formated_line}|')
    h_line(WIDTH)

def boxifyCalendar(listOfmonths):
    WIDTH = 120
    h_line(WIDTH)
    listOfCol = ['Month', 'Monthly Payment', 'Applied to Principal', 'Applied to Interest', 'Principal' ]
    header = "".join([col.ljust(int(WIDTH/len(listOfCol))," ") for col in listOfCol])
    print(header)
    for month in listOfmonths:
        formated_line =  "".join([col.ljust(int(WIDTH/len(listOfCol))," ") for col in month])
        print(formated_line)
    h_line(WIDTH)




if __name__ == "__main__":
    (loan_principle, loan_apr) = getArgv()
    annual_interest = loan_principle * loan_apr
    interest_daily = (annual_interest)/365.0
    content = []
    content.append(f'Principle: ${loan_principle}')    
    content.append(f'Apr: {loan_apr *100}%')    
    content.append(f'Daily Interest: ${format(interest_daily, ".4f")}')
    content.append(f'Monthly Interest(30 days): ${format(interest_daily * 30, ".2f")}')
    content.append(f'Annual Interest: ${format(annual_interest, ".2f")}')
    boxify(content)
    monthly_payment = getinfo()
    paymentCal = calPaymentCalendar(loan_principle, monthly_payment, loan_apr)
    boxifyCalendar(paymentCal)
