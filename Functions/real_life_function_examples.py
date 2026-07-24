


def calculate_discounted_price(original_price, discount_percent):
    discount_amount = (original_price * discount_percent) / 100
    return original_price - discount_amount


def calculate_total_with_tax(price, tax_percent):
    tax_amount = (price * tax_percent) / 100
    return price + tax_amount


def print_receipt(item_name, quantity, unit_price):
    total_price = quantity * unit_price
    print("Receipt")
    print("Item:", item_name)
    print("Quantity:", quantity)
    print("Unit price:", unit_price)
    print("Total:", total_price)


def show_real_life_examples():
    discounted = calculate_discounted_price(1000, 10)
    taxed = calculate_total_with_tax(500, 5)

    print("Discounted price:", discounted)
    print("Price after tax:", taxed)
    print_receipt("Notebook", 3, 50)


if __name__ == "__main__":
    show_real_life_examples()
