x = int(input())

for i in range(x):

    word = input()
    length = len(word)

    if length <= 10:
        print(word)

    else:
        print(word[0] + str(length - 2) + word[length - 1])

