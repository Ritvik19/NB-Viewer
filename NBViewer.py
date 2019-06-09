import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tk_html_widgets import HTMLScrolledText
import json

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
with open(filename,encoding="utf-8") as f:
    contents = f.read()

contents_dict = json.loads(contents)

content = ''

for i, x in enumerate(contents_dict['cells']):
    if x['cell_type'] == 'code':
        content += f'<pre style="background-color:#eeeeee">{i+1:{2}} Code:</pre>'
        content += '<pre style="background-color:#b2dfdb">'+''.join(x['source']) + '</pre>'
    else:
        content += f'<pre style="background-color:#eeeeee">{i+1:{2}} Markdown:</pre>'
        content += '<pre style="background-color:#f0f4c3">'+''.join(x['source']) + '</pre>'    
#    print(f'{i+1:{2}} Code:') if x['cell_type'] == 'code' else print(f'{i+1:{2}} Markdown:')
#    print(''.join(x['source']))
    if x['cell_type'] == 'code':
        if len(x['outputs']) > 0:
            op = ''
            for o in x['outputs']:
                if 'text' in o.keys():
                    op += ''.join(o['text']) + '\n'
                elif 'data' in o.keys():
                    op += ''.join(o['data']['text/plain']) + '\n'
#            print(f'\nOutput:\n{op.strip()}')
            content += '<pre style="background-color:#d7ccc8">'+ f'\nOutput:\n{op.strip()}' + '</pre>'
#    print('-'*50)

root = tk.Tk()
root.title('NB Viewer - '+str(filename))
root.state('zoomed')
html_ = HTMLScrolledText(root, html=content)
html_.pack(expand=True)
html_.fit_height()
root.mainloop()
