def help_generation(clicked_order, correct_order, hint_state, condition, name_map, get_row_hint):

    # Generates a hint based on the participant's current answer and help condition
    
    # Check whether the participant made a mistake

    wrong_index = None

    for index in range(len(clicked_order)):
        if index < len(correct_order) and clicked_order[index] != correct_order[index]:
            wrong_index = index
            break

    # Error hints

    if wrong_index is not None:

        if hint_state["last_wrong_index"] != wrong_index:
            hint_state["wrong_help_level"] = 0
            hint_state["last_wrong_index"] = wrong_index

        hint_state["wrong_help_level"] += 1

        correct_item = correct_order[wrong_index]
        correct_word = name_map[correct_item]
        step_number = wrong_index + 1
        row_hint = get_row_hint(correct_item)

        if condition == "system":

            if hint_state["wrong_help_level"] == 1:
                return "Stap " + str(step_number) + " is in de " + row_hint + "."

            return "Stap " + str(step_number) + " moet " + correct_word + " zijn."

        if condition == "user":

            if hint_state["wrong_help_level"] == 1:
                return "Stap " + str(step_number) + " lijkt nog niet te kloppen. Probeer daar een ander voorwerp."

            if hint_state["wrong_help_level"] == 2:
                return "Stap " + str(step_number) + " lijkt nog niet te kloppen. Stap " + str(step_number) + " is in de " + row_hint + "."

            return "Stap " + str(step_number) + " moet " + correct_word + " zijn."

    # Next-step hints

    hint_state["last_wrong_index"] = None

    correct_so_far = 0

    for index in range(len(clicked_order)):
        if index < len(correct_order) and clicked_order[index] == correct_order[index]:
            correct_so_far += 1
        else:
            break

    if hint_state.get("last_correct_so_far") != correct_so_far:
        hint_state["next_help_level"] = 0
        hint_state["last_correct_so_far"] = correct_so_far

    hint_state["next_help_level"] += 1

    remaining_items = correct_order[correct_so_far:]

    # Sequence complete
  
    if len(remaining_items) == 0:
        return "Volgens mij heeft u de hele volgorde al ingevuld. U kunt op klaar klikken als u tevreden bent."

    next_item = remaining_items[0]
    next_word = name_map[next_item]
    row_hint = get_row_hint(next_item)

    if condition == "user":

        if hint_state["next_help_level"] == 1:
            return "U bent al goed bezig. Ik zal u een kleine hint geven. Het volgende voorwerp bevindt zich in de " + row_hint + "."

        return "De volgende stap moet " + next_word + " zijn."
    
    if condition == "system":

        if hint_state["next_help_level"] == 1:
            return "U bent al goed bezig. Het volgende voorwerp bevindt zich in de " + row_hint + "."

        return "De volgende stap moet " + next_word + " zijn."
