"""
Problem: Inventory Matching and Pricing
Approach: Sort items by price ascending, fulfill order greedily.
"""
def fulfill_order(inventory, order, budget):
    sorted_items = sorted(inventory.items(), key=lambda x: x[1]['price'])
    fulfilled = {}
    remaining_budget = budget
    
    for item, qty in order.items():
        available = inventory.get(item, {}).get('quantity', 0)
        price = inventory.get(item, {}).get('price', float('inf'))
        
        max_qty = min(qty, available, remaining_budget // price)
        if max_qty > 0:
            fulfilled[item] = max_qty
            remaining_budget -= max_qty * price
            
    if sum(fulfilled.values()) == sum(order.values()):
        return "Fulfilled", fulfilled
    elif fulfilled:
        return "Partially Fulfilled", fulfilled
    else:
        return "Impossible", {}

# Example usage:
if __name__ == "__main__":
    inventory = {
        'apple': {'quantity': 50, 'price': 1.5},
        'banana': {'quantity': 30, 'price': 2.0}
    }
    order = {'apple': 40, 'banana': 20}
    status, result = fulfill_order(inventory, order, 100)
    print(f"Order status: {status}")
    print("Fulfilled items:", result)