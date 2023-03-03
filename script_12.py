print("Hello world")
print(13 % 3 * 3 - 3**2)
print(round(11*2.5/3, 2))
print(round(3.14159**2/2))
pi = 31.4159265
print ("%.4e" % (pi))

L = list(map(float, input().split()))
# number_str = input("Input numbers in pass ")
# number_single_str = number_str.split()
# number_list = list(map(int, number_single_str))
L[0], L[-1] = L[-1], L[0]
# print(number_list)
# number_list.append(number_list[0])
# print(number_list)
# number_list[0] = number_list[-2]
# print(number_list)
# number_list.pop(-2)
# print(number_list)
L.append(sum(L))
# number_list.append(sum(number_list))
# print(number_list)
print(L)


book = {'title': input('input title'), 'author': input('input name of author'), 'year': int(input('input year'))}
print(book)

text = '''The Zen of PythonBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!'''

#print(unique_list)
unique_set = list(set(text))
print(unique_set)
print("Количество уникальных символов: ", len(unique_set))

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
a = 5
b = 3+2
print(id(a))
print(id(b))
c = id(a) - id(b)
print(c)
