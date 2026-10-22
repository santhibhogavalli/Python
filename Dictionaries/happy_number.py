# problem : Happy Number 19 → 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1
# scenario: Detect a cycle in a retry loop’s state
# pattern : sets
# solution : Use a set to track seen tasks. If a value is already in the set, it indicates a cycle.
def detect_cycle(sentences):
    seen = set()

    for sentence in sentences:
        if sentence in seen:
            print(f"Cycle detected: {sentence}")
            return

        seen.add(sentence)

    print("No cycle found")
       
if __name__ == "__main__":
    task = ["which is a happy number..??", "Not sure", "Let check this out", "which is a happy number..??", "Happy number is a number which eventually."]
    detect_cycle(task)