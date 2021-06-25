def do_health(max_health, health):

    health_dashes = 20  # Max Displayed dashes

    dash_convert = int(max_health/health_dashes)                 # Get the number to divide by to convert health to dashes (being 10)
    current_dashes = int(health/dash_convert)                     # Convert health to dash count: 80/10 => 8 dashes
    remaining_health = health_dashes - current_dashes             # Get the health remaining to fill as space => 12 spaces

    health_display = '\033[1;92m*\033[m' * current_dashes         # Convert 8 to 8 dashes as a string:   "--------"
    remaining_display = '-' * remaining_health                    # Convert 12 to 12 spaces as a string: "            "

    print("|" + health_display + remaining_display + "|" + f'( {health} / {max_health} )')# Print out textbased healthbar


do_health(200, 169)

