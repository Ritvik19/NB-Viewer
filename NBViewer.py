from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
with open(filename) as f:
    contents = f.read()

contents_dict = json.loads(contents)

for i, x in enumerate(contents_dict['cells']):
    print(f'{i+1:{2}} Code:') if x['cell_type'] == 'code' else print(f'{i+1:{2}} Markdown:')
    print(''.join(x['source']))
    if x['cell_type'] == 'code':
        if len(x['outputs']) > 0:
            op = ''
            for o in x['outputs']:
                if 'text' in o.keys():
                    op += ''.join(o['text']) + '\n'
                elif 'data' in o.keys():
                    op += ''.join(o['data']['text/plain']) + '\n'
            print(f'\nOutput:\n{op.strip()}')
    print('-'*50)
