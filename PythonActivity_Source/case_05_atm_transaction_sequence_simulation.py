# Case Study 5: ATM Transaction Sequence Simulation
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

balance = float(input("Opening balance: "))
n = int(input("Number of transactions: "))
accepted = rejected = 0
for _ in range(n):
    kind = input("Transaction (D/W): ").upper()
    amount = float(input("Amount: "))
    if amount <= 0:
        ok = False
    elif kind == "D":
        balance += amount
        ok = True
    elif kind == "W" and amount <= 10000 and amount <= balance:
        balance -= amount
        ok = True
    else:
        ok = False
    if ok:
        accepted += 1
        print(f"Accepted. Balance: {balance:.2f}")
    else:
        rejected += 1
        print(f"Rejected. Balance unchanged: {balance:.2f}")
print(f"Summary: accepted={accepted}, rejected={rejected}, final balance={balance:.2f}")
