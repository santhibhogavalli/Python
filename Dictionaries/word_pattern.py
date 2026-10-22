# problem : Word Pattern (abba → a b b a, dog cat cat dog → d o g c a t c a t d o g)
# pattern : dictionary
# scenario : Check a message sequence matches a fixed role pattern.

# solution : use 2 dictionaries to map char from the pattern to the word and vice versa.
# If a character in the pattern is mapped to a different word or vice versa, print not a valid pattern word and continue for next word.
def word_pattern(pattern, message):
    if len(pattern) != len(message):
        print("Not matching")
        return False
    dic_p, dic_m = {}, {}
    for char_p, word_m in zip(pattern, message):
        if dic_p.get(char_p) is None and dic_m.get(word_m) is None:
            print(f"Mapping {char_p} to {word_m}")
            dic_p[char_p] = word_m
            dic_m[word_m] = char_p
        elif dic_p.get(char_p) != word_m or dic_m.get(word_m) != char_p:
            print("Not a valid pattern word")
        
    return True

if __name__ == "__main__":
    pattern = "abbabba"
    message = ["dog cat cat dog", "dog cat cat fish", "dog cat dag cat", "dog dog dog dog", "dog cat cat dog", "dog cat tat fish", "dog cat fish tat"]
    word_pattern(pattern, message)