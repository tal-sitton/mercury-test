from collections import Counter


def av_of_list(list):
    """
    :type list: List
    """
    if (list):
        if type(list[0]) is int:
            return sum(list) / len(list)
        elif type(list[0]) is str:
            words_to_count = (word for word in list)
            c = Counter(words_to_count)
            first_common = c.most_common(2)[0]

            if len(c.most_common(2)) == 1:
                return first_common[0] + " x{} times".format(first_common[1])

            second_common = c.most_common(2)[1]
            if first_common[0] == '':
                return str(second_common[0]) + " x{} times".format(second_common[1])

            if first_common[1] is second_common[1]:
                return first_common[0] + " ; " + second_common[0] + " x{} times each".format(first_common[1])

            return first_common[0] + " x{} times".format(first_common[1])

        print("type: " + str(type(list[0])))
