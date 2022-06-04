from ascii_art import blackjack_art
from blackjack import begin_round, get_player_decision, dealer_plays, end_round, coins_left


print(blackjack_art);
print("\nWelcome to BlackJack!\n");

def get_game_over():
    if not coins_left():
        return True;
    yes_no = {"y" : False, "n" : True};
    decision = "";
    while decision not in yes_no:
        decision = input("Play again (Y/n)? ").lower();
    return yes_no[decision];

# Game loop
game_over = False;
while not game_over:
    begin_round();
    get_player_decision();
    dealer_plays();
    end_round();
    game_over = get_game_over();
    print("");


print("\nThank you for playing BlackJack!");
print("Goodbye.\n");