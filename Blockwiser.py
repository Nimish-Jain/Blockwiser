from __future__ import with_statement                                                            
from tkinter import *
import contextlib 
  
try: 
    from urllib.parse import urlencode           
  
except ImportError: 
    from urllib import urlencode 
try: 
    from urllib.request import urlopen 
  
except ImportError: 
    from urllib2 import urlopen 
  
import sys 

window = Tk()
window.geometry('1250x500+30+30')
window.configure(bg='#2475B0')
window.title('Blockwiser')

url = ''
respp = ''

def make_tiny(url): 
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))     
    with contextlib.closing(urlopen(request_url)) as response:                       
        return response.read().decode('utf-8 ')          


def get_link():
	global url
	global respp
	url = link_entry.get()

	res = url[:23] + '.' + url[23:]
	ans_box = Text (window)
	respp = make_tiny(res)
	
	ans_box.insert(INSERT, respp)
	ans_box.place(x = 530, y = 265 , width=250, height=25)

title_label = Label(window, text = "Blockwiser", bg='#2475B0', fg = 'White',font=("Courier", 44)).place(x=300,y=65, width=700, height=75)

text_label = Label(window, text = "Enter Video URL to get AD-Free URL", bg='#2475B0', fg = 'White',font=("Courier", 14)).place(x=300,y=145, width=700, height=25)

link_entry = Entry(window)
link_entry.place(x = 500, y = 180 , width=330, height=25)

Ans_button = Button(window,text = "Get URL", command = get_link ).place(x = 605, y = 220 , width=110 , height=25)

window.mainloop()
