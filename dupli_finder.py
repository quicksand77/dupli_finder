def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word.upper() in counts:
            counts[word.upper()] += 1
        else:
            counts[word.upper()] = 1
    counts2 = count_duplicates(counts)
    try:
        return counts, counts2, len(counts), len(counts2)
    except:
        return counts, counts2, len(counts), counts2



def count_duplicates(counts):
    counts2 = dict()
    for key in counts:
        if counts[key] > 1:
            counts2[key] = counts[key]
        else:
            pass
    if len(counts2) > 0:
        return counts2
    else:
        return 0


input1 = input("Please input the string to check for duplicates - separated by tabs, spaces or commas: ")

counts, counts2, total1, total2 = word_count(input1)


print("List of words and their occurrences:",counts)



print("There are a total of",total1,"words.")
print("There are",total2,"duplicated words.\n")

if counts2 == 0:
    print("Congratulations, there are no duplicates.")
else:
    print("List of words that occurred more than once:",counts2)

pause1 = input("Press enter to continue.")