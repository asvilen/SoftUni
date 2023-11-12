pen_packages = int(input())
marker_packages = int(input())
board_detergent_liters = int(input())
discount_rate = int(input())

pen_packages_price = 5.8
marker_packages_price = 7.2
detergent_price = 1.2
discount = 1 - discount_rate / 100
total_sum = (pen_packages_price * pen_packages + marker_packages_price * marker_packages + board_detergent_liters * detergent_price) * discount

print(total_sum)