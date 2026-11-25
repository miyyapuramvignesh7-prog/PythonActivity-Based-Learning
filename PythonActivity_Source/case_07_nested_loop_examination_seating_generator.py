# Case Study 7: Nested Loop Examination Seating Generator
# Student: Miyyapuram Vignesh | NIAT ID: N26V01A0197 | NRI ID: 26000633

rows = int(input("Rows: "))
cols = int(input("Columns: "))
reserved_count = int(input("Reserved seat count: "))
reserved = []
for _ in range(reserved_count):
    r = int(input("Reserved row (1-based): "))
    c = int(input("Reserved column (1-based): "))
    reserved.append((r - 1, c - 1))
students = input("Roll numbers separated by spaces: ").split()
grid = [["." for _ in range(cols)] for _ in range(rows)]
for r in range(rows):
    for c in range(cols):
        if (r + c) % 2 == 0:
            grid[r][c] = "X"
for r, c in reserved:
    if 0 <= r < rows and 0 <= c < cols:
        grid[r][c] = "R"
available = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "."]
if len(students) > len(available):
    print(f"Capacity error: {len(available)} available seats for {len(students)} students")
else:
    for roll, (r, c) in zip(students, available):
        grid[r][c] = roll
    print("Seating grid (X=blocked, R=reserved, .=vacant):")
    for r, line in enumerate(grid, 1):
        print(f"Row {r}: " + " | ".join(line))
    print(f"Assigned: {len(students)} | Vacant allowed seats: {len(available)-len(students)}")
