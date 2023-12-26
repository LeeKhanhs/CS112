def football_kit(n, teams):
    # Create an array to count the occurrences of each home color
    home_colors = [0] * (10**5 + 1)
    
    # Count the occurrences of each home color
    for home_color, away_color in teams:
        home_colors[home_color] += 1

    # Calculate and print the number of games each team plays in home and away kits
    for home_color, away_color in teams:
        home_games = n - 1 + home_colors[away_color]
        away_games = n - 1 - home_colors[away_color]
        print(home_games, away_games)

# Input: Number of teams
n = int(input())

# Input: Team descriptions
teams = [tuple(map(int, input().split())) for _ in range(n)]

# Output: Number of games each team plays in home and away kits
football_kit(n, teams)