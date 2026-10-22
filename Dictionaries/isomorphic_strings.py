# problem: Isomorphic Strings (egg → e g g, add → a d d, foo → f o o, bar → b a r)
# pattern: dictionary
# scenario: Map one tokenizer vocabulary to another consistently

# solution  use  two dictionaries to map characters from the first string to the second and vice versa.
# If a character in the first string is mapped to a different character in the second string or vice versa, return False.

def is_isomorphic(s, t):
    if len(s) != len(t):
       print("Not isomorphic")
       return False
    dic_s, dic_t = {}, {}
    for char_s, char_t in zip(s, t):
        if dic_s.get(char_s) is None and dic_t.get(char_t) is None:
            print(f"Mapping {char_s} to {char_t}")
            dic_s[char_s] = char_t
            dic_t[char_t] = char_s
        elif dic_s.get(char_s) != char_t or dic_t.get(char_t) != char_s:
            print("Not isomorphic")
            return False
    print("Isomorphic")

if __name__ == "__main__":
    is_isomorphic("sai", "santhi")