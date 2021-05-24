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

def update_root_readme(path):
    for folder in os.listdir(ALL_SOLUTIONS):
        count[folder] = len(os.listdir(str(ALL_SOLUTIONS) + '/' + folder)) - 1

    now = datetime.datetime.now().date()
    op = ''

    for key in totals.keys():
        if key in count:
            op += f'{key}: {count[key]}/{totals[key]}  \n'

    final_output = f'# 450 DSA\n{op}\nLast Update on {now}.'


    with open('README.md', 'w+') as f:
        f.truncate(0)
        f.write(final_output)

def update_individual_readme(path):
    for folder in os.listdir(ALL_SOLUTIONS):
        folder = str(ALL_SOLUTIONS) + '/' + folder
        if not os.path.isfile(folder):
            all_files = os.listdir(folder)
            all_files.remove('README.md')

            if all_files:
                all_ids = [int(x[:2]) for x in all_files]

                with open(f'{folder}/README.md', 'r') as f:
                    all_lines = f.readlines()
                    for idx in all_ids:
                        print(all_lines[idx + 2])
                        all_lines[idx + 2] = all_lines[idx + 2].replace('[ ]', '[x]')
                        print(all_lines[idx + 2])
                    f.close()

                with open(f'{folder}/README.md', 'w') as f:
                    new_contents = ''.join(all_lines)
                    f.write(new_contents)
                    f.close()

update_individual_readme(ALL_SOLUTIONS)
update_root_readme(ALL_SOLUTIONS)
