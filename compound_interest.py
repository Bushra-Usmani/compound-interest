principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle amount: "))
    if principle < 0:
        print("Principle amount cannot be negative or zero.")
    else:
        break

while True:
    rate = float(input("Enter rate of interest: "))
    if rate < 0:
        print("Rate of interest cannot be negative or zero.")
    else:
        break

while True:
    time = int(input("Enter number of years: "))
    if time < 0:
        print("Time cannot be negative or zero.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s is ${total:,.2f}")
