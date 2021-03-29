# https://stepik.org/lesson/3380/step/1?unit=963
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

def count_games(game_dict, key, is_win, is_draft):
    if key in game_dict:
        game_dict[key]['total'] += 1
    else:
        game_dict[key] = { 'total': 1, 'wins': 0, 'fails': 0, 'drafts': 0, 'scores': 0 }

    if is_win:
        game_dict[key]['wins'] += 1
        game_dict[key]['scores'] += 3
    elif is_draft:
        game_dict[key]['drafts'] += 1
        game_dict[key]['scores'] += 1
    else:
        game_dict[key]['fails'] += 1



n = int(input())
result = {}
total_games = {}

for i in range(0,n):
    game = input()
    game_arr = game.strip().split(";")

    first_is_win = int(game_arr[1]) > int(game_arr[3])
    second_is_win = int(game_arr[1]) < int(game_arr[3])
    is_draft = not first_is_win and not second_is_win

    count_games(total_games, game_arr[0], first_is_win, is_draft)
    count_games(total_games, game_arr[2], second_is_win, is_draft)

for k,v in total_games.items():
    print(k, end=":")
    print(v['total'], v['wins'], v['drafts'], v['fails'], v['scores'], sep=" ")
