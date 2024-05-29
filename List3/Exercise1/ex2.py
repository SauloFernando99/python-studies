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

def main():
    players = registry_players()


if __name__ == "__main__":
    main()
