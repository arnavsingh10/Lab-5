import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to the stock data."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid item or quantity type.")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Remove quantity of an item from stock data."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock data.")

def get_qty(item):
    """Return the quantity of the given item."""
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load stock data from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print("Data file not found. Starting with empty stock data.")

def save_data(file="inventory.json"):
    """Save stock data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)

def print_data():
    """Print all items in stock."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

def check_low_items(threshold=5):
    """Return list of items below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]

def main():
    """Main function for basic testing."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("orange", 5)
    remove_item("apple", 3)
    remove_item("grape", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
