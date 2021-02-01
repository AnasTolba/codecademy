import random

money = 100

class ValidationException(Exception):
    pass

# Game Name Decorator
def game_decorator(game_function):
    def wrapper(*args, **kwargs):
        if game_function.__name__ == 'coin_flip':
            print('\nYou are playing Coin Flip:\n')
            game_function(*args, **kwargs)
        elif game_function.__name__ == 'cho_han':
            print('\nYou are playing Cho Han:\n')
            game_function(*args, **kwargs)
        elif game_function.__name__ == 'high_card':
            print('\nYou are playing High Card:\n')
            game_function(*args, **kwargs)
        elif game_function.__name__ == 'roulette':
            print('\nYou are playing Roulette:\n')
            game_function(*args, **kwargs)
    return wrapper

# Validators

def validate_bet(bet):
    global money
    if bet > money:
        print('You can\'t bet more than you have')
        raise ValidationException()
    elif bet < 0:
        print('Your bet can\'t be less than 0')
        raise ValidationException()
    else:
        pass

# Game of chance functions 

@game_decorator
def coin_flip(call, bet):
    flip = random.randint(1,2)
    computer_flip = ''
    global money
    validate_bet(bet)
    if flip == 1:
        computer_flip = 'Heads'
    else:
        computer_flip = 'Tails'
    
    if computer_flip == call:
        money += bet
        print('You chose {}\nThe coin flip result is {}\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(call, computer_flip, bet, money))
    else:
        money -= bet
        print('You chose {}\nThe coin flip result is {}\n\nYou have lost ${}\nYour total bank is now ${}\n\n\n'.format(call, computer_flip, bet, money))

@game_decorator
def cho_han(call, bet):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    even_or_odd = ''
    global money
    validate_bet(bet)
    if (dice1 + dice2) %2 == 0:
        even_or_odd += 'Even'
    else:
        even_or_odd += 'Odd'
    if call == even_or_odd:
        money += bet
        print('You chose {}\nThe dice roll results are: {} + {} = {}\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(call, dice1, dice2, dice1 + dice2, bet, money))
    else:
        money -= bet
        print('You chose {}\nThe dice roll results are: {} + {} = {}\n\nYou have lost ${}\nYour total bank is now ${}\n\n\n'.format(call, dice1, dice2, dice1 + dice2, bet, money))

@game_decorator
def high_card(bet):
    player_card = random.randint(1,13)
    computer_card = random.randint(1,13)
    global money
    validate_bet(bet)
    if player_card > computer_card:
        money += bet
        print('Your card was {}\nThe computers card was {}\nYour card was Higher\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(player_card, computer_card, bet, money))
    elif player_card < computer_card:
        money -= bet
        print('Your card was {}\nThe computers card was {}\nYoue card was Lower\n\nYou have lost ${}\nYour total bank is now ${}\n\n\n'.format(player_card, computer_card, bet, money))
    else:
        print('Your card was {}\nThe computers card was {}\n\nYou have tied \nYour total bank remains at ${}\n\n\n'.format(player_card, computer_card, money))

@game_decorator
def roulette(call, bet):
    random_num = random.randint(1,37)
    global money
    validate_bet(bet)
    if call == 'Even' and random_num % 2 == 0 and random_num != 0:
        money += bet
        print('You bet on {}\nThe wheel landed on {}\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(call, random_num, bet, money))
    elif call == 'Odd' and random_num % 2 == 1 and random_num != 37:
        money += bet
        print('You bet on {}\nThe wheel landed on {}\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(call, random_num, bet, money))
    elif call == random_num:
        money += (bet * 35)
        print('You bet on {}\nThe wheel landed on {}\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(call, random_num, bet*35, money))
    elif call == '00' and random_num == 37:
        money += (bet * 35)
        print('You bet on {}\nThe wheel landed on 00\n\nYou have won ${}\nYour total bank is now ${}\n\n\n'.format(call, bet*35, money))
    else:
        money -= bet
        print('You bet on {}\nThe wheel landed on {}\n\nYou have lost ${}\nYour total bank is now ${}\n\n\n'.format(call, random_num, bet, money))


#Game of chance functions called here

try:
    coin_flip('Heads', 101)
except ValidationException:
    pass
try:
    cho_han('Odd', 20)
except ValidationException:
    pass
try:
    high_card(30)
except ValidationException:
    pass
try:
    roulette('00', 10)
except ValidationException:
    pass
try:
    roulette('Even', 10)
except ValidationException:
    pass
try:
    roulette('Odd', 10)
except ValidationException:
    pass
try:
    roulette(12, 10)
except ValidationException:
    pass
