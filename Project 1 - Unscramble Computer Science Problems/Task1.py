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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def get_all_telephone_numbers():
    """
        Get all telephone numbers from records(text & call).
    """

    # Get All Telephone Numbers from Text Data
    # Example Single Record & Format of Text Data
    # ['97424 22395', '90365 06212', '01-09-2016 06:03:22'] -> Data
    # ['incoming_number', 'answering_number', 'Date Time'] -> Format
    text_telephone_numbers = []

    for record in texts:
        text_telephone_numbers.append(record[0])
        text_telephone_numbers.append(record[1])

    # Get All Telephone Numbers from Call Data
    # Example Single Record & Format of Call Data
    # ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'] -> Data
    # ['incoming_number', 'answering_number', 'Date Time', 'Duration'] -> Format
    call_telephone_numbers = []

    for record in calls:
        call_telephone_numbers.append(record[0])
        call_telephone_numbers.append(record[1])

    return text_telephone_numbers + call_telephone_numbers


def get_unique_telephone_numbers():
    """
        Get unique telephone numbers from records(text & call).
    """
    return list(set(get_all_telephone_numbers()))


def print_unique_telephone_numbers_count():
    """
        Prints the Count of Unique telephone numbers from all the records.
    """
    count = len(get_unique_telephone_numbers())
    message = "There are {} different telephone numbers in the records.".format(count)
    print(message)


print_unique_telephone_numbers_count()
