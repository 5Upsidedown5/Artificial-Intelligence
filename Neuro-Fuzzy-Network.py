import math

def rule1(x1, x2, x3, c, q):
    a = math.exp(-math.pow((x1 - c) / q, 2)) * math.exp(-math.pow((x2 - c) / q, 2)) * math.exp(-math.pow((x3 - c) / q, 2)) #rules
    return a


def rule2(x1, x2, x3, c, q):
    a = math.exp(-math.pow((x1 - c) / q, 2)) * math.exp(-math.pow((x2 - c) / q, 2)) * math.exp(-math.pow((x3 - c) / q, 2))  # rules
    return a


def Calculate():

    w1 = 1
    w2 = 2

    numerator = 0
    denominator = 0
    neuron = 0
    c = [1, 2, 3, 4]
    q = [1, 2, 3, 4]
    x = [2, 4, 3], [6, 2, 1], [7, 5, 4], [6, 2, 2], [2, 1, 1]

    for v in range(5):
        numerator = w1 * rule1(x[v, 0], x[v, 1], x[v, 2], c[0], q[0]) + w2 * rule2(x[v, 0], x[v, 1], x[v, 2], c[1], q[1])
        denominator = rule1(x[v, 0], x[v, 1], x[v, 2], c[0], q[0]) + rule2(x[v, 0], x[v, 1], x[v, 2], c[1], q[1])
        neuron = numerator/denominator
        print(neuron)


