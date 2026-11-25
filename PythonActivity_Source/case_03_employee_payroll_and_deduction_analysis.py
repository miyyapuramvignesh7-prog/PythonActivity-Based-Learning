# Case Study 3: Employee Payroll and Deduction Analysis
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

basic = float(input("Basic pay: "))
hours = float(input("Overtime hours: "))
incentive = float(input("Incentive: "))
if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid input: values must be non-negative")
else:
    hra = 0.20 * basic
    transport = 0.10 * basic
    overtime = (basic / 160) * 1.5 * hours
    gross = basic + hra + transport + overtime + incentive
    deduction = min(gross, 20000) * 0.05
    deduction += min(max(gross - 20000, 0), 20000) * 0.10
    deduction += max(gross - 40000, 0) * 0.20
    print("\nSALARY STATEMENT")
    print(f"Basic: {basic:.2f} | HRA: {hra:.2f} | Transport: {transport:.2f}")
    print(f"Overtime: {overtime:.2f} | Incentive: {incentive:.2f}")
    print(f"Gross: {gross:.2f} | Deduction: {deduction:.2f} | Net: {gross-deduction:.2f}")
