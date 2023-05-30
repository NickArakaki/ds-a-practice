def split(arr):
    string = arr[-1]
    words = []

    l = r = 0
    while r < len(string):
        if string[r].isupper():
            words.append(string[l:r])
            l = r
        r += 1

    words.append(string[l:r])

    if arr[0] == "M":
        words[-1] = words[-1][:-2]

    return " ".join(words).lower().strip()


def combine(arr):
    token = arr[0]
    string = arr[-1]
    words = string.split(" ")

    if token == "M" or token == "V":
        for i in range(1, len(words)):
            words[i] = words[i].title()
    else:
        for i in range(len(words)):
            words[i] = words[i].title()

    if token == "M":
        words.append("()")

    return "".join(words)



def main(s):
    components = s.split(";")

    if components[0] == "C":
        print(combine(components[1:]))
    else:
        print(split(components[1:]))

print(main("S;M;plasticCup()")) # plastic cup
print(main("S;C;LargeSoftwareBook")) # whiteSheetOfPaper()
print(main("S;V;pictureFrame")) # picture frame
print(main("C;V;mobile phone")) # mobilePhone
print(main("C;C;coffee machine")) # CoffeeMachine
print(main("C;M;white sheet of paper")) # plastic cup
