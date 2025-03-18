# ©️ Ayça "Alex" Kaygusuz 2025
# Refer to README.md for How-Tos, problem descriptions, and more
# Uncomment example cases at the end of the file for example runs
# Run the related test file in the tests folder for more test cases

from collections import deque, defaultdict

def findSubstring(s, words):
    if not s or not words:
        return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = defaultdict(int)

    for word in words:
        word_count[word] += 1

    result = []

    for i in range(word_len):  # Check all possible start positions
        left = i
        right = i
        current_count = defaultdict(int)
        word_queue = deque()  # Track word order to remove old words correctly

        while right + word_len <= len(s):
            word = s[right:right + word_len]
            right += word_len

            if word in word_count:
                current_count[word] += 1
                word_queue.append(word)

                while current_count[word] > word_count[word]:
                    left_word = word_queue.popleft()
                    current_count[left_word] -= 1
                    left += word_len

                if right - left == total_len:
                    result.append(left)
            else:
                current_count.clear()
                word_queue.clear()
                left = right

    return result

# Example usages

# s1 = "barfoothefoobarman"
# words1 = ["foo", "bar"]
# print(findSubstring(s1, words1))  # Output: [0, 9]

# s2 = "wordgoodgoodgoodbestword"
# words2 = ["word", "good", "best", "word"]
# print(findSubstring(s2, words2))  # Output: []

# s3 = "barfoofoobarthefoobarman"
# words3 = ["bar", "foo", "the"]
# print(findSubstring(s3, words3))  # Output: [6, 9, 12]