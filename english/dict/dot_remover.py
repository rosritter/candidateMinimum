from collections import OrderedDict
from wordcounter import read_file, write_file



def remove_dot_from_transcription(string: str) -> str:
    parts = []
    for word in string.split(' '):
        if '[' in word and '.' in word:
            print(word)
            w = word.replace('.', '')
            print(word)
        else:
            w = word    
        parts.append(w)
    return ''.join(parts)


def main(filename: str):
    
    content = read_file(filename)
    s = {}
    s['0'] = content.split('\n')[0]
    s['1'] = content.split('\n')[1]
    words = {sentense.split(' ')[2]: sentense for sentense in content.split('\n')[2:]}
    for w in words.keys():
        if not w in s.keys():
            s[w] = words[w]
        else:
            print(w)
    print(len(s))
    s = OrderedDict(sorted(s.items()))
    # print(s.keys())
    string = ''.join([ f"| {i - 1}  " + remove_dot_from_transcription(string) + '\n' 
                      for i, string in enumerate(s.values())])
    
    write_file(filename, string)

if __name__ == "__main__":
    main('dict.md')