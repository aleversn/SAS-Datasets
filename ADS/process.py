# %%
import json

with open('./question.csv', encoding='utf-8') as f:
    ori_list = f.read().split('\n')

if ori_list[-1] == '':
    ori_list = ori_list[1:-1]
else:
    ori_list = ori_list[1:]

result = []

for item in ori_list:
    line = item.split('\t')
    id, title, ref = line[0], line[1], line[2]
    filename = './answer/{}.json'.format(id)
    with open(filename, encoding='utf-8') as answer_f:
        answers = answer_f.read()
    answers = json.loads(answers)
    for obj in answers:
        score = obj['score']
        answer = obj['answer'].replace('\n', '')
        result.append([id, title, ref, score, answer])

# %%
with open('./ori.csv', 'w+', encoding='utf-8') as f:
    f.write("")

with open('./ori.csv', 'a', encoding='utf-8') as f:
    for item in result:
        f.write('\t'.join(item) + '\n')

# %%
# 格式化数据集
import json
import random

result = []
question_dict = []
with open('question.csv', encoding='utf-8') as f:
    question_dict = f.readlines()
question_dict = question_dict[1:]

for q_item in question_dict:
    q_item = q_item.split('\t')
    id, question, ref = q_item[0], q_item[1], q_item[2]
    ref2 = q_item[3] if len(q_item) > 3 else ''
    ref3 = q_item[4] if len(q_item) > 4 else ''
    with open('answers/{}.json'.format(id), encoding='utf-8') as f:
        answer_dict = json.load(f)
    for answer_item in answer_dict:
        answer_item['q_id'] = id
        answer_item['question'] = question
        answer_item['reference1'] = ref.strip()
        answer_item['reference2'] = ref2.strip()
        answer_item['reference3'] = ref3.strip()
        result.append(answer_item)

with open('all.jsonl', 'w', encoding='utf-8') as f:
    for item in result:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

random.shuffle(result)

train_set = result[:int(len(result) * 0.7)]
test_set = result[int(len(result) * 0.7):]

with open('train.jsonl', 'w', encoding='utf-8') as f:
    for item in train_set:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

with open('test.jsonl', 'w', encoding='utf-8') as f:
    for item in test_set:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

# %%
