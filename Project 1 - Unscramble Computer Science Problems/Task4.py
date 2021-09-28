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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Filter TeleNumbers
incoming_numbers = set([i[0] for i in calls
                        if i[0][0] == '1' and len(i[0]) == 10])

answering_numbers = [i[1] for i in calls if i[1][0] == '1' and len(i[1]) == 10]

anwsering_msg_numbers = [i[1] for i in texts
                         if i[1][0] == '1' and len(i[1]) == 10]

incoming_msg_numbers = [i[0] for i in texts
                        if i[0][0] == '1' and len(i[0]) == 10]

# The numbers who  have sent/recieved messages and \
# recieved call were not telecallers
invalid_set = set(answering_numbers + incoming_msg_numbers
                  + anwsering_msg_numbers)

valid_telenumber = sorted([i for i in incoming_numbers
                           if i not in invalid_set])

print("These numbers could be telemarketers: ")

for i in valid_telenumber:
    print(i)
