from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('JF-Ar - ToDo List')
root.geometry("400x600")

#Define Font

font_app = Font(
    family="Helvetica Neue Ultra Leve", 
    size= 27 )

#Create frame
app_frame = Frame(root)
app_frame.pack(pady=10)

#crate listbox
app_list = Listbox(
    app_frame, font=font_app,
    width=25, height=5,
    bg="SystemButtonFace", bd=0,
    fg="#464646", highlightthickness= 0,
    selectbackground="#652a62", activestyle="none"
)

app_list.pack(side=LEFT, fill=BOTH)

# fictitious list
things_to_do = ['Ler a Biblia', 'Ler um Livro', 'Estudar Python', 'Estudar Django', 'Lavar a Louça', 'Jantar']
#add in listbox
for item in things_to_do:
    app_list.insert(END, item)

#scroll
app_scroll = Scrollbar(app_frame)
app_scroll.pack(side=RIGHT, fill=BOTH)

app_list.config(yscrollcommand=app_scroll.set)
app_scroll.config(command=app_list.yview)

#box to add items
box_add = Entry(root, font=("Helvetica Neue Estreito", 20))
box_add.pack(pady=20)

#button for app/frame
button_app = Frame(root)
button_app.pack(pady=20)

def delet_item():
    app_list.delete(ANCHOR)

def add_item():
    app_list.insert(END, box_add.get())
    box_add.delete(0, END)

def check_item():
    app_list.itemconfig(
        app_list.curselection(),
        fg="#dedede"
    )
    app_list.selection_clear(0, END)

def uncheck_item():
    app_list.itemconfig(
        app_list.curselection(),
        fg="#464646"
    )
    app_list.selection_clear(0, END)

def delet_check_item():
    cont = 0
    while cont < app_list.size():
        if app_list.itemcget(cont, "fg") == "#dedede":
            app_list.delete(app_list.index(cont))

        cont += 1

#other buttons
delet_button = Button(button_app, text='Deletar item', command=delet_item) 
add_button = Button(button_app, text='Adcionar item', command=add_item) 
check_item_button = Button(button_app, text='Item concluído', command=check_item)
uncheck_item_button = Button(button_app, text='Desfazer item concluído', command=uncheck_item)
delet_check_item_button = Button(button_app, text='Excluir intem concluído', command=delet_check_item)

delet_button.grid(row=0, column=0)
add_button.grid(row=1, column=0, pady=20)
check_item_button.grid(row=0, column=1)
uncheck_item_button.grid(row=1, column=1,padx=20, pady=20)
delet_check_item_button.grid(row=2, column=0)
root.mainloop()