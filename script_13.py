def is_leap_year(x):
    return ((x % 400 == 0) or (x % 4 == 0) and (x % 100 != 0))


x = 900
print(is_leap_year(x))

x = input('input number : ')
print('3' in str(x) and '7' in str(x))

try:
    age = int(input("How old are you?"))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError as error:
    print(error)
    print("Неправильный возраст")
else:
    print(f"You are {age} years old!")  # Возраст выводится только в случае, если пользователь ввёл правильный возраст.


try:
    z = input('input string of number : ')
    q = int(z)
except ValueError as error:
    print('You are input wrong number!')
else:
    print('You are input.', q)
finally:
    print('Exit the program')

print(list(range(5)))


S = 1  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 2

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S * i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)


p = int(input('input number: '))
while p < 1000:
    p **= 2

print(p)

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую сроку
    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения тоже самое
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)


list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей,
# где на первом месте стоит индекс, а затем значение
# [(0, -5), (1, 2), (2, 4), ...]
for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")


text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
print(text)

count = {}  # для подсчета символов и их количества
for char in text:
   if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[char] += 1
   else:
       count[char] = 1

for char, cnt in count.items():
   print(f"Символ {char} встречается {cnt} раз")

a = int(input())
if 100 < a < 999:
    if a % 2 == 0:
        if a % 3 == 0:
            print(f'a is satisfy all condition {a}')

if type(a) == int and 100 < a < 999 and a % 2 == 0 and a % 3 == 0:
    print(f'{a} satisfy all condition')

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")


L = list(map(int, input().split()))
print(L)
print(all(L))

List_new = list(map(int, input().split()))
print(not any(List_new))

K = [[i * j for j in range(1, 10)] for i in range(1, 10)]
print(K, sep="\n")

P = [bool(int(input()) % 2 == 0) for i in range(5)]
print(P)

h = [a * b for a, b in zip(L, K)]
print(h)


heads = 35  # количество голов
legs = 94  # количество ног

for r in range(heads + 1):  # количество кроликов
    for ph in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
        if (r + ph) > heads or \
        (r * 4 + ph * 2) > legs:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Количество кроликов", r)
            print("Количество фазанов", ph)
            print("---")