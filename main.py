def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for inputs
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

print("Final price:", final_price)