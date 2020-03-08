game_properties = [
    "current_score",
    "high_score",

    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 0)

print(initial_game_state)

a=initial_game_state.items()
count=0
for k,v in a:
    count+=1
    print(f"SrNo.{count} key is {k} and value is {v} ")
    