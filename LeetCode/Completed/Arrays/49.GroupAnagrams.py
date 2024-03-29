"""
Given an array of strings strs,
group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by
rearranging the letters of a different word
or phrase, typically using all the
original letters exactly once.

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

# def groupAnagrams(strs):
#     res = {}

#     for s in strs:
#         key = "".join(sorted(s))

#         if key not in res:
#             res[key] = [s]
#         else:
#             res[key].append(s)

#     return res.values()

def groupAnagrams(strs):
    res = {}

    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1

        if tuple(count) not in res:
            res[tuple(count)] = [s]
        else:
            res[tuple(count)].append(s)

    return res.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""])) # [[""]]
print(groupAnagrams(["a"])) # [["a"]]
