def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = {}
    total_calories = 0

    for item, info in sorted_items:
        if budget >= info['cost']:
            count = budget // info['cost'] 
            budget -= count * info['cost']
            total_calories += count * info['calories']
            selected_items[item] = {'count': count, 'calories': info['calories'], 'cost': info['cost']}
    
    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

try:
    budget = int(input("Введіть бюджет (ціле число від 10): "))
    if budget < 9:
        raise ValueError()
except ValueError:
    print("Будь ласка, введіть число.")
    exit()
    
selected_items, total_calories = greedy_algorithm(items, budget)
print("Вибрані елементи:", selected_items)
print("Загальна кількість калорій:", total_calories)