from collections import deque

animals = deque()

print(dir(animals))


animals.appendleft('rats')
animals.appendleft('cats')
animals.appendleft('dogs')
animals.appendleft('birds')
animals.appendleft('rabbits')


print(f'Initial list {animals}')
while(animals):
    print(animals.pop())

print(f'Now animals: {animals}')