import random
number_ = []
for i in range(1000000):
    number_.append(random.randrange(0,1000000))
print(number_)
print(min(number_))
print(max(number_))
print(sum(number_))
print(len(number_))
print(random.randint(3, 9))
