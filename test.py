# elements = ['Humphrey the Bear', 'Spike the Bee', 'Fat Cat']
# # print(elements)


# my_file = open('animals.txt', 'r')
# for line in my_file:
#     val = list(map(int, line.split(" ")))
#     print(sum(val))

# my_file.close()


# with open('animals.txt', 'r') as my_file:
#     for line in my_file:
#         values_str = line.split(" ")
#         values_int = list(map(int, ))
#         print(sum(values_int))


# # In F strings,
# # !r - repr() - shows us the characters
# # !s - str()
# # !a - ascii()


# read test_file.txt
# from os import system


# with open('animals.txt') as file:
#     print(repr(file.readlines()))


# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# with open('planets.txt', 'w', encoding='utf-8') as file:
#     for planet in planets:
#         file.write(planet + '\n')


# old_file_lines = []
# with open('animals.txt') as file:
#     old_file_lines = file.read().split("\n")


# with open('animals_new.txt', 'w') as file:
#     for idx, line in enumerate(old_file_lines):
#         if idx == len(old_file_lines) - 1:
#             print(line, end='', file=sys.stderr)
#         else:
#             print(line, end=' ', file=file)


# text = "john.andrew.smith@yougotmail.com"

# idx = text.index('@')

# print(text[:idx])


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


# print(numbers[5::5])


# s_words = []
# text = "First ladies rule the State and state the rule: ladies first"
# for word in text.split(" "):
#     if word[-1] == "s":
#         s_words.append(word)

# print("_".join(s_words))


# random_numbers = [1, 22, 333, 4444, 55555]
# random_numbers_str = list(map(str, random_numbers))
# print("\n".join(random_numbers_str))



dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
text = "srutinize is to examene closely and minutely"
# mispelt_words = []
# for word in text.split():
#     if word not in dictionary:
#         mispelt_words.append(word)


# print("\n".join(mispelt_words))


