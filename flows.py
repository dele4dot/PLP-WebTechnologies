def calculate_discount(original_price, discount_percent):
    """
    Calculates the final price after applying a discount.
    - If discount is 20% or more, applies the discount
    - Otherwise, keeps the original price
    """
    if discount_percent >= 20:  # Only apply if discount is 20% or more
        # Calculate discount amount (like how much money you're saving)
        money_saved = original_price * (discount_percent / 100)
        # Calculate final price after discount
        final_price = original_price - money_saved
        return final_price
    else:
        # No discount applied, return original price
        return original_price

# Main part of the program - like the checkout process
print("Welcome to the Supermarket Discount Calculator!")
print("---------------------------------------------")

# Get input from customer (like scanning an item)
item_price = float(input("Enter the original price of the item: $"))
discount_offered = float(input("Enter the discount percentage (0-100): "))

# Calculate the final price using our function
payable_amount = calculate_discount(item_price, discount_offered)

# Display the result to the customer
if discount_offered >= 20:
    print(f"\nCongratulations! You saved {discount_offered}%!")
    print(f"Original price: ${item_price:.2f}")
    print(f"Your final price: ${payable_amount:.2f}")
else:
    print(f"\nNo discount applied (needs to be 20% or more).")
    print(f"Your price: ${payable_amount:.2f}")
