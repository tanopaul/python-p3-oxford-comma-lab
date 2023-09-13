def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        comma_values = ", ".join(items[0: -1])
        and_value = ", and " + items[-1]
        sentence = comma_values + and_value
        print(sentence)

    return sentence

oxford_comma(["fiddleheads", "okra", "kohlrabi"])