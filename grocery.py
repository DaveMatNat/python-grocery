# Designing my Grocery Inventory

INVENTORY = {
    "milk": 2.99,
    "yogurt": 3.49,
    "cheese": 4.49,
    "butter": 3.99,
    "beef": 6.99,
    "tofu": 2.79,
    "potato": 1.99,
    "peanut": 1.49,
    "broccoli": 2.49,
    "ketchup": 2.99,
    "gum": 1.29,
    "chips": 3.49,
    "popcorn": 2.49,
    "egg": 2.59,
    "bread": 1.99,
    "mango": 1.49,
    "peanut butter": 3.22
}

# -----  CHECKOUT FUNCTIONS  ----- #
# WRITE YOUR CODE BELOW #   
def clerk_checkout(total, cart):
    """
    processes an item at a time by letting the user input each item name
    prints sub totals every iteration
    update cart & return total rounded to two decimal places
    """
    while True:
        usr_input = str(input("> ")).strip()
        if usr_input == "END CART":
            break
        elif usr_input.lower() in INVENTORY.keys():
            if usr_input.lower() in cart:
                cart[usr_input.lower()] += 1
            else:
                cart[usr_input.lower()] = 1
            total += INVENTORY[usr_input.lower()]
            print(f"Subtotal: ${total:.2f}")
    return total

def express_checkout(total, cart):
    """
    processes multiple items all at once (up to max --> 10) by letting the user-
    -input comma-separated items
    update cart & return total rounded to two decimal places
    """
    max = 10
    usr_input = str(input("> ")).lower().split(",")
    for count, item in enumerate(usr_input):
        item = item.strip()
        if item in INVENTORY.keys():
            if count == max:
                break
            if item in cart:
                cart[item] += 1
            else:
                cart[item] = 1
            total += INVENTORY[item]
    return total

def print_receipt(total, cart):
    """
    Prints the receipt with the list of items, 
    their quantities, and prices per item.
    """
    print("\n--- RECEIPT ---")
    for k, v in cart.items():
        print(f"{k.ljust(max_length(cart.keys()))}\t {v}\t ${INVENTORY[k]}")
    print(f"TOTAL: ${total:.2f}")
    return

def max_length(lst):
    """
    returns the length of the longest string in the given list 
    (used for ljust referrenced in the print_receipt function)
    """
    max = ""
    for i in lst:
        if len(i) > len(max):
            max = i
    return len(max)

# MAIN CODE
def main():
    """
    main function handle user's input for selecting a checkout method and calling them
    """
    TOTAL = 0
    cart = {}
    usr_input = input("Which method would you like to checkout with? [clerk or express]: ")
    if usr_input == "clerk":
        TOTAL = clerk_checkout(TOTAL,cart)
    # example of items for 10 limit, strip, and formatting test: "egg,egg,egg,milk,milks,milked,butter,cheese,tofu,  egg,bread,paprika,pizza,basil, mango, egg, egg, egg, popcorn, peanut"
    elif usr_input == "express":
        TOTAL = express_checkout(TOTAL,cart)
    else:
        return print("INVALID CHECKOUT METHOD.")
    print_receipt(TOTAL,cart)

# calls the main function
if __name__ == "__main__":
    main()