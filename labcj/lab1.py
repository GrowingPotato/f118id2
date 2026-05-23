import math

def calculate_entropy(probabilities):
    """Считает энтропию H по формуле Шеннона."""
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def shannon_fano_recursive(chars_with_probs):
    """
    Рекурсивный алгоритм разбиения Шеннона-Фано.
    Принимает список кортежей [ (символ, вероятность), ... ]
    """
    if len(chars_with_probs) <= 1:
        return {chars_with_probs[0][0]: ""} if chars_with_probs else {}

    # Поиск точки наиболее равного разделения суммы вероятностей
    total_p = sum(item[1] for item in chars_with_probs)
    acc_p = 0
    split_idx = 0
    min_diff = total_p

    for i, (_, p) in enumerate(chars_with_probs):
        acc_p += p
        diff = abs((total_p - acc_p) - acc_p)
        if diff < min_diff:
            min_diff = diff
            split_idx = i + 1
        else:
            break

    # Рекурсивно добавляем 0 левой части и 1 правой
    left_part = chars_with_probs[:split_idx]
    right_part = chars_with_probs[split_idx:]

    codes = {}
    for char, _ in left_part:
        codes[char] = "0"
    for char, _ in right_part:
        codes[char] = "1"

    # Слияние кодов из вложенных разбиений
    left_codes = shannon_fano_recursive(left_part)
    right_codes = shannon_fano_recursive(right_part)

    for char in codes:
        if char in left_codes:
            codes[char] += left_codes[char]
        elif char in right_codes:
            codes[char] += right_codes[char]

    return codes

def main():
    # 1) Ввод данных
    print("--- Проект: Кодирование Шеннона-Фано ---")
    data_student = input("Введите ФИО и дату студента: ")
    data_family = input("Введите данные членов семьи: ")
    message = data_student + data_family
    n = len(message)

    # 2) Подсчет частот и вероятностей
    frequencies = {}
    for char in message:
        frequencies[char] = frequencies.get(char, 0) + 1

    # Сортировка по убыванию частоты (важно для Шеннона-Фано)
    sorted_chars = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    chars_probs = [(char, f / n) for char, f in sorted_chars]

    # Проверка суммы вероятностей
    sum_p = sum(p for _, p in chars_probs)
    print(f"\nДлина сообщения: {n} символов")
    print(f"Проверка: Σp = {sum_p:.6f} ≈ 1")

    # 3) Построение кодов
    codes = shannon_fano_recursive(chars_probs)

    # 4) Вывод таблицы результатов
    print(f"\n{'Символ':<10} | {'fᵢ':<4} | {'pᵢ':<8} | {'Код':<10} | {'lᵢ'}")
    print("-" * 50)
    
    total_b = 0
    l_average = 0
    for char, p in chars_probs:
        code = codes[char]
        li = len(code)
        fi = frequencies[char]
        total_b += fi * li
        l_average += p * li
        # Для наглядности отображаем пробел
        disp_char = f"'{char}'" if char != " " else "'space'"
        print(f"{disp_char:<10} | {fi:<4} | {p:<8.4f} | {code:<10} | {li}")

    # 5) Расчет метрик
    h = calculate_entropy([p for _, p in chars_probs])
    eta = h / l_average
    r = 1 - eta

    # Равномерный код
    alphabet_size = len(frequencies)
    l_uniform = math.ceil(math.log2(alphabet_size))
    b_uniform = n * l_uniform

    # 6) Сравнение и итоги
    print("\n" + "="*30)
    print(f"{'Метрика':<20} | {'Шеннон-Фано':<12} | {'Равномерный'}")
    print("-" * 50)
    print(f"{'Общий объём B (бит)':<20} | {total_b:<12} | {b_uniform}")
    print(f"{'Ср. длина L (бит)':<20} | {l_average:<12.3f} | {l_uniform}")
    print(f"{'Энтропия H':<20} | {h:<12.3f} | -")
    print(f"{'Эффективность η':<20} | {eta:<12.3f} | {h/l_uniform:.3f}")
    print(f"{'Избыточность r':<20} | {r:<12.3f} | {1-(h/l_uniform):.3f}")
    print("="*30)

if __name__ == "__main__":
    main()

