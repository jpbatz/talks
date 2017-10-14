# The following puzzle comes from the checkio website and is used as the
# basis for a group problem-solving session during one of our PyHawaii sessions
# https://py.checkio.org/mission/the-longest-palindromic/

# Your task is to write a function that finds the longest palindromic substring
# of a given string.  string will be less than 20

# If you find more than one substring you should return the one which is closer
# to the beginning.

# solution 1: does not pass single letter "a"
# def longest_palindromic(text):
#     # your code here...
#     maxpal = ''
#     # loop over length of string
#     for index, char in enumerate(text):
#
#         endpos = len(text)
#         while endpos > index and endpos != -1:
#             endpos = text.rfind(char, index, endpos)
#             substr = text[index:endpos+1]
#             if endpos > index and substr == substr[::-1] and len(substr) > len(maxpal):
#                 maxpal = substr
#     return maxpal


# solution 2: passes all test!
# def longest_palindromic(text):
#     palindrome_word = ''
#     palindrome_size = 0
#     for start in range(len(text)):
#         for end in range(start + palindrome_size + 1, len(text) + 1):
#             tempword = text[start:end]
#             if tempword == tempword[::-1]:
#                 palindrome_word = tempword
#                 palindrome_size = len(tempword)
#     return palindrome_word

# solution 3: Jeff's
# def longest_palindromic(text):
#     longest = ''
#
#     # for i in range(len(text)):
#     #     for j in range(i, len(text)):
#     #         substr = text[i:j+1]
#
#     for substr in [text[i, j+1] for i in range(len(text)) for j in range(i, len(text))]:
#         if len(substr) > len(longest) and substr == substr[::-1]:
#             longest = substr
#     return longest

# solution 4:
def longest_palindromic(text):
    max_pal = []
    for x, _ in enumerate(text):
        for y in range(x+1, len(text)+1):
            substr = text[x:y]
            if substr == substr[::-1]:
                max_pal.append(substr)
    return max(longest, key=len)


if __name__ == '__main__':

    assert longest_palindromic("artrartrt") == "rtrartr"
    assert longest_palindromic("abacada") == "aba"
    assert longest_palindromic("aaaa") == "aaaa"
    assert longest_palindromic("a") == "a"
    print('All tests passed successfully')
