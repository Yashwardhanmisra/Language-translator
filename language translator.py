from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
root=Tk()
root.geometry('980x320')
root.resizable(0,0)
root['bg']='skyblue'
root.title('LANGUAGE TRANSLATOR BY YASHWARDHAN')
Label(root,text="Language Translator",font="Arial 20 bold").pack()
Label(root,text="Enter Text You Want To Convert:",font="Arial 13 bold",
    bg='white smoke').place(x=60,y=90)
input_text = Entry(root, width=60)
input_text.place(x=30,y=130)
input_text.get()
Label(root,text="The Converted Text:",font='arial 13 bold',
    bg='white smoke').place(x=600,y=90)
Output_text=Text(root,font='arial 10',height=3,wrap=WORD,padx=5,pady=5,width=50)
Output_text.place(x=550,y=130)
language=list(LANGUAGES.values())
dest_lang=ttk.Combobox(root,values=language,width=22)
dest_lang.place(x=240,y=150)
dest_lang.set('choose language')
def Translate():
    translator=Translator()
    translated=translator.translate(text=input_text.get(),dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
trans_btn=Button(root,text='Translate',font='arial 12 bold',
                pady=5,command=Translate,bg='orange',activebackground='green')
trans_btn.place(x=440,y=200)
root.mainloop()