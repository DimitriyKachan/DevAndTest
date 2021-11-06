def sort_str(strin):
    stri = strin.upper()

    names_pairs = stri.split(";")

    names = []
    for i in names_pairs:
        names.append(i.split(":"))

    a = len(names)

    while a > 0:
        for i in range(len(names)-1):
            if names[i][1][0] > names[i+1][1][0]:
                names_pairs[0], names_pairs[i+1] = names_pairs[i+1], names_pairs[i]

            elif names[i][1][0] == names[i+1][1][0]:
                if names[i][0][0] > names[i + 1][0][0]:
                    names_pairs[i], names_pairs[i+1] = names_pairs[i+1], names_pairs[i]
            a -= 1
    return names_pairs


s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

print(sort_str(s))