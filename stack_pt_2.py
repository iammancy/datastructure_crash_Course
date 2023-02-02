from collections import deque

animals = deque()

print(dir(animals))


animals.append('rats')
animals.append('cats')
animals.append('dogs')
animals.append('cows')
animals.append('birds')
animals.append('fish')
animals.append('planktons')
animals.append('whales')


print(f'Animals list initially {animals}')

while(animals):
    print(animals.pop())

print(f'Animals list now : {animals}')