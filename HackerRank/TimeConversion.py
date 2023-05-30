"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

def timeConversion(s):
    components = s.split(":")

    if components[0] == "12" and components[-1].endswith("AM"):
        components[0] = 0
    elif components[0] != "12" and components[-1].endswith("PM"):
        components[0] = int(components[0]) + 12

    return f"{components[0]}:{components[1]}:{components[2][:2]}"


# print(timeConversion("07:05:45PM")) # 19:05:45
print(timeConversion("12:05:45AM")) # 00:05:45
# print(timeConversion("07:05:45PM")) # 19:05:45
