# Case Study 1: University Scholarship Allocation
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

n = int(input("Number of applicants: "))
quota = int(input("Scholarship quota: "))
eligible = []
for _ in range(n):
    name = input("Name: ")
    aggregate = float(input("Aggregate (%): "))
    subject = float(input("Minimum subject mark (%): "))
    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income: "))
    qualified = aggregate >= 80 and subject >= 60 and attendance >= 75 and income <= 300000
    if qualified:
        eligible.append((name, aggregate, attendance))
eligible.sort(key=lambda item: (-item[1], -item[2], item[0].lower()))
print("\nEligible candidates (ranked):")
if not eligible:
    print("No eligible candidates")
for rank, item in enumerate(eligible, 1):
    name, aggregate, attendance = item
    award = "AWARDED" if rank <= quota else "WAITLIST"
    print(f"{rank}. {name} | {aggregate:.1f}% | attendance {attendance:.1f}% | {award}")
