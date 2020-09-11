from collections import Counter


def average_of_list(the_list):
    """
    :type the_list: List
    """
    if the_list:
        if type(the_list[0]) is int:
            return sum(the_list) / len(the_list)
        elif type(the_list[0]) is str:
            words_to_count = (word for word in the_list)
            c = Counter(words_to_count)
            first_common = c.most_common(2)[0]

            if len(c.most_common(2)) == 1:
                return first_common[0]

            second_common = c.most_common(2)[1]
            if first_common[0] == '':
                return str(second_common[0])

            if first_common[1] is second_common[1]:
                return first_common[0] + " / " + second_common[0] + " x{} times each".format(first_common[1])

            return first_common[0]

        print("type: " + str(type(the_list[0])))
