def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Знаходимо середину масиву
        left_half = arr[:mid]  # Ліва половина масиву
        right_half = arr[mid:]  # Права половина масиву

        merge_sort(left_half)  # Рекурсивно сортуємо ліву половину
        merge_sort(right_half)  # Рекурсивно сортуємо праву половину

        i = j = k = 0

        # Злиття відсортованих половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Додаємо залишки лівої половини
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Додаємо залишки правої половини
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Переміщуємо елементи масиву, які більші за ключ, на одну позицію вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Вставляємо ключ на правильну позицію


def timsort(arr):
    return sorted(arr)  # Використовуємо вбудовану функцію sorted(), яка реалізує Timsort


import timeit
import random

# Генерація випадкових даних для тестування
def generate_random_list(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Вимірювання часу виконання алгоритмів
def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data.copy()), number=1)

sizes = [100, 1000, 5000, 10000]  # Розміри масивів для тестування
results = {}

for size in sizes:
    data = generate_random_list(size)  # Генерація випадкового масиву
    results[size] = {
        'Merge Sort': measure_time(merge_sort, data),  # Вимірювання часу для Merge Sort
        'Insertion Sort': measure_time(insertion_sort, data),  # Вимірювання часу для Insertion Sort
        'Timsort': measure_time(timsort, data),  # Вимірювання часу для Timsort
    }

# Виведення результатів
for size in sizes:
    print(f"Size: {size}")
    for sort_type, time_taken in results[size].items():
        print(f"{sort_type}: {time_taken:.6f} seconds")
    print()


import heapq

def merge_k_lists(lists):
    heap = []
    # Додаємо всі елементи з усіх списків у купу
    for l in lists:
        for val in l:
            heapq.heappush(heap, val)
    # Виймаємо всі елементи з купи, отримуючи відсортований список
    merged_list = [heapq.heappop(heap) for _ in range(len(heap))]
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

