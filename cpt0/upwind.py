
def upwind():
# Map (2D grid)
    game_map = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", " ", "#"],
        ["#", " ", " ", " ", "#", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]

# Player starting position
    player_x = 1
    player_y = 1

    def draw_map():
        for y in range(len(game_map)):
            for x in range(len(game_map[y])):
                if x == player_x and y == player_y:
                    print("P", end="")
                else:
                    print(game_map[y][x], end="")
            print()

    def move(dx, dy):
        global player_x, player_y
        new_x = player_x + dx
        new_y = player_y + dy

    
        if game_map[new_y][new_x] != "#":
            player_x = new_x
            player_y = new_y

# Game loop
    while True:
        draw_map()
        move_input = input("Move (w/a/s/d or q to quit): ")

        if move_input == "q":
            break
        elif move_input == "w":
            move(0, -1)
        elif move_input == "s":
            move(0, 1)
        elif move_input == "a":
            move(-1, 0)
        elif move_input == "d":
            move(1, 0)

        print("\n" * 5)  # clear screen effect