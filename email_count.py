def check_emails():
    txt_file = open('sample.txt')
    print(txt_file)
    count = 0
    emails = list()
    for line in txt_file:
        words = line.split(" ")
        if len(words) == 0:
            continue
        if words[0] != 'From':
            continue
        else:
            emails.append(words[1])
            count += 1
    print(emails, count)

check_emails()