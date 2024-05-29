def registry_players():
    players = []
    keep_registering = "yes"

    while keep_registering == "yes":
        name = str(input("Insert player's name: "))
        age = int(input("Insert player's age: "))
        weight = float(input("Insert player's weight: "))
        team = str(input("Insert player's team: "))

        player = [name, age, weight, team]

        players.append(player)

        keep_registering = str(input("Do tou want to register a new player? (yes or no): "))

    return players


def mean_age_from_corinthians_players_with_weight_above_80(players):
    total_players = 0
    age_sum = 0

    for player in players:
        if player[2] > 80 and player[3] == "corinthians":
            total_players += 1
            age_sum += player[1]

    return age_sum/total_players


def main():
    players = registry_players()

    print(f"Mean age of players from Corinthians and weight above 80 kilos: "
          f"{mean_age_from_corinthians_players_with_weight_above_80(players)}")


if __name__ == "__main__":
    main()
