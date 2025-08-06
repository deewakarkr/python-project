string = input("Enter the string: ").lower()
checked = ""

while i < len(string):
    ch = string[i]
    if ch not in checked:
        count = 0
        j = 0
        while j < len(string):
            if string[j] == ch:
                count += 1
            j += 1
        print(f"{ch} occurs {count} times")
        checked += ch  # mark as counted
    i += 1
