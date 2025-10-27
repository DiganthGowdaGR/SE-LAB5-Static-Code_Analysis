"""
Inventory Management System

A simple inventory management system that provides functionality to add,
remove, and track items in stock. Includes data persistence through JSON files.
"""

import json
import logging
from datetime import datetime

# Global variable for storing inventory data
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add items to the inventory.

    Args:
        item (str): Name of the item to add
        qty (int): Quantity to add
        logs (list): Optional list to store operation logs

    Returns:
        None
    """
    if logs is None:
        logs = []

    # Input validation
    if not item or not isinstance(item, str):
        logging.warning("Invalid item name provided")
        return
    
    if not isinstance(qty, int):
        logging.warning("Invalid quantity type provided")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info(f"Added {qty} of {item} to inventory")


def remove_item(item, qty):
    """
    Remove items from the inventory.

    Args:
        item (str): Name of the item to remove
        qty (int): Quantity to remove

    Returns:
        None
    """
    # Input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for remove_item")
        return
    
    if qty <= 0:
        logging.warning("Quantity must be positive")
        return
    
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info(f"Removed {qty} of {item} from inventory")
    except KeyError:
        logging.warning(f"Item '{item}' not found in inventory")


def get_qty(item):
    """
    Get the quantity of a specific item.

    Args:
        item (str): Name of the item

    Returns:
        int: Quantity of the item in stock
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file (str): Path to the JSON file

    Returns:
        None
    """
    global stock_data
    with open(file, "r", encoding='utf-8') as f:
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file (str): Path to the JSON file

    Returns:
        None
    """
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))


def print_data():
    """
    Print a report of all items in inventory.

    Returns:
        None
    """
    print("Items Report")
    for item in stock_data:
        print(f"{item} -> {stock_data[item]}")


def check_low_items(threshold=5):
    """
    Check for items with low stock levels.

    Args:
        threshold (int): Minimum quantity threshold

    Returns:
        list: List of items below the threshold
    """
    result = []
    for item in stock_data:
        if stock_data[item] < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate inventory system functionality.

    Returns:
        None
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    logging.info("Starting inventory system")
    
    add_item("apple", 10)
    add_item("banana", -2)
    # Test input validation
    add_item(123, "ten")  # This will now be handled gracefully
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    # Removed dangerous eval() call
    print("System operations completed safely")
    logging.info("Inventory system operations completed")


if __name__ == "__main__":
    main()