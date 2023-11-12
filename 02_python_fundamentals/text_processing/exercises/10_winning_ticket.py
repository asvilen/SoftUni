def ticket_checker(text):
    if len(text) != 20:
        return "invalid ticket"
    half_length = int(len(text) / 2)
    left_part = text[:half_length]
    right_part = text[half_length:]
    winning_symbols = ['@', '#', '$', '^']
    for winning_symbol in winning_symbols:
        if winning_symbol in text:
            for repetitions in range(10, 5, -1):
                winning_symbol_repetitions = winning_symbol * repetitions
                if winning_symbol_repetitions in left_part and winning_symbol_repetitions in right_part:
                    if repetitions == 10:
                        return f'ticket "{text}" - {repetitions}{winning_symbol} Jackpot!'
                    else:
                        return f'ticket "{text}" - {repetitions}{winning_symbol}'
    return f'ticket "{text}" - no match'


ticket_collection = input().split(", ")
for ticket in ticket_collection:
    ticket = ticket.strip()
    print(ticket_checker(ticket))
