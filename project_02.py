def wordsNumber(phrase):
    li = phrase.split(sep=" ")
    words = []
    for element in li:
        if element not in words:
            words.append(element)
    return(len(words))        

ph = input("please enter your phrase   ")
print(f"your phrase contain {wordsNumber(ph)} words without repetion")
