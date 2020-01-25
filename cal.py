import sys

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
    HEIGHT = 30
    h_line(WIDTH)
    for line in content:
        formated_line = line.ljust(WIDTH - 2, ' ')
        print(f'|{formated_line}|')
    h_line(WIDTH)



if __name__ == "__main__":
    (loan_principle, loan_apr) = getArgv()
    annual_interest = loan_principle * loan_apr
    interest_daily = (annual_interest)/365.0
    content = []
    content.append(f'Principle: ${loan_principle}')    
    content.append(f'Apr: {loan_apr *100}%')    
    content.append(f'Daily Interest: ${format(interest_daily, ".2f")}')
    content.append(f'Monthly Interest(30 days): ${format(interest_daily * 30, ".2f")}')
    content.append(f'Annual Interest: ${format(annual_interest, ".2f")}')
    boxify(content)