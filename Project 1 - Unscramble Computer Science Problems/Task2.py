"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""


def filter_calls(month=9, year=2016):
    """
        Filter's the call records based on month & year.
    """

    # Validate Month & Year
    assert type(month) == int and (month > 0 and month <= 12)
    assert type(year) == int and (year/1000 >= 1 and year/1000 <= 10)

    # Convert Month & Year to String Format
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    year = str(year)

    # Example Single Record & Format of Call Data
    # ['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'] -> Data
    # ['incoming_number', 'answering_number', 'Date Time', 'Duration'] -> Format

    filtered_records = []

    # Loop through each record and filter based on month & year
    for record in calls:
        r_day, r_month, r_year = record[2].split(" ")[0].split("-")
        if r_month == month and r_year == year:
            filtered_records.append(record)

    return filtered_records[:]


def get_telephone_numbers_duration():
    """
        Returns: Dict of Duration of every number.
        By Aggregating the duration of each telephone number.
    """

    # Get the Filtered Call Data
    data = filter_calls()

    durations = dict()

    for record in data:
        durations[record[0]] = durations.get(record[0], 0) + int(record[-1])
        durations[record[1]] = durations.get(record[1], 0) + int(record[-1])

    return durations


def get_telephone_numbers_max_duration():
    """
        Return's the Telephone Number and Duration tuple
        having maximum duration.
    """

    telephone = ""
    duration = 0

    duration_dict = get_telephone_numbers_duration()

    # Loop through records and get the maximum
    for r_telephone in duration_dict:
        r_duration = duration_dict[r_telephone]
        if r_duration > duration:
            telephone = r_telephone
            duration = r_duration

    return (telephone, duration)


def print_message():
    """
        Prints the longest phone user and usage duration in september 2016.
    """

    telephone_number, duration = get_telephone_numbers_max_duration()
    message = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
                telephone_number, duration)
    print(message)


print_message()
