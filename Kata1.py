# reverses all the words that are >= 5 chars
def spin_words(sentence):
    j = 0
    for i in range(len(sentence)):
        if sentence[i] == " ":
            if j >= 5:
                s1 = sentence[i-j:i]
                s3 = s1[::-1]
                s2 = sentence
                # strings are immutable, so it can't be edited directly. new string -> overwrite existing
                sentence = s2[:i-j] + s3 + s2[i:]
                j = 0
            else:
                j = 0
        elif i == len(sentence)-1 and j >= 4:
            s1 = sentence[i - j:i] + sentence[i]
            s3 = s1[::-1]
            s2 = sentence
            sentence = s2[:i - j] + s3
        else:
            j = j + 1
    return sentence


def main():
    sentence = "I programmed the strings so correctly!"
    sentence = spin_words(sentence)
    print(sentence)

if __name__ == '__main__':
    main()