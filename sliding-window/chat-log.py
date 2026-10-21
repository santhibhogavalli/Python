#Chat log: find the longest stretch of characters with no repeat, to spot spam bursts.

#problem : Find the longest stretch of characters with no 

#solution: 1. read all the paragraph into a string
#           2. use a sliding window approch to find the longest substring with no repeating characters.  
#           3. return the longest substring


def main(paragraph_data):
    #split the paragraph into words
    words = paragraph_data.split()
    #create a dictionary to store the last index of each character
    char_index = {}
    #initialize the start and end of the window 
    start = 0
    #initialize the longest substring
    longest_substring = ""
    #iterate through the words
    for end, char in enumerate(words):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end

        if end - start + 1 > len(longest_substring):
            longest_substring = words[start:end + 1]

    print("Longest substring with no repeating characters:", longest_substring)

if __name__ == "__main__":
    #read the paragraph into a string
    paragraph_data = """
                    Sliding Window Technique is a method used to solve problems that involve subarray or substring or window.Instead of repeatedly iterating over the same elements, the sliding window maintains a range (or “window”) that moves step-by-step through the data, updating results incrementally.The main idea is to use the results of previous window to do computations for the next window.Commonly used for problems like finding subarrays with a specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently.
                """
    main(paragraph_data)
