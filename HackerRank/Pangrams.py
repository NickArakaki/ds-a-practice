def pangrams(s):
    # Write your code here
    if len(s) < 26:
        return "not pangram"

    words = s.split(" ")
    chars = set("".join(words).lower())
    return "pangram" if len(chars) == 26 else "not pangram"


print(pangrams("The quick brown fox jumps over the lazy dog")) # "pangram"
