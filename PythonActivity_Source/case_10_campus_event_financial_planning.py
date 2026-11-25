# Case Study 10: Campus Event Financial Planning
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
transport = float(input("Transport cost: "))
catering = float(input("Catering cost per participant: "))
certificate = float(input("Certificate cost per participant: "))
planned = int(input("Planned participants: "))
sponsorship = float(input("Sponsorship: "))
fee = float(input("Registration fee per participant: "))
values = [venue, equipment, transport, catering, certificate, sponsorship, fee]
if any(x < 0 for x in values) or planned < 0:
    print("Invalid financial input")
else:
    fixed = venue + equipment + transport
    per_person = catering + certificate
    cost = fixed + planned * per_person
    funds = sponsorship + planned * fee
    balance = funds - cost
    print(f"Planned cost: {cost:.2f} | Funds: {funds:.2f} | Balance: {balance:.2f}")
    if fee <= per_person and sponsorship < fixed:
        print("Break-even cannot be reached through registrations alone")
    else:
        count = 0
        while sponsorship + count * fee < fixed + count * per_person:
            count += 1
        print(f"Minimum registrations to break even: {count}")
