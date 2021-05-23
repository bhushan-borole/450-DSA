from pathlib import Path
import os
import datetime


ALL_SOLUTIONS = Path('solutions/')

count = {}
totals = {
    'Array': 36,
    'Matrix': 10,
    'String': 43,
    'Searching & Sorting': 36,
    'Linked List': 36,
    'Binary Trees': 35,
    'Binary Search Trees': 22,
    'Greedy': 35,
    'BackTracking': 22,
    'Stacks & Queues': 38,
    'Heap': 18,
    'Graph': 44,
    'Trie': 6,
    'Dynamic Programming': 60,
    'Bit Manipulation': 10
}

for folder in os.listdir(ALL_SOLUTIONS):
    count[folder] = len(os.listdir(str(ALL_SOLUTIONS) + '/' + folder))

now = datetime.datetime.now().date()
op = ''

for key in totals.keys():
    op += f'{key}: {count[key]}/{totals[key]}\n'

final_output = f'''
# 450 DSA

{op}

Last Update on {now}.
'''


with open('README.md', 'w+') as f:
    f.truncate(0)
    f.write(final_output)

