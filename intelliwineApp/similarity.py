import sys

from math import*


def square_rooted(x):
    return sqrt(sum([a*a for a in x]))


def cosine_similarity(x, y):
    numerator = sum(a*b for a, b in zip(x, y))
    denominator = sqrt(sum([a*a for a in x]))*sqrt(sum([a*a for a in y]))
    return numerator/float(denominator)


def get_json_value(vector):
    vector_values = []
    for key, value in vector.items():
        vector_values.append(value)

    return vector_values
