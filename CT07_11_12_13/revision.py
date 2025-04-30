# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884]

# maximum = 0
# for i in list1:
#     if i > maximum:
#         maximum = i
# print(maximum)

# # find the minimum

# minimum = 10101001010101000101001010010010
# for i in list1:
#     if i < minimum:
#         minimum = i
# print(minimum)

# sum = 0
# for i in list1:
#     sum += i
# length = len(list1)
# print(sum)
# average = sum / length
# print(average)
# ARTTSDP = round(sum / length, 2)
# print(ARTTSDP)



words = [
    "level", "racecar", "orange", "radar", "banana", "civic", "refer",
    "apple", "madam", "kayak", "robot", "reviver", "noon", "pop", "deed",
    "book", "wow", "mirror", "eye", "nope", "rotor", "stats", "hello", 
    "toot", "peep", "school", "mum", "dad", "gig", "noon",
    "python", "coding", "class", "student", "lesson", "computer", "keyboard",
    "monitor", "window", "projector", "teacher", "laptop", "science", "library",
    "pencil", "marker", "whiteboard", "homework", "question", "answer"
]

word = "nnnnn"


# function only checks 1 word to see if its a palindrome
def isitapalindromeidkwhyuwouldwanttoknowthisanywaysword(word):
    if word == word[::-1]:
        return True
    else:
        return False

for maybeapalindrome in words:
    if isitapalindromeidkwhyuwouldwanttoknowthisanywaysword(maybeapalindrome):
        print(maybeapalindrome + "is a palindrome")
