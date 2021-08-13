OUT_FILE = 'res/wordcount.txt'

def count_words():
    f = open('res/strongs.txt', 'r')
    d = {}
    for line in f:
        line = line[:-1].split(" ")
        for word in line:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d

def ordering(tup):
    return tup[1]

def to_tuple(d):
    tuples = []
    for key in d:
        tuples.append((key, d[key]))
    tuples.sort(key=ordering, reverse=True)
    return tuples

def write_to_file(tups):
    f = open(OUT_FILE, 'w')
    for tup in tups:
        f.write(tup[0] + ' - ' + str(tup[1]) + '\n')
    f.close()

def run():
    word_dict = count_words()
    tuples = to_tuple(word_dict)
    write_to_file(tuples)

if __name__ == "__main__":
    run()
    print("Check the file " + OUT_FILE)