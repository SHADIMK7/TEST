def discount(cart_total, quantity, gift_wrap_count):
    flat_10 = 10 if cart_total > 200 else 0
    bulk_5 = max([0.05 * quantity[i] * price[i] for i in range(len(price)) if quantity[i] > 10], default=0)
    bulk_10 = 0.1 * cart_total if sum(quantity) > 20 else 0
    tiered_50 = 0.5 * sum([price[i] * (quantity[i] - 15) for i in range(len(price)) if quantity[i] > 15])

    discount = {
        "flat_10_discount": flat_10,
        "bulk_5_discount": bulk_5,
        "bulk_10_discount": bulk_10,
        "tiered_50_discount": tiered_50
    }

    applicable_discount = max(discount, key=discount.get)
    discount_amount = discount[applicable_discount]

    return applicable_discount, discount_amount


def shipping_fee(quantity):
    return sum(quantity) // 10 * 5


def gift_wrap_fee(gift_wrap_count):
    return sum(gift_wrap_count)


def receipt(product_names, quantity, price, gift_wrap_count):
    cart_total = sum([quantity[i] * price[i] for i in range(len(price))])
    discount_name, discount_amount = discount(cart_total, quantity, gift_wrap_count)
    shipping_fee = shipping_fee(quantity)
    gift_wrap_fee = gift_wrap_fee(gift_wrap_count)
    total = cart_total - discount_amount + shipping_fee + gift_wrap_fee

    print("Receipt:")
    for i in range(len(product_names)):
        print(f"{product_names[i]} - Quantity: {quantity[i]}, Total: ${quantity[i] * price[i]}")

    print("\nSubtotal: $", cart_total)
    print(f"Discount Applied ({discount_name}): ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print("\nTotal: $", total)


product_names = ["Product A", "Product B", "Product C"]
price = [20, 40, 50]

quantity = [int(input(f"Enter quantity for {product}: ")) for product in product_names]
gift_wrap_count = [int(input(f"Is {product} wrapped as a gift? (Enter 0 for no, 1 for yes): ")) for product in product_names]

receipt(product_names, quantity, price, gift_wrap_count)
