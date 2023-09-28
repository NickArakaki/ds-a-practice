"""
Given a string s, sort it in decreasing order based
on the frequency of the characters. The frequency of
a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers,
return any of them.

Constraints:
    1 <= s.length <= 5 * 105
    s consists of uppercase and lowercase English letters and digits.
"""

def frequencySort(s):
    frequency_map = {}

    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) + 1

    # sorted_chars = freq_map.items().sort(key= lambda tup: tup[1], reverse=True)
    freq_list = list(frequency_map.items())
    freq_list.sort(key=lambda tup: tup[1], reverse=True)

    res = ""
    for char, freq in freq_list:
        res += char * freq

    return res

print(frequencySort("tree")) # "eert"
print(frequencySort("cccaaa")) # "aaaccc"
print(frequencySort("Aabb")) # "bbAa"
