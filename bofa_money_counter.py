# usr/bin/env python3
# Author: Ernest Jinian
import re

def read_contents(filename):
    file = open(filename, 'r')
    text = file.read()
    x = re.findall('\d+\.\d+', text)
    total_money = 0
    amount_transactions = 0
    for dollar_amount in x:
        amount_transactions += 1
        total_money += float(dollar_amount)
    print('Total amount of transactions:', amount_transactions)
    print('Net profit:', '$' + str(total_money))
    file.close()

def main():
    read_contents('bofa.txt')

main()