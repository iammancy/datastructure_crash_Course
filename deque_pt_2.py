from collections import deque

animals = deque()

animals.appendleft('rats')
animals.appendleft('cats')
animals.appendleft('dogs')
animals.appendleft('cows')
animals.appendleft('birds')
animals.appendleft('fish')
animals.appendleft('planktons')
animals.appendleft('whales')


print(f'initailly animals: {animals}')

while(animals):
    print(animals.pop())

print(f'now animals: {animals}')