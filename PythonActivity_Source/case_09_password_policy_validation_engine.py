# Case Study 9: Password Policy Validation Engine
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

password = input("Password: ")
failures = []
if len(password) < 8:
    failures.append("at least 8 characters")
if not any(ch.isupper() for ch in password):
    failures.append("at least one uppercase letter")
if not any(ch.islower() for ch in password):
    failures.append("at least one lowercase letter")
if not any(ch.isdigit() for ch in password):
    failures.append("at least one digit")
if not any(ch in "!@#$" for ch in password):
    failures.append("at least one special character from !@#$")
if any(password[i] == password[i+1] == password[i+2] for i in range(len(password)-2)):
    failures.append("no three identical consecutive characters")
if "password" in password.lower():
    failures.append("must not contain the word 'password'")
if failures:
    print("Invalid password. Failed rules:")
    for rule in failures:
        print("- " + rule)
else:
    print("Password is valid")
