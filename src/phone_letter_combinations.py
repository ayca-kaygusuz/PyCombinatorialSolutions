# ©️ Ayça "Alex" Kaygusuz 2025
# Refer to README.md for How-Tos, problem descriptions, and more
# Uncomment example cases at the end of the file for example runs
# Run the related test file in the tests folder for more test cases

def letter_combinations(digits):
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    combinations = []

    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return
        digit = digits[index]
        if digit not in phone_map:
            return  # Skip invalid digits
        possible_letters = phone_map[digit]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return combinations

# Example usages:
# print(letter_combinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# print(letter_combinations(""))    # Output: []
# print(letter_combinations("2"))   # Output: ["a","b","c"]