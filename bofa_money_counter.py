# usr/bin/env python3
# Author: Ernest Jinian
import re
import collections

def read_contents(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print('File Error! bofa.txt is not in the same directory as this script')
        return
    text = file.read()
    
    # regex to find all dollar amounts
    dollars = re.findall('[-+]?\$\d{1,3}(?:,\d{3})*\.\d{2}', text)

    # regex to find all names
    names = re.findall('Zelle Transfer Conf# [\d\w]+; (.+)', text)

    # variables
    total_pos = 0
    total_neg = 0
    amount_pos_transactions = 0
    amount_neg_transactions = 0
    names = collections.Counter(names)

    # looping through each dollar amount
    for dollar_amount in dollars:
        dollar_amount = dollar_amount.replace("$", "")
        dollar_amount = dollar_amount.replace(",", "")
        if float(dollar_amount) > 0:
            total_pos += float(dollar_amount)
            amount_pos_transactions += 1
        else:
            total_neg += float(dollar_amount)
            amount_neg_transactions += 1
    
    total = total_pos + total_neg
    total = "{:,.2f}".format(total)

    # truncate total_pos and total_neg to 2 decimal places
    total_pos = "{:,.2f}".format(total_pos)
    total_neg = "{:,.2f}".format(abs(total_neg))

    # format the counter object    
    res_str = "\b"
    for pair in names.most_common():
        res_str += pair[0] + " has " + str(pair[1]) + " transaction(s) with you\n"
    
    print('Total amount of positive transactions:', str(amount_pos_transactions) + " (Received a total of $" + str(total_pos) + ")")
    print('Total amount of negative transactions:', str(amount_neg_transactions) + " (Sent a total of $" + str(total_neg) + ")\n")
    print('People in the file:\n', res_str if len(names) > 0 else 'No names found')
    print('Net profit:', '$' + str(total))
    file.close()

def main():
    read_contents('bofa.txt')

main()
