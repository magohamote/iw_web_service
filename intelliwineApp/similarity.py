import sys
from numpy import concatenate

from intelliwineApp.vector_reduction import reduce_bottle_aroma, reduce_user_charac
from math import*


def square_rooted(x):
    return sqrt(sum([a*a for a in x]))


def cosine_similarity(x, y):
    numerator = sum(a*b for a, b in zip(x, y))
    denominator = sqrt(sum([a*a for a in x]))*sqrt(sum([a*a for a in y]))
    return numerator/float(denominator)


def compute_cosine_similarity(user_charac, user_aroma, bottle_charac, bottle_aroma, unitary_user_vector):

    score = 0
    for key in bottle_aroma:
        reduced_user_charac = reduce_user_charac(user_charac, bottle_charac[key])
        reduced_bottle_aroma = reduce_bottle_aroma(bottle_aroma[key], user_aroma)

        full_user_vector = concatenate([reduced_user_charac, unitary_user_vector])
        full_bottle_vector = concatenate([[1, 1, 1, 1, 1, 1, 1, 1, 1], reduced_bottle_aroma])

        score = max(score, cosine_similarity(full_user_vector, full_bottle_vector))

    return score

