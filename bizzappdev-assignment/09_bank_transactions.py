"""
Problem: Bank Transaction Analyzer
Approach: Track transactions and balance incrementally.
"""
transactions = []

while True:
    trans = input("Enter transaction (e.g., +500 or -200), or 'done': ")
    if trans.lower() == 'done':
        break
    try:
        amount = int(trans)
        transactions.append(amount)
        balance = sum(transactions)
        print(f"New balance: {balance}")
    except:
        print("Invalid input")

print("\nFinal Summary:")
print("Transactions:", transactions)
print("Final balance:", sum(transactions))