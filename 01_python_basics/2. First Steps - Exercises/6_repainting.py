plastic_bags_qbm = int(input())
paint_liters = int(input())
dilutor_liters = int(input())
hours_of_work = int(input())

plastic_bags_price = 1.5
paint_price = 14.5
dilutor_price = 5
bags = 0.4
paint_liters += paint_liters * 0.1
plastic_bags_qbm += 2

total_material_expenses = plastic_bags_qbm * plastic_bags_price + paint_liters * paint_price + dilutor_liters * dilutor_price + bags
work_expenses_per_hour = total_material_expenses * 0.3
total_expenses = total_material_expenses + work_expenses_per_hour * hours_of_work

print(total_expenses)