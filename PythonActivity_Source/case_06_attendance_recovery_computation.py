# Case Study 6: Attendance Recovery Computation
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

held = int(input("Classes held: "))
attended = int(input("Classes attended: "))
target = float(input("Required attendance (%): "))
absences = int(input("Expected absences before attending: "))
if held <= 0 or attended < 0 or attended > held or not 0 <= target <= 100 or absences < 0:
    print("Invalid attendance data")
else:
    current = attended / held * 100
    need = 0
    while (attended + need) / (held + need) * 100 < target:
        need += 1
    scenario_total = 0
    a, h = attended, held
    while a / h * 100 < target:
        scenario_total += 1
        h += 1
        if scenario_total > absences:
            a += 1
    print(f"Current attendance: {current:.2f}%")
    print(f"Consecutive classes to attend: {need}")
    print(f"Total future classes including {absences} expected absence(s): {scenario_total}")
