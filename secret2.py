import random
import time

names = ['Mumma', 'Bhaiya', 'Bubba', 'Mankoo']
drawn = ['']
user = ''
assigner = 0
alreadyDrawn = False

i = 0
for i in range(len(names)):
    user = input('Enter name exactly as Mumma, Bhaiya, Bubba, or Mankoo: ')
    assignment = user
    while assignment == user:
        assigner = random.randint(0, (len(names) - 1))
        assignment = names[assigner]
        j = 0
        print(len(drawn))
        for j in range(len(drawn)):
            if drawn[j] == assignment:
                alreadyDrawn = True
            else:
                alreadyDrawn = False
        if assignment != user and alreadyDrawn == False:
            break
        elif assignment == user:
            pass
    drawn = drawn.append(assignment)
    print(f'You have {assignment}.')
    print('')