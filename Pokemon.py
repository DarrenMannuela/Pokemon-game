file = None
with open("Pokemon List.txt", "r", encoding="utf-8") as d:
    file = d.read()

pokemons = file.split(" ")
pokemon_used = []


def game(pokemon_list: list):
    player_turn = "player_1"
    last_letter_of_prev_wrd = " "
    if player_turn == "player_1":
        player_1 = input("\nPlease choose your Pokemon player 1:").lower()
        if player_1 in pokemon_list:
            if player_1[0] == last_letter_of_prev_wrd or last_letter_of_prev_wrd == " " and player_1 not in pokemon_used:
                pokemon_used.append(player_1)
                last_letter_of_prev_wrd = player_1[-1]
                player_turn = "player_2"
            else:
                print("\nSorry that word has been used or does not match with the requirement", player_turn)
                return False
        else:
            print("\nSorry you have lost", player_turn)
            return False

    if player_turn == "player_2":
        player_2 = input("\nPlease choose your Pokemon player 2:").lower()
        if player_2 in pokemon_list:
            if player_2[0] == last_letter_of_prev_wrd or last_letter_of_prev_wrd == " " and player_2 not in pokemon_used:
                pokemon_used.append(player_2)
                last_letter_of_prev_wrd = player_2[-1]
                player_turn = "player_1"
            else:
                print("\nSorry that word has been used", player_turn)
                return False

        else:
            print("\nSorry you have lost", player_turn)
            return False
    return pokemon_used,  player_turn, last_letter_of_prev_wrd


if __name__ == "__main__":
    while True:
        game(pokemons)


