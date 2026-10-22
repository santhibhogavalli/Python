# Problem: Contains Duplicate
# pattern: sets
# Scenario : Detect duplicate prompt IDs in a batch

#solution: use a set to track seen prompt IDs. 
# If a prompt ID is not in the set, add it. If a prompt ID is already in the set, it is a duplicate.

def main():
    prompt_ids = [1, 2, 3, 3, 5, 1, 6]
    # set is new empty object which is iterable and can store unique elements.
    existing_ids = set()
    duplicates = []
    for id in prompt_ids:
        if id in existing_ids:
            duplicates.append(id)
        else:
            existing_ids.add(id)
    print("Duplicate prompt IDs:", duplicates)

if __name__ == "__main__":
    main()
