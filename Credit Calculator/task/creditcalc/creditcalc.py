import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str, choices=['diff', 'annuity'])
parser.add_argument('--interest', type=float)
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--periods', type=int)

args = vars(parser.parse_args())

type_ = args['type']
interest = args['interest']
principal = args['principal']
payment = args['payment']
periods = args['periods']


class CreditCalculator:
    def __int__(self):
        pass

    @staticmethod
    def payment_calc(interest, principal, periods):
        interest /= 1200
        annuity = math.ceil(
            principal * (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
        overpayment = (annuity * periods) - principal
        print(f"Your annuity payment = {annuity}!")
        print(f"Overpayment = {overpayment}")

    @staticmethod
    def diff_payment_calc(interest, principal, periods):
        interest /= 1200
        sum_ = 0
        for i in range(periods):
            diff = math.ceil((principal / periods) + interest *
                             (principal - ((principal * ((i + 1) - 1)) / periods)))
            sum_ += diff
            print(f"Month {i + 1}: paid out {diff}")
        overpayment = sum_ - principal
        print()
        print(f"Overpayment = {overpayment}")

    @staticmethod
    def periods_calc(interest, principal, payment):
        interest /= 1200
        periods = math.ceil(
            math.log((payment / (payment - (interest * principal))), 1 + interest)) // 12
        overpayment = (payment * (periods * 12)) - principal
        print(f"You need {periods} years to repay this credit!")
        print(f"Overpayment = {overpayment}")

    @staticmethod
    def principal_calc(interest, payment, periods):
        interest /= 1200
        principal = math.floor(
            payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1)))
        overpayment = (periods * payment) - principal
        print(f"Your credit principal = {principal}!")
        print(f"Overpayment = {overpayment}")


credit_calc = CreditCalculator()

try:
    if type_ == 'annuity':
        if principal is None:
            credit_calc.principal_calc(interest, payment, periods)
        elif payment is None:
            credit_calc.payment_calc(interest, principal, periods)
        elif periods is None:
            credit_calc.periods_calc(interest, principal, payment)
    elif type_ == 'diff':
        credit_calc.diff_payment_calc(interest, principal, periods)
except Exception:
    print("Incorrect parameters")
