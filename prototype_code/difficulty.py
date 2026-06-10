def difficulty(clicked_order, practice_order):
    
    # Determines the participant's difficulty level based on the number of correctly remembered items in the calibration round.

    correct_streak = 0

    for index in range(len(clicked_order)):
        if index < len(practice_order) and clicked_order[index] == practice_order[index]:
            correct_streak += 1
        else:
            break

    if correct_streak == 1:
        return "easy"
    elif correct_streak == 2:
        return "medium"
    elif correct_streak == 3 or correct_streak == 4:
        return "hard"
    elif correct_streak == 5:
        return "extreme"
    else:
        return "easy"
