# Case Study 2: Progressive Electricity Billing
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

n = int(input("Number of months: "))
previous = None
for _ in range(n):
    month = input("Month: ")
    units = float(input("Units consumed: "))
    if units < 0:
        print("Invalid units")
        continue
    first = min(units, 100) * 2
    second = min(max(units - 100, 0), 100) * 3
    third = max(units - 200, 0) * 5
    energy = first + second + third
    if units <= 50:
        adjustment = -0.05 * energy
    elif energy > 500:
        adjustment = 0.10 * energy
    else:
        adjustment = 0
    bill = energy + adjustment + 50
    flag = " | UNUSUAL INCREASE" if previous is not None and bill > 1.5 * previous else ""
    print(f"{month}: energy={energy:.2f}, adjustment={adjustment:.2f}, fixed=50.00, total={bill:.2f}{flag}")
    previous = bill
