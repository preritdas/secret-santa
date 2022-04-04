import random
import numpy as np
import time

names = np.array(['Mumma', 'Bhaiya', 'Bubba', 'Mankoo'])
print(type(names))
print(len(names))

for name in names:
    user = input('Enter your name exactly. Mumma, Bhaiya, Bubba, or Mankoo: ')
    rando = random.randint(0, len(names) - 1)
    assignment = names[rando]
    while assignment == user:
        assignment = names[rando]
    i=0
    for i in range(len(names)):
        if names[i] == assignment:
            break
        else:
            pass
    np.delete(names, i)
    print(f'You have {assignment}. Pass device to next person. Exploding in 3...')
    time.sleep(2)
    print('2...')
    time.sleep(2)
    print('1...')
    time.sleep(2)
    i = 0
    for i in range(1):
        print('')