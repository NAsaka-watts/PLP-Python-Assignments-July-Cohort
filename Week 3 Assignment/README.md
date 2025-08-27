# Discount Calculator Assignment 🛒

## Overview
This project demonstrates a simple **Python function** that calculates the final price of an item after applying a discount.  
It includes:

- Function creation
- Parameter handling
- Conditional statements
- User input and output

---

## Function: `calculate_discount(price, discount_percent)`

### Purpose
Calculates the **final price** based on the discount percentage.  

### Logic
- If the discount is **20% or higher**, the function applies the discount to the original price.
- Otherwise, the function returns the **original price** without any change.

### Example Implementation
```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Example usage
price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

final_price = calculate_discount(price, discount)
print(f"Final price: {final_price}")
