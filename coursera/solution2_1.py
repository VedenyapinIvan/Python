import os
import tempfile
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')


print('key - {}, val - {}'.format(parser.parse_args().key, parser.parse_args().val))

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

data = json.load(open(storage_path))
if parser.parse_args().val is None:
    print(', '.join(data[parser.parse_args().key]))
else:
    data[parser.parse_args().key].append(parser.parse_args().val)
    # with open(storage_path, 'w') as f:
    #     print(data)
    # json.dump(storage_path, data)

print('full --> {}'.format(data))
