from functools import cmp_to_key


def parse():
    return [(cards, int(bid)) for cards, bid in [line.split() for line in data]]


type_order = [
    [1, 1, 1, 1, 1],  # High card
    [1, 1, 1, 2],  # One pair
    [1, 2, 2],  # Two pair
    [1, 1, 3],  # Three of kind
    [2, 3],  # Full house
    [1, 4],  # Four of kind
    [5],  # Five of kind
]


def get_type(hand):
    count_dict = dict((c, hand.count(c)) for c in hand)
    return type_order.index(sorted(list(count_dict.values())))


def cmp(a, b):
    return (a > b) - (a < b)


def cmp_input_factory(get_type, strength_order):
    def cmp_input(input1, input2):
        hand1, hand2 = input1[0], input2[0]
        cmp_type = cmp(get_type(hand1), get_type(hand2))
        if cmp_type != 0:
            return cmp_type
        else:
            for i in range(len(hand1)):
                c1, c2 = hand1[i], hand2[i]
                cmp_card = cmp(strength_order.index(c1), strength_order.index(c2))
                if cmp_card != 0:
                    return cmp_card
            raise ValueError("unreachable")

    return cmp_input


def q1():
    data = parse()
    strength_order_p1 = "23456789TJQKA"
    sorted_data = sorted(
        data, key=cmp_to_key(cmp_input_factory(get_type, strength_order_p1))
    )
    return sum((i + 1) * v[1] for (i, v) in enumerate(sorted_data))


def get_type_q2(hand):
    if "J" in hand:
        return max(get_type(hand.replace("J", c)) for c in "J23456789TQKA"[1:])
    return get_type(hand)


def q2():
    data = parse()
    sorted_data = sorted(
        data, key=cmp_to_key(cmp_input_factory(get_type_q2, "J23456789TQKA"))
    )
    return sum((i + 1) * v[1] for (i, v) in enumerate(sorted_data))
