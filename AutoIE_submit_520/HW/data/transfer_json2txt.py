import json


with open('data/Test.json', 'r', encoding='utf8') as file:
    test_dicts = []
    file_test = file.read().split('\n')
    for line in file_test:
        if len(line) == 0:
            continue
        test_dicts.append(json.loads(line))
test_dicts.sort(key=lambda a: a['id'])

cnt = 0
with open('data/test.txt', 'w+', encoding='utf8') as file:
    for d in test_dicts:
        for char in d['query']:
            file.write(char+" O\n")
        file.write('\n')
        cnt+=1
print(cnt)

