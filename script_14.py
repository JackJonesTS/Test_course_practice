import time

def print_a_add_b(a, b):
    print(a + b)

# объявили функцию для подсчета количества символов в неком абстрактном тексте


def char_frequency(text):
   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчета символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")


def del_find(a, n):
    if a % n == 0:
        print(f'{n} delitel for {a}')
    else:
        print(f'{n} not delitel for {a}')


def get_multipliers(a):
   count = 0
   for n in range(1, a + 1):
       if a % n == 0:
           count += 1

   return count


def check_polindrome(text):
    text = text.lower
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    if text == text[::-1]:
        return True
    else:
        return False


a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)


a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)


print(a)
print(*a)

def multiplication(*num):
    multip = 1
    for i in num:
        multip *= i
        print(multip)
    
    return multip

print(multiplication(5))
print(multiplication(4, 6, 6, 65, 7))
print(multiplication(54, 87, 89))

def fib():
    a, b = 0, 1
    yield a  # F0
    yield b  # F1

    while True:
        a, b = b, a + b
        yield b


#  num = int(input('input number for start: '))
#  step = int(input('input step: '))


#  def infin_line(num1=1, step1=1):
#      counter = num1

#      while True:
#          yield counter
#          counter += step1


#  def repeat_list(list_):
#     list_values = list_.copy()
#     while True:
#         value = list_values.pop(0)
#         list_values.append(value)
#         yield value

#  for i in repeat_list([1, 2, 3]):
#     print(i)

N = 100


def decorator_time(fn):
   def wrapper():
#       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
#       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
in_build_pow()


mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
   mean_pow_2 += pow_2()
   mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время:"
      f" {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время:"
      f" {mean_in_build_pow / 100:.10f}")


def D(a, b, c):
    return b ** 2 - 4 * a * c


def quadratic_solve(a, b, c):
    if D(a, b, c) < 0:
        return 'no real root'
    elif D(a, b, c) == 0:
        return - b / (2 * a)
    else:
        return (-b - D(a, b, c) ** 0.5) / (2 * a), \
            (-b + D(a, b, c) ** 0.5) / (2 * a)


L = list(map(float, input().split()))
print(quadratic_solve(*L))
M = {'a': 1, 'b': 0, 'c': -1}
print(quadratic_solve(**M))

iter_obj = iter("Hello!")

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))


def odd(x):
    return x % 2 == 0


result = filter(odd, [-2, -1, 0, 1, -3, 2, -3])
print(list(result))


d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
print(sorted(d.items(), key=lambda x: x[1]))
print(d.items())
print(d)

data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

min_index = min(data, key=lambda x: x[0] / x[1] ** 2)
print(min_index)


a = ["asd", "bbd", "ddfa", "mcsa"]
print(list(map(len, a)))


def print_ladder(n):
    for i in range(n + 1):
        print('*' * i)
 #   return 0


n = 5
print_ladder(n)

some_var = None

if some_var is None:
    print("NoneType")
else:
    print(type(some_var))


def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, который будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper


def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я - оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я - оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0

decorated_function1 = my_decorator(print_ladder)
#  decorated_function1()


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458

def linear_solve(a, b):
    return b/a

print(linear_solve(2, 9))


def f(n):
   return n * 123456789


def cache(func):
   cache_dict = {}
   def wrapper(num):
       nonlocal cache_dict
       if num not in cache_dict:
           cache_dict[num] = func(num)
           print(f"Добавление результата в кэш: {cache_dict[num]}")
       else:
           print(f"Возвращение результата из кэша: {cache_dict[num]}")
       print(f"Кэш {cache_dict}")
       return cache_dict[num]
   return wrapper

print(cache(f))
cache_new = cache(f)
cache_new(3)
cache_new(6)
cache_new(3)

