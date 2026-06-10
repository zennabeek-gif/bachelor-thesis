def system_inititiated_triggers(condition, help_is_shown, help_offer_is_shown, show_order_again, error_made, clicked_order, correct_order, last_error_offer_order, last_correct_offer_order, current_time, last_help_offer_time, last_click_time):

    # Only offer automatic help in the system-initiated condition.
    if condition != "system":
        return None

    # Do not offer help if another help message is already visible.
    if help_is_shown or help_offer_is_shown or show_order_again:
        return None

    # Offer help after a new mistake.
    if error_made and clicked_order != last_error_offer_order:
        return "Mmm, volgens mij ging er iets niet helemaal goed. Zal ik even met u meekijken?"

    # Offer help when the sequence appears complete.
    if clicked_order == correct_order and clicked_order != last_correct_offer_order:
        return "Volgens mij heeft u de hele volgorde goed ingevuld. U kunt op klaar klikken als u tevreden bent."

    # Offer help after 10 seconds of inactivity.
    if current_time - last_help_offer_time > 10 and current_time - last_click_time > 10:
        return "Ik zie dat u even nadenkt. Zal ik u een klein beetje op weg helpen?"

    return None
