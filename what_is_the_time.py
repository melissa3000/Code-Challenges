"""Peter can see a clock in the mirror from the place he sits in the office.
When he saw the clock shows 12:22

He knows that the time is 11:38

in the same manner:

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

Please complete the method which is provided with mirror time as string, and
return the real time as string.

The return time value should always be between 1<= time < 13. This is the
convenient way that human read the clock.

"""

def what_is_the_time(time_in_mirror):

    converter = {"01": "10", "02": "09", "03": "08", "04": "07", "05": "06",
                "06": "05", "07": "04", "08": "03", "09": "02", "10": "01",
                "11": "12", "12": "11"}
    even_hour = {"12": "12", "01": "11", "02": "10", "03": "09", "04": "08",
                "05": "07", "06": "06", "07": "05", "08": "04", "09": "03",
                "10": "02", "11": "01"}

    hours, minutes = time_in_mirror.split(':')

    minutes = int(minutes)

    if minutes == 00:
        new_minutes = 00
        new_hour = even_hour.get(hours)
    else:
        new_minutes = 60 - minutes

        new_hour = converter.get(hours)

    new_time = ""

    new_time = new_hour + ":" + str(new_minutes).zfill(2)

    print new_time



what_is_the_time("06:35") #==> "05:25", "didn't work for '06:35'")
what_is_the_time("11:59") #==> "12:01", "didn't work for '11:59'")
what_is_the_time("12:02") #==> "11:58", "didn't work for '12:02'")
what_is_the_time("04:00") #==> "08:00", "didn't work for '04:00'")
what_is_the_time("06:00") #==> "06:00", "didn't work for '06:00'")
what_is_the_time("12:00") #==> "12:00", "didn't work for '12:00'")




