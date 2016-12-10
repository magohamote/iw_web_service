import sys


def create_user_charac_dict(user_vector):
    user_dict = dict()
    user_dict["sweetness"] = (user_vector["sweetness1"], user_vector["sweetness2"], user_vector["sweetness3"], user_vector["sweetness4"], user_vector["sweetness5"], user_vector["sweetness6"])
    user_dict["acidity"] = (user_vector["acidity1"], user_vector["acidity2"], user_vector["acidity3"], user_vector["acidity4"], user_vector["acidity5"])
    user_dict["tannin"] = (user_vector["tannin1"], user_vector["tannin2"], user_vector["tannin3"], user_vector["tannin4"], user_vector["tannin5"])
    user_dict["alcohol"] = (user_vector["alcohol1"], user_vector["alcohol2"], user_vector["alcohol3"], user_vector["alcohol4"], user_vector["alcohol5"])
    user_dict["body"] = (user_vector["body1"], user_vector["body2"], user_vector["body3"], user_vector["body4"], user_vector["body5"])
    user_dict["flavour_intensity"] = (user_vector["flavour_intensity1"], user_vector["flavour_intensity2"], user_vector["flavour_intensity3"], user_vector["flavour_intensity4"], user_vector["flavour_intensity5"])
    user_dict["quality_level"] = (user_vector["quality_level1"], user_vector["quality_level2"], user_vector["quality_level3"], user_vector["quality_level4"], user_vector["quality_level5"], user_vector["quality_level6"])

    return user_dict


def create_user_aroma_mask(user_aroma_vector):
    mask = []

    for i in user_aroma_vector:
        if user_aroma_vector[i] == 1:
            mask.append(i)

    return mask


def reduce_user_charac(vector_to_reduce, mask):
    reduced_vector = []

    for i in mask:
        if i in vector_to_reduce:
            reduced_vector.append(vector_to_reduce[i][mask[i]])

    return reduced_vector


def reduce_bottle_aroma(vector_to_reduce, mask):
    reduced_vector = []

    for i in mask:
        reduced_vector.append(vector_to_reduce[i])

    return reduced_vector

