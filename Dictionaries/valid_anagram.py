# problem : Valid Anagram (listen → l i s t e n, silent → s i l e n t, eat → e a t, tea → t e a)

# Scenario : Check whether two template keys normalise to the same key

# pattern : dictionary
# solution : Use a dictionary to count the frequency of each character in both strings 
# and compare the dictionaries. If they are equal, the two strings are anagrams.

def valid_anagram(s, t):
    if len(s) != len(t):
        print("Not anagrams")
        return False
    count_s, count_t = {}, {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    if count_s == count_t:  
        print("Anagrams")
        return True 


if __name__  == "__main__":
    valid_anagram("listen", "silent")