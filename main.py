import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо міні-купу з початковими значеннями довжин кабелів
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
         # Витягуємо два найкоротші кабелі
        first_min_cable = heapq.heappop(cables)
        second_min_cables = heapq.heappop(cables)

         # Вартість з'єднання двох кабелів
        cost = first_min_cable + second_min_cables
        total_cost += cost

        # Додаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

cables = [8, 4, 2, 7]
print("Мінімальні витрати на об'єднання кабелів:", min_cost_to_connect_cables(cables))    
