# http://www.rd.go.th/publish/5938.0.html

def calc_tax(income):
    tax_rate_table = ((4000000, .35),
                      (2000000, .30),
                      (1000000, .25),
                      (750000, .20),
                      (500000, .15),
                      (300000, .10),
                      (150000, .05),
                      (0, 0))
    total_tax = 0
    for bracket, tax_rate in tax_rate_table:
        if income > bracket:
            total_tax += (income - bracket) * tax_rate
            print("{:12,} {:3.0%} {:12,} {:12,.0f}"
                  .format(bracket, tax_rate, income - bracket, (income - bracket) * tax_rate))
            income = bracket
    return total_tax

if __name__ == '__main__':
    income = 2000000
    tax = calc_tax(income)
    print("income = {:,}, tax = {:10,.0f}".format(income, tax))