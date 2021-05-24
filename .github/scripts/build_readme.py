from pathlib import Path
import os
import datetime
import textwrap
import urllib.parse


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

op = '''
# 450 DSA

|Category|# completed ps|# total ps|% complete|
|:---:|:---:|:---:|:---:|
'''

def update_root_readme(path):
    for folder in os.listdir(path):
        count[folder] = len(os.listdir(str(path) + '/' + folder)) - 1

    now = datetime.datetime.now().date()
    op = textwrap.dedent('''
        # 450 DSA

        |Category|# completed ps|# total ps|% complete|
        |:---:|:---:|:---:|:---:|
        ''')

    for key in totals.keys():
        if key in count:
            complete = count[key]
            remaining = totals[key]
            percent = round(complete/remaining * 100, 1)
            url = urllib.parse.quote(f'./solutions/{key}')
            op += f'|[{key}]({url})|{complete}|{remaining}|{percent}|\n'

    op += f'\n\n### Last Update on {now}.'

    with open('README.md', 'w+') as f:
        f.truncate(0)
        f.write(op)

def update_individual_readme(path):
    for folder in os.listdir(path):
        category = str(path) + '/' + folder
        if not os.path.isfile(category):
            all_files = os.listdir(category)
            all_files.remove('README.md')

            if all_files:
                all_ids = [int(x[:2]) for x in all_files]

                with open(f'{category}/README.md', 'r') as f:
                    all_lines = f.readlines()
                    for idx in all_ids:
                        print(all_lines[idx + 2])
                        all_lines[idx + 2] = all_lines[idx + 2].replace('[ ]', '[x]')
                        print(all_lines[idx + 2])
                    f.close()

                with open(f'{category}/README.md', 'w') as f:
                    new_contents = ''.join(all_lines)
                    f.write(new_contents)
                    f.close()

update_individual_readme(ALL_SOLUTIONS)
update_root_readme(ALL_SOLUTIONS)
