def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    
    window_size = 5

    if len(opponent_history) < window_size:
        return 'S' 

    last_sequence = "".join(opponent_history[-window_size:])
    play_order[last_sequence] = play_order.get(last_sequence, 0) + 1
    
    if len(opponent_history) > window_size:
        opponent_history.pop(0)

    potential_plays = [last_sequence[-4:] + next_play for next_play in 'RPS']
    sub_order = {play: play_order.get(play, 0) for play in potential_plays}

    prediction = max(sub_order, key=sub_order.get)[-1]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]