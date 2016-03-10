# Kyle O'Connor kyjoconn@ucsc.edu assignment 4
import random


def cards_at_rank(rank):
    """ appends given rank to each suit """
    deck_1 = []
    for suit in 'CDHS':
        card = rank + suit
        deck_1.append(card)
    return deck_1


def get_deck():
    """applies cards_at_rank to each rank to return a deck with all possible ranks and suits"""
    deck = []
    for r in '23456789TJQKA':
        this_rank = cards_at_rank(r)
        deck += this_rank
    return deck


def count_occs(hand_int):
    """ given a hand containing only ranks, counts how many times each rank appears in the hand """
    rank = '23456789TJQKA'
    count = []
    for j in range(14):
        num_occs = hand_int.count(rank[j])
        count += num_occs


def rankpokerhand(hand):
    """ given a hand, ranks hand and returns an integer representation of flush, pair, etc """
    special_lst = [0] * 5
    hand_rank = 0
    hand_int = []
    hand_suit = []
    count_suit = [0] * 4
    count_instances = [0] * 13
    rank = '23456789TJQKA'
    suit = 'CDHS'
    #next 2 for loops collect lists of just integers and suits of the hand
    for i in range(len(hand)):
        hand_int += hand[i][0]
    for i in range(len(hand)):
        hand_suit += hand[i][1]
    #next two for loops collect numbers on how many times each rank or suit appears in given hand
    for j in range(4):
        count_suit[j] += hand_suit.count(suit[j])
    for j in range(13):
        count_instances[j] += hand_int.count(rank[j])
    #next two for loops account for hands of type straight flush and straight
    for k in range(len(count_instances)):
        if [1] * 5 == count_instances[k:k + 5] and 5 in count_suit:
            hand_rank = 1
    for k in range(len(count_instances)):
        if hand_rank != 1:
            if [1] * 5 == count_instances[k:k + 5]:
                hand_rank = 5
    #if statements to check for hand type
    if 4 in count_instances and hand_rank != 1:
        hand_rank = 2
    elif 2 in count_instances and 3 in count_instances:
        hand_rank = 3
    elif 5 in count_suit and hand_rank != 1:
        hand_rank = 4
    elif count_instances[12] == 1:
        for el in range(-1, 4):
            special_lst[el] += count_instances[el]
        if special_lst == [1] * 5:
            hand_rank = 5
    elif 3 in count_instances:
        hand_rank = 6
    elif count_instances.count(2) == 2:
        hand_rank = 7
    elif 2 in count_instances:
        hand_rank = 8
    # last elif statement to return high card if there are no other hand types that apply
    elif hand_rank != 1 and hand_rank != 5:
        high_card = '2C'
        for i in range(5):
            if rank.index(hand[i][0]) >= rank.index(high_card[0]):
                high_card = hand[i]
            hand_rank = high_card
    return hand_rank



def hand_string(hand_type):
    """ given an integer ranking, converts ranking to appropriate string full house, flush, etc """
    deck = get_deck()
    if hand_type == 1:
        return 'straight flush'
    if hand_type == 2:
        return 'four of a kind'
    if hand_type == 3:
        return 'full house'
    if hand_type == 4:
        return 'flush'
    if hand_type == 5:
        return 'straight'
    if hand_type == 6:
        return 'three of a kind'
    if hand_type == 7:
        return 'two pair'
    if hand_type == 8:
        return 'pair'
    elif hand_type <= 9:
        return 'high card'
    if hand_type >= 10:
        return deck[hand_type]


def monte_carlo(number_of_hands):
    """ runs rankpokerhand for desired trials, gathers and prints stats on results """
    result_list = []
    percentages = []
    deck = get_deck()
    for i in range(number_of_hands):
        hand = random.sample(deck, 5)
        result_int = rankpokerhand(hand)
        if result_int not in range(1, 10):
            result_int = 9
        result_list.append(result_int)
    for i in range(1, 10):
        percent = (float(result_list.count(i)) / number_of_hands) * 100
        percentages.append(percent)
    for i in range(1, 10):
        print '{0:18s} : {1:.2f}%'.format(hand_string(i), percentages[i - 1])

# next part so that this file can be imported as a module
if __name__ == "__main__":
    #if run standalone (not imported) will print the stats for 10000 hands
    print monte_carlo(10000)





