# PyCombinatorialSolutions

## Overview
PyCombinatorialSolutions is a Python library designed to solve combinatorial problems efficiently. This repository currently includes solutions for two problems: "Substring with Concatenation of All Words" and "Letter Combinations of a Phone Number".

## Problems

### 1. Substring with Concatenation of All Words
You are given a string `s` and an array of strings `words`. All the strings in `words` are of the same length. A concatenated string is a string that exactly contains all the strings of any permutation of `words` concatenated.

#### Problem Description
Return an array of the starting indices of all the concatenated substrings in `s`. You can return the answer in any order.

#### Examples
- **Example 1:**
    - Input: `s = "barfoothefoobarman"`, `words = ["foo","bar"]`
    - Output: `[0, 9]`
    - Explanation: The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of `words`. The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of `words`.

- **Example 2:**
    - Input: `s = "wordgoodgoodgoodbestword"`, `words = ["word","good","best","word"]`
    - Output: `[]`
    - Explanation: There is no concatenated substring.

- **Example 3:**
    - Input: `s = "barfoofoobarthefoobarman"`, `words = ["bar","foo","the"]`
    - Output: `[6, 9, 12]`
    - Explanation: The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"]. The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"]. The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

#### Constraints
- `1 <= s.length <= 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` and `words[i]` consist of lowercase English letters.

### 2. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent based on T9 input method (aka the old cellphone input method). Return the answer in any order.

#### Problem Description
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#### Examples
- **Example 1:**
    - Input: `digits = "23"`
    - Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

- **Example 2:**
    - Input: `digits = ""`
    - Output: `[]`

- **Example 3:**
    - Input: `digits = "2"`
    - Output: `["a","b","c"]`

#### Constraints
- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range ['2', '9'].

## Installation
To install the library, you can use pip:
```bash
pip install pycombinatorialsolutions
```

## Dependencies
This library requires the following dependencies:
- Python 3.6+
- `numpy` (for efficient array operations)
- `pytest` (for running tests)

You can install the dependencies using pip:
```bash
pip install numpy pytest
```

## Usage
```python
from pycombinatorialsolutions import find_substring_indices, letter_combinations

# Example usage for Substring with Concatenation of All Words
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(find_substring_indices(s, words))  # Output: [0, 9]

# Example usage for Letter Combinations of a Phone Number
digits = "23"
print(letter_combinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## License
This project is licensed under the MIT License. Check the LICENSE file for more details.