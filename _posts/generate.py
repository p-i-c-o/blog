from datetime import datetime
import os

def get_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date

def create(filename, content):
    with open(filename, 'w+') as f:
	     f.write(content)
	     f.close()

date = get_current_date()
title = input('Article title >>> ')
tags =  input('Article tags  >>> ').split(' ')
img =   input('Image name    >>> ')

template = f"""---
title: {title}
tags: {tags}
author: me
image: https://github.com/p-i-c-o/p-i-c-o.github.io/blob/main/img/{img}.png?raw=true
---
"""

filen = date+"-"+title.replace(' ', '-')+".md"

create(filen, template)

os.system(f'nano {filen}')
