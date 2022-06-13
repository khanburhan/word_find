# from english_words import english_words_set

def find_words():
    file = "/usr/share/dict/words"
    handle = open(file)
    words_list = handle.read().split('\n')
    handle.close()
    # print(words_list)

    ch1 = input("Please enter first character \n")
    ch1_count = int(input(
        "Please numbers of times first character should appear \n"))
    ch2 = input("Please enter second character \n")
    ch2_count = int(input(
        "Please numbers of times second character should appear \n"))
    ch3 = input("Please enter third character \n")
    ch3_count = int(input(
        "Please numbers of times third character should appear \n"))

    for word in words_list:
        word = word.lower()
        # if (len(word) != 6):
        if (word.count(ch1) != ch1_count):
            continue
        if (word.count(ch2) != ch2_count):
            continue
        if (word.count(ch3) != ch3_count):
            continue
        print(word)


find_words()
