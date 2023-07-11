from datetime import datetime

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

template = f"""title: {title}
tags: {tags}
author: me
"""

create(date+"-"+title.replace(' ', '-')+".md", template)
