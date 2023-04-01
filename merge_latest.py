"""
Merge all json in data/latest into one jsonl file

After:
jskiner --jsonl data/latest.jsonl --nworkers 8 --verbose 1 --out data/latest.schema
"""
import os
import json
import tqdm

INPUT_PATH = 'data/latest'
OUTPUT_PATH = 'data/latest.jsonl'
files = os.listdir(INPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)

with open(OUTPUT_PATH, 'a') as fw:
    for file in tqdm.tqdm(files):
        with open(f'{INPUT_PATH}/{file}', 'r') as fr:
            data = json.load(fr)
        json_str = json.dumps(data)
        fw.write(json_str + '\n')