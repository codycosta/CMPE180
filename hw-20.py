'''
Author:     Cody Costa
Date:       5/13/2025

'''

def tower_of_hanoi(n, source, target, extra, step=[1]):
    tower_of_hanoi.counter += 1
    if n == 1:
        print(f'Step {step[0]}: Move WHEEL #1 from pillar {source} to {target}')
        step[0] += 1
    else:
        tower_of_hanoi(n - 1, source, extra, target, step)
        print(f'Step {step[0]}: Move WHEEL #{n} from pillar {source} to {target}')
        step[0] += 1
        tower_of_hanoi(n - 1, extra, target, source, step)


num_wheels = 2
tower_of_hanoi.counter = 0
tower_of_hanoi(num_wheels, 'A', 'B', 'C')

print(f'\nTotal Steps = {tower_of_hanoi.counter}')
