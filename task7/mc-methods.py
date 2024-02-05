import random
from prettytable import PrettyTable

num_simulations = 1000000

sum_count = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    sum_count[total] += 1

probabilities = {k: v / num_simulations * 100 for k, v in sum_count.items()}

table = PrettyTable()
table.field_names = ["Сума", "Імовірність"]

for k, v in probabilities.items():
    table.add_row([k, f"{v:.2f}% ({sum_count[k]}/{num_simulations})"])

print(table)