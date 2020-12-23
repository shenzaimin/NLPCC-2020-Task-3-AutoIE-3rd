from tqdm import tqdm


with open('./ValidLabel.json', 'r', encoding='utf8') as file:
    import json
    file_valid = file.read().split('\n')
    dict_list = []
    for line in tqdm(file_valid):
        if len(line) == 0:
            continue
        else:
            dict_list.append(json.loads(line))

print('Writing query')
with open('./valid_query.txt', 'w+', encoding='utf8') as file:
    for d in dict_list:
        if 'query' in d.keys():
            file.write(d['query']+'\n')

print('Writing TV...')
with open('./TV.txt', 'w+', encoding='utf8') as file:
    for d in dict_list:
        if 'TV' in d.keys():
            for d_tv in d['TV']:
                file.write(d_tv['str']+'\n')

print('Writing PER...')
with open('./PER.txt', 'w+', encoding='utf8') as file:
    for d in dict_list:
        if 'PER' in d.keys():
            for d_per in d['PER']:
                file.write(d_per['str']+'\n')

print('Writing NUM...')
with open('./NUM.txt', 'w+', encoding='utf8') as file:
    for d in dict_list:
        if 'NUM' in d.keys():
            for d_num in d['NUM']:
                file.write(d_num['str']+'\n')

print('Done!')