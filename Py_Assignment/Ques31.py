with open(r"C:\Users\Student\Documents\DS Training\text.txt", encoding='utf-8') as data:
    lines= data.readlines()
    words= sum(len(line.split()) for line in lines)
print("Lines: ", len(lines))
print("Words: ",words)