"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def print_message_a():
    """
		Prints List all area code who got call from bangalore
    """
    prefixs = set([get_the_prefix_code(i[1]) for i in filter_callers_with_area_code()])
    
    print("The numbers called by people in Bangalore have codes:")
    
    for i in sorted(prefixs):
        print(i)


def print_message_b():
    """
		Prints the percentage of fixed line calls made from
		Bangalore to fixed lines in Bangalore.
	"""
    return None


def get_the_prefix_code(number):
    """
		Returns the area code / Mobile Prefix 
  		of given phone number(if valid).
    """
    if number[0] == "(" and ")" in number and number[1] == '0':
        return number[1:number.index(')')]
    elif number[0] in ['7', '8', '9']:
        return number[:4]
    elif number[0] == '1' and len(number) == 10:
        return number[:3]
    else:
        return -1


def filter_callers_with_area_code(area_code='080'):
    """
		Return's all records, In which the call initiated
		with given area_code
    """
    filtered_data = []
    
    for record in calls:
        if area_code == get_the_prefix_code(record[0]):
            filtered_data.append(record)
            
    return filtered_data[:]



print_message_a()