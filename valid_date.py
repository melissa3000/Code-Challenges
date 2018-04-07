# Your task is to write a regular expression (regex) that will match a string only if it contains at least one valid date, in the format [mm-dd] (that is, a two-digit month, followed by a dash, followed by a two-digit date, surrounded by square brackets).

# You should assume the year in question is not a leap year. Therefore, the number of days each month should have are as follows:

# 1. January - 31 days
# 2. February - 28 days (leap years are ignored)
# 3. March - 31 days
# 4. April - 30 days
# 5. May - 31 days
# 6. June - 30 days
# 7. July - 31 days
# 8. August - 31 days
# 9. September - 30 days
# 10. October - 31 days
# 11. November - 30 days
# 12. December - 31 days
# All text outside a valid date can be ignored, including other invalid dates.

# "[01-23]" // January 23rd is a valid date
# "[02-31]" // February 31st is an invalid date
# "[02-16]" // valid
# "[ 6-03]" // invalid format
# "ignored [08-11] ignored" // valid
# "[3] [12-04] [09-tenth]" // December 4th is a valid date

import re

validation = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 31,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

word_ending = {
    "0": "th",
    "1": "st",
    "2": "nd",
    "3": "rd",
    "4": "th",
    "5": "th",
    "6": "th",
    "7": "th",
    "8": "th",
    "9": "th",
}

def valid_date(str):

    match_obj = re.search(r"\[\d\d\-\d\d\]", str)

    if match_obj == None:
        return "invalid format"
    else:
        date = match_obj.group()

    month = date[1:3]
    days = date[4:6]

    # Invalidate if not an actual month
    month_word = months.get(month, 0)
    if month_word == 0:
        return "invalid format"

    # Invalidate if too many days for the month
    valid_days = validation.get(month_word, 0)
    if int(days) > valid_days:
        return "invalid format"

    word_end = word_ending.get(days[1], 0)

    result = month_word + " " + days + word_end + " " + "is a valid date"
    print result


valid_date("[01-23]")






# collect_date("ignored [08-11] ignored")






