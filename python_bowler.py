'''
Script to calculate the score of a bowling game. Expected input is a string.
WARNING: Does not check for any type of bad inputs.
'''
def bowling_score(game):
    game_frames = [];
    last_frame = []
    # initiators:
    counter = 0;
    frame = 0;

    game = game.replace('-','0');
    # Distribute rolls into frames:
    while frame <= 8:
        if game[counter] == 'X':
            game_frames.append(10)
            counter = counter + 1
        else:
            this_frame = [game[counter], game[counter+1]]
            game_frames.append(this_frame)
            counter = counter + 2
        frame += 1

    # Calculate last frame score:
    num_last_rolls = len(game)-counter
    if num_last_rolls == 2:
        last_frame = [int(game[-1]), int(game[-2])]
        score = int(last_frame[0]) + int(last_frame[1])
    else:
        last_frame = game[-3]+game[-2]+game[-1]
        last_frame = [x if x!= 'X' else 10 for x in last_frame]  # X = 10

        if game[-2] == '/':
            score = 10 + int(last_frame[-1])
        elif game[-1] == '/':
            score = 20
        else:
            score = int(last_frame[0])+int(last_frame[1])+int(last_frame[2])

    game_frames.append(last_frame)

    # Score rest of game from last to first:
    for frame in range(8,-1,-1):
        # for strikes:
        if game_frames[frame] == 10:
            if game_frames[frame + 1] == 10:
                if game_frames[frame + 2] == 10: # turkey!
                    score += 30
                else:
                    score += (20 + int(game_frames[frame+2][0]))
            elif game_frames[frame + 1][1] == '/':
                score += 20
            else:
                score += 10 + (int(game_frames[frame+1][0]) +
                               int(game_frames[frame+1][1]))
        # for spares:
        elif game_frames[frame][1]== '/':
            if game_frames[frame+1] == 10:
                score += 20
            else:
                score += 10 + int(game_frames[frame+1][0])
        # nada
        else:
            score += int(game_frames[frame][0]) + int(game_frames[frame][1])

    return score
