# Task 1: Write a function smallest that accepts a List of numbers as an argument. It should return the smallest number in the List.
def smallest(numbers):
        s = sorted(set(numbers))
        return s[0]

numbers = [56, 78, 90, 43, 34, 98, 2, 6, 65]
print(smallest(numbers))


# Task 2: Write a function largest that accepts a List of numbers as an argument. It should return the largest number in the List
def largest(numbers):
        s = sorted(set(numbers))
        return s[-1]

numbers = [56, 78, 90, 43, 34, 98, 2, 6, 65]
print(largest(numbers))

# Task 3: Write a function shortest that accepts a List of Strings as an argument. It should return the shortest String in the List
def find_shortest_word(words_list):
        word_len = []
        for word in words_list:
                word_len.append((len(word), word))
        word_len.sort()
        return word_len[0][1]

print(find_shortest_word(["PHP", "Exercises", "Backend"]))


# Task 4: Write a function longest that accepts a List of Strings as an argument. It should return the longest String in the List
def find_longest_word(words_list):
        word_len = []
        for n in words_list:
        word_len.append((len(n), n))
        word_len.sort()
        return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))