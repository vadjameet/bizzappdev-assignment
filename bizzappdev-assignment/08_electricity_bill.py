"""
Problem: Electricity Bill Calculation
Approach: Calculate slab-wise charges.
"""
def calculate_bill(units):
    slabs = [
        (0, 100, 5),
        (101, 300, 7),
        (301, 500, 10),
        (501, float('inf'), 15)
    ]
    total = 0
    breakdown = []
    
    for start, end, rate in slabs:
        if units <= 0:
            break
        slab_units = min(end, units) - start + 1 if start <= units else 0
        if slab_units <= 0:
            continue
        cost = slab_units * rate
        breakdown.append(f"{start}-{end if end != float('inf') else ''} units @ ${rate}/unit = ${cost}")
        total += cost
        units -= slab_units
    
    print("Electricity Bill:")
    print('\n'.join(breakdown))
    print(f"Total Amount Payable = ${total}")

# Example usage:
calculate_bill(450)