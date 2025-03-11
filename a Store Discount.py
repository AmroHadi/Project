# Purchase details
total_purchase = 180000

is_member = False  # Change to True if the customer is a member

# Check if the discount is applicable
if total_purchase > 200000 or is_member:
    print("Discount is applicable.")
else:
    print("Discount is not applicable.")