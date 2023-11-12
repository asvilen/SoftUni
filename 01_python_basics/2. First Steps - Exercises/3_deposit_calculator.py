deposited_sum = float(input())
deposit_period_in_months = int(input())
yearly_interest = float(input())

sum = deposited_sum + deposit_period_in_months * ((deposited_sum * yearly_interest / 100) / 12)

print(sum)