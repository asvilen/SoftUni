import sys

reading = input()

min_number = sys.maxsize

while reading != "Stop":
    reading = int(reading)
    if reading < min_number:
        min_number = reading
    reading = input()
print(min_number)