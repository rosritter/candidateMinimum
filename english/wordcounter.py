from collections import OrderedDict

def read_file(filename: str) -> str:
    with open(filename, "r") as file:
        content = file.read()  # Read the entire file into a single string
    return content

def write_file(filename: str, content:str) -> str:
    with open('new_' + filename, "w") as file:
        file.write(content)


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
    string = ''.join([string+'\n' for string in s.values()])
    write_file(filename, string)

if __name__ == "__main__":
    main('clear_dict.md')