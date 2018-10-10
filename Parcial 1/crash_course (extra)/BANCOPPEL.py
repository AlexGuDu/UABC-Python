import random

def credit_raise(acct_holder, card_info):
    if card_info[0] == 1:
        old_credit = card_info[1]
        credit = card_info[1] + (card_info[1]*0.25)
        print(acct_holder+"'s credit went from", old_credit, 'to',credit)
    if card_info[0] == 2:
        old_credit = card_info[1]
        credit = card_info[1] + (card_info[1]*0.35)
        print(acct_holder+"'s credit went from",old_credit, 'to',credit)
    if card_info[0] == 3:
        old_credit = card_info[1]
        credit = card_info[1] + (card_info[1]*0.40)
        print(acct_holder+"'s credit went from",old_credit, 'to',credit)
    if card_info[0] != 1 and card_info[0] != 2 and card_info[0] != 3 :
        old_credit = card_info[1]
        credit = card_info[1] + (card_info[1]*0.50)
        print(acct_holder+"'s credit went from",old_credit, 'to',credit)

def assign_cards():
    cards_dict = {}
    for i in range(random.randint(1, 5)):
        c_info = [random.randint(1,4), random.randint(1500,6000)]
        c_card_num = 'c_card' + str(i)
        cards_dict.update({c_card_num:c_info})
    return cards_dict

def best_card(cards):
    best_c = next(iter(cards.values()))
    for key in cards.keys():
        c_type = cards[key][0]
        c_balance = cards[key][1]

        if c_type == best_c[0]:
            if c_balance > best_c[1]:
                best_c[0] = c_type
                best_c[1] = c_balance
        elif c_type > best_c[0]:
            best_c[0] = c_type
            best_c[1] = c_balance
    return best_c


credit_raise('Mike', best_card(assign_cards()))
