animals = []

animals.insert(0,'rats')
animals.insert(0,'cats')
animals.insert(0,'dogs')
animals.insert(0,'cows')
animals.insert(0,'birds')
animals.insert(0,'fish')
animals.insert(0,'planktons')
animals.insert(0,'whales')

print(f'initailly animals: {animals}')

while(animals):
    print(animals.pop())

print(f'now animals: {animals}')