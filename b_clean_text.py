import re

OUT_FILE = 'res/strongs.txt'

def clean_text():
    out = []
    f = open('res/text.txt', 'r')
    for line in f:
        if line != '\n':
            regex = '[GH][0-9]{3,4}'
            out.append(re.findall(regex, line))
    return out

def write_to_file(strongs):

    f = open(OUT_FILE, 'w')
    for line in strongs:
        s = ""
        for word in line:
            s += word + " "
        s = s[:-1] + "\n"
        f.write(s)

    f.close()

def run():
    cleaned = clean_text()
    write_to_file(cleaned)

if __name__ == '__main__':
    run()