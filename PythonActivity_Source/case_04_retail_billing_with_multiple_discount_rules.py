# Case Study 4: Retail Billing with Multiple Discount Rules
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

n = int(input("Number of products: "))
items = []
subtotal = 0.0
for _ in range(n):
    name = input("Product: ")
    category = input("Category (E/G): ").upper()
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))
    if category not in ("E", "G") or price < 0 or quantity < 0:
        print("Invalid product record")
        continue
    line = price * quantity
    items.append((name, category, price, quantity, line))
    subtotal += line
discount = min(subtotal * 0.10, 1000) if subtotal >= 5000 else 0
tax_total = 0.0
print("\nITEMIZED INVOICE")
for name, category, price, quantity, line in items:
    share = (line / subtotal * discount) if subtotal else 0
    taxable = line - share
    tax = taxable * (0.18 if category == "E" else 0.05)
    tax_total += tax
    print(f"{name}: {quantity} x {price:.2f} = {line:.2f}; discount {share:.2f}; tax {tax:.2f}")
print(f"Subtotal: {subtotal:.2f} | Discount: {discount:.2f} | Tax: {tax_total:.2f} | Total: {subtotal-discount+tax_total:.2f}")
