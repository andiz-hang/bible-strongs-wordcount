import requests
import sys

OUT_FILE = 'res/text.txt'

def fetch_passage(reference):
    if not reference:
        print("ERROR: Must provide a reference")
        exit()
    query = {'bible': 'kjv_strongs', 'reference': reference, 'data_format': 'raw', 'markup': 'raw'}
    return requests.get("https://api.biblesupersearch.com/api", params=query).json()['results']['kjv_strongs']

def get_ref_from_cl():
    if len(sys.argv) == 2:
        return sys.argv[1]
    if len(sys.argv) > 2:
        print('WARNING: Received 2 or more command-line arguments. Please provide only 1 argument')
        return ''
    return ''

def write_to_file(passages):

    f = open(OUT_FILE, 'w')

    for passage in passages:
        f.write(passage['text'] + '\n\n')
        

    f.close()

def run(ref):
    passages = fetch_passage(ref)
    write_to_file(passages)

if __name__ == '__main__':
    run()
    print("Check the file '" + OUT_FILE + "'")