import re
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

file = open("tweets.txt", "r", encoding='utf-8')
string = ''
file1 = open("preprocessed_tweets.txt", "w", encoding='utf-8')

a = True
while a:
    string = file.readline()
    if not string:
        a = False
    str = []
    new_string = ''
    str = re.split(' ', string)
    i = 0
    while len(str) != i:

        remove = re.match('\A@', str[i])
        if remove:
            new_string = re.sub(str[i], '', string)
            string = new_string
        remove = re.findall(r'([A-Za-zıİüÜöÖğĞşŞçÇ]+([/!.,;:\-\'’#“”]|[\d])+[A-Za-zıİüÜöÖğĞşŞçÇ]+)', str[i])
        if remove:
            new_string = re.sub(str[i], '', string)
            string = new_string
        i = i + 1
    i = 0
    while len(str) != i:
        if "(" in str[i]:
            new_string = re.sub('[:+$*?();!.,;/\-\'’^“”]|[\d+]+', '', string)
            string = new_string
        elif "?" in str[i]:
            new_string = re.sub('[:+$*?();!.,;/\-\'’^“”]|[\d+]+', '', string)
            string = new_string
        elif "^" in str[i]:
            new_string = re.sub('[:+$*?();!.,;/\-\'^’“”]|[\d+]+', '', string)
            string = new_string
        elif "*" in str[i]:
            new_string = re.sub('[:+$*?();!.,;/\-\'’^“”]|[\d+]+', '', string)
            string = new_string
        elif "$" in str[i]:
            new_string = re.sub('[:+$*?();!.,;/\-\'’^“”]|[\d+]+', '', string)
            string = new_string
        elif "+" in str[i]:
            new_string = re.sub('[:+$*?();!.,/\-\'’^“”]|[\d+]+', '', string)
            string = new_string
        elif ")" in str[i]:
            new_string = re.sub('[:+$*?();!.,;/\-\'’^“”]|[\d+]+', '', string)
            string = new_string
        else:
            remove = re.findall('\w', str[i])
            new_string = re.sub(str[i], listToString(remove), string)
            string = new_string
            str[i] = str[i].replace(str[i], listToString(remove))
            remove = re.findall('\D', str[i])
            new_string = re.sub('\d', '', string)

            string = new_string

        i = i + 1
    new_string = re.sub(' +', ' ', new_string)
    new_string = re.sub("^\s+", "", new_string)
    new_string = re.sub("\s+$", "", new_string)
    file1.write(new_string + "\n")
file1.close()
file.close()
