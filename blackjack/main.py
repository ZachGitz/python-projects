import art
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def deal_card():
    return random.choice(cards)


def calculate_score(card):
    if (sum(card) == 21 and len(card) == 2):
        return 0
    if (11 in card and sum(card) > 21):
        card.remove(11)
        card.append(1)
    return sum(card)


def computer():
    while (calculate_score(computer_cards) <= 17):
        computer_cards.append(deal_card())


def compare(user_score, computer_score):
    if (user_score > computer_score and computer_score <= 21 and user_score <= 21):
        print("YOU WON")
    elif (user_score < computer_score and computer_score <= 21 and user_score <= 21):
        print("YOU LOST")
    elif (user_score > 21 and computer_score <= 21):
        print("YOU LOST")
    elif (user_score <= 21 and computer_score > 21):
        print("YOU WON")
    elif (user_score == computer_score or user_score > 21 and computer_score > 21):
        print("DRAW")


def blackjack():
    print(art.logo)
    inp = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if (inp == "n"): return
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer()
    print(f"  Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"  Computer's first card: {computer_cards[0]}")
    ent = "t"

    while (ent != "n"):
        if (calculate_score(user_cards) > 21):
            break
        ent = input("Type 'y' to get another card, type 'n' to pass:")
        if (ent == "y"):
            user_cards.append(deal_card())
            clear()
            print(art.logo)
            print(f"  Your cards: {user_cards}, current score:{calculate_score(user_cards)}")
            print(f"  Computer's first card: {computer_cards[0]}")
    print(f"  Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"  Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    compare(calculate_score(user_cards), calculate_score(computer_cards))

    ant = input("Do you want to play another game of Blackjack? y/n: ")
    if (ant == "y"):
        clear()
        blackjack()
    else:
        return


blackjack()