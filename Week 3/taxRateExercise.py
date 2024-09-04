# Write a python program that calculates the taxes for a product
# price <= 100 = 3% tax
# 100 < price <= 1000 = 5% tax
# 1000 < price <= 10,000 = 7% tax
# price > 10,000 = 9% tax rate

cost = float(input("Enter price of product: $"))
tax_rate = 0

if cost <= 100:
    tax_rate = 0.03
elif cost <= 1_000:
    tax_rate = 0.05
elif cost <= 10_000:
    tax_rate = 0.07
else:
    tax_rate = 0.09

tax_amount = round(cost * tax_rate, 2)
total_cost = round(cost + tax_amount, 2)
print("Total cost is $" + str(total_cost) + " with $" + str(tax_amount) + " in tax.")