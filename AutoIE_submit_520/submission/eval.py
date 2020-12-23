import json
from copy import deepcopy


def get_entities(ent_dict):
    entities = []
    for key in ent_dict.keys():
        if key not in ['id', 'query']:
            for ent in ent_dict[key]:
                entities.append((ent['start_position'], ent['end_position'], key))
    return entities


def evaluate(f_name_pred, f_name_true):
    file_pred = open(f_name_pred, 'r', encoding='utf-8').read().split('\n')
    file_true = open(f_name_true, 'r', encoding='utf-8').read().split('\n')
    dicts_pred, dicts_true = [], []

    for line in file_pred:
        if len(line) == 0:
            continue
        else:
            dicts_pred.append(json.loads(line))

    for line in file_true:
        if len(line) == 0:
            continue
        else:
            dicts_true.append(json.loads(line))
    dicts_pred_temp = deepcopy(dicts_pred)
    dicts_pred = []
    cnt = 0
    for d in dicts_pred_temp:
        if d["query"] in [dd["query"] for dd in dicts_true] and d["id"] not in ['04056', '04243', '04567',
                                                                                '03855', '03907', '04504', '05360', '05776',
                                                                                '09047', '07144', '06500', '06171', '09772',
                                                                                '07407', '07467', '06569', '08691', '01067',
                                                                                '06997']:
            dicts_pred.append(d)
            cnt += 1
    print(cnt)
    assert len(dicts_pred) == len(dicts_true)
    dicts_pred.sort(key=lambda a: a['query'])
    dicts_true.sort(key=lambda a: a['query'])

    true, pred, right = 0, 0, 0

    for i in range(len(dicts_pred)):
        assert dicts_pred[i]["query"] == dicts_true[i]["query"]
        entities_pred = list(set(get_entities(dicts_pred[i])))
        entities_true = list(set(get_entities(dicts_true[i])))
        pred += len(entities_pred)

        true += len(entities_true)
        for one in entities_pred:
            if one in entities_true:
                right += 1
    precision = right * 1.0 / pred if pred > 0 else 0
    recall = right * 1.0 / true if true > 0 else 0
    f1 = (2.0 * precision * recall) / (precision + recall) if precision > 0 or recall > 0 else 0
    return precision, recall, f1


if __name__ == '__main__':
    fname_pred = 'Hermers.json'
    fname_true = 'TestLabel.json'
    p, r, f1 = evaluate(fname_pred, fname_true)
    print(p * 100, r * 100, f1 * 100)

