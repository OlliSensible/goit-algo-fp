def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    item_list = list(items.keys())
    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            cost = items[item_list[i-1]]['cost']
            calories = items[item_list[i-1]]['calories']
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]
    
    w = budget
    selected_items = {}
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            item_name = item_list[i-1]
            selected_items[item_name] = selected_items.get(item_name, 0) + 1
            w -= items[item_name]['cost']
    
    return selected_items, dp[len(items)][budget]

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

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("DP Вибрані елементи:", selected_items_dp)
print("DP Загальна кількість калорій:", total_calories_dp)