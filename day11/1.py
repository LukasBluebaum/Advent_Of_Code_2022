from math import prod


monkeys_test = [
    {
        'items':[79, 98],
        'operation': 'mul',
        'operand': 19,
        'div': 23,
        True: 2,
        False: 3,
    },
    {
        'items':[54, 65, 75, 74],
        'operation': 'add',
        'operand': 6,
        'div': 19,
        True: 2,
        False: 0,
    },
    {
        'items':[79, 60, 97],
        'operation': 'pow',
        'operand': 2,
        'div': 13,
        True: 1,
        False: 3,
    },
    {
        'items':[74],
        'operation': 'add',
        'operand': 3,
        'div': 17,
        True: 0,
        False: 1,
    }
]

monkeys = [
    {
        'items':[71, 56, 50, 73],
        'operation': 'mul',
        'operand': 11,
        'div': 13,
        True: 1,
        False: 7,
    },
    {
        'items':[70, 89, 82],
        'operation': 'add',
        'operand': 1,
        'div': 7,
        True: 3,
        False: 6,
    },
    {
        'items':[52, 95],
        'operation': 'pow',
        'operand': 2,
        'div': 3,
        True: 5,
        False: 4,
    },
    {
        'items':[94, 64, 69, 87, 70],
        'operation': 'add',
        'operand': 2,
        'div': 19,
        True: 2,
        False: 6,
    },
    {
        'items':[98, 72, 98, 53, 97, 51],
        'operation': 'add',
        'operand': 6,
        'div': 5,
        True: 0,
        False: 5,
    },
    {
        'items':[79],
        'operation': 'add',
        'operand': 7,
        'div': 2,
        True: 7,
        False: 0,
    },
    {
        'items':[77, 55, 63, 93, 66, 90, 88, 71],
        'operation': 'mul',
        'operand': 7,
        'div': 11,
        True: 2,
        False: 4,
    },
    {
        'items':[54, 97, 87, 70, 59, 82, 59],
        'operation': 'add',
        'operand': 8,
        'div': 17,
        True: 1,
        False: 3,
    }
]


def apply_op(monkey, item):
    if monkey['operation'] == 'add':
        return item + monkey['operand']
    elif monkey['operation'] == 'mul':
        return item * monkey['operand']
    else:
        return item * item

factor = prod(monkey['div'] for monkey in monkeys)

inspections = [0] * len(monkeys)
rounds = 10000
for _ in range(rounds):
    for idx, monkey in enumerate(monkeys):
        inspections[idx] += len(monkey['items'])
        for item in monkey['items']:
            item = apply_op(monkey, item) % factor
            monkeys[monkey[(item % monkey['div']) == 0]]['items'].append(item)
        monkey['items'] = []

    #for monkey in monkeys:
    #    print(monkey['items'])

inspections = sorted(inspections)
print(inspections[-1] * inspections[-2])


