import json

def saveOut(df):
    df_out = df.groupby('pass')['aug'].apply(list).reset_index(name='aug')

    passed = []
    for aug in df_out.loc[1]['aug']:
        passed.append({"augmentation": aug, "checks": ["diversity", "fidelity"]})

    failed = []
    for aug in df_out.loc[0]['aug']:
        failed.append({"augmentation": aug, "checks": ["diversity", "fidelity"]})

    out = {}
    out['passed'] = passed
    out['failed'] = failed

    json.dump(out, open('../data/output/output.json', 'w'))
    print('Success!')

def loadData(file_path = '../data/raw/augmentations.json'):
    return json.load(open(file_path, 'r'))