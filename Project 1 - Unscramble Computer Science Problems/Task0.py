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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def print_text_record(index=0):
    """
        Prints the text message record for the given index
    """
    assert type(index) == int
    record = texts[index]

    # Example Single Record & Format of Text Data
    # ['97424 22395', '90365 06212', '01-09-2016 06:03:22'] -> Data
    # ['incoming_number', 'answering_number', 'Date Time'] -> Format

    incoming_number = record[0]
    answering_number = record[1]
    time_stamp = record[2]
    date, time = time_stamp.split(" ")

    print("First record of texts, {} texts {} at time {}".
          format(incoming_number, answering_number, time)
          )


def print_call_record(index=-1):
    """
        Prints the call data record for the given index
    """
    assert type(index) == int
    record = calls[index]

    # Example Single Record & Format of Call Data
    # ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'] -> Data
    # ['incoming_number', 'answering_number', 'Date Time', 'Duration'] -> Format

    incoming_number = record[0]
    answering_number = record[1]
    time_stamp = record[2]
    date, time = time_stamp.split(" ")
    duration = record[3]

    print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
          .format(incoming_number,
                  answering_number,
                  time,
                  duration
                  )
          )


print_text_record()
print_call_record()
