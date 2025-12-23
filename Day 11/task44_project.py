import art, random

def random_card():
    """This function will return the random value"""
    cards = [11, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 10 ,10, 10]
    card = random.choice(cards)
    return card

def score_cal(cards): 
    """This will return the sun of the users card """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        return 1
    
    return sum(cards)

def compare(user_score, computer_score):
    """This function will compare the score of the players"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose, Opponent has a Blackjack"
    elif user_score == 0:
        return "You Win,You have a Blackjack"
    elif computer_score  > 21:
        return "You win, Opponent went over"
    elif user_score  > 21:
        return "You lose, you went over" 
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(art.logo)

    user_cards = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False


    for _ in range(2):
        # rand_val = random_card()
        # user_list.append(rand_val) #we can also do this below
        user_cards.append(random_card())
        computer_card.append(random_card())
        

    while not is_game_over:
        user_score = score_cal(user_cards)
        computer_score = score_cal(computer_card)

        print(f"Your cards: {user_cards} Your Score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            want_card = input("Type 'y' for take another card or 'n' for not: ").lower()
            if want_card == "y":
                user_cards.append(random_card())
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score > 17:
        computer_card.append(random_card)
        computer_score = score_cal(computer_card)

    print(f"Your cards {user_cards} and Your Score: {user_score}." )
    print(f"Computer cards {computer_card} and Computer Score: {computer_score}." )
    print(compare(user_score, computer_score))

while input("Tpye 'y' to play and the Game and 'n' for not: ").lower() == "y":
    print("\n" * 20)
    play_game()