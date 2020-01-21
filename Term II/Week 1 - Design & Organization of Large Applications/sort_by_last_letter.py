stored = []

def sort_by_last_letter(strings):
    def last_letter(x):
        return x[-1]
    stored.appemd(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)

