import sys

reading = input()

max_number = - sys.maxsize

while reading != "Stop":
    reading = int(reading)
    if reading > max_number:
        max_number = reading
    reading = input()
print(max_number)