number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

chicken_menu = 10.35
fish_menu = 12.4
vegetarian_menu = 8.15
delivery_cost = 2.5
total_minus_desert = number_of_chicken_menus * chicken_menu + number_of_fish_menus * fish_menu + number_of_vegetarian_menus * vegetarian_menu
desert = total_minus_desert * 0.2
order_total = total_minus_desert + desert + delivery_cost

print(order_total)