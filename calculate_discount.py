# Function to calculate discount and final price
def calculate_discount():
# Get user input for original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
# Calculate discount amount
discount_amount = (original_price * discount_percentage) / 100
# Calculate the final price after applying discount
final_price = original_price - discount_amount
# Display the results
print("Original Price: ", original_price)
print("Discount Amount: ", discount_amount)
print("Final Price: ", final_price)
# Run the discount
calculate_discount()