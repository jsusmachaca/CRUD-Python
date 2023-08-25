from tkinter import Tk, Frame, StringVar, Entry, Button, messagebox, Label
from modules.mysql import update_data
from modules.mysql import connection as con


class Edit:
    def __init__(self, parent=None, con=None, id=None):
        self.con = con
        self.id = id
        self.__root = parent
        self.__frame = Frame(self.__root,
                             width=500,
                             height=500,
                             bg='#0f101a')
        self.__frame.pack(expand=True, fill='both')
        self.__Components()
    
    def __str__(self) -> str:
        return 'Done'

    def __Components(self) -> None:
        self.__Frames()
        self.__Labels()
        self.__Entrys()
        self.__Buttons()

    def __Frames(self):
        self.__frame_entrys = Frame(self.__frame)
        self.__frame_entrys.configure(bg='white')
        self.__frame_entrys.place(x=30, y=30)

    def __Labels(self):
        label = Label(self.__frame_entrys)
        label_ape = Label(self.__frame_entrys)
        label_num = Label(self.__frame_entrys)

        label.configure(text='Nombre')
        label.grid(column=0, row=0, sticky='e')

        label_ape.configure(text='Apellido')
        label_ape.grid(column=0, row=1, sticky='e')

        label_num.configure(text='Número')
        label_num.grid(column=0, row=2, sticky='e')


    def __Entrys(self,) -> None:
        self.__name = StringVar()
        self.__ape = StringVar()
        self.__num = StringVar()

        entry_name = Entry(self.__frame_entrys,
                      textvariable=self.__name) 
        entry_name.configure(bg='white')
        entry_name.grid(row=0, column=1)

        entry_ape = Entry(self.__frame_entrys,
                          textvariable=self.__ape)
        entry_ape.configure(bg='white')
        entry_ape.grid(row=1, column=1)

        entry_num = Entry(self.__frame_entrys,
                          textvariable=self.__num)
        entry_num.configure(bg='white')
        entry_num.grid(row=2, column=1)
    
    def __Buttons(self):
        def getData():
            name = self.__name.get()
            ape = self.__ape.get()
            num = self.__num.get()
            data = update_data(self.con, self.id, name, ape, num)
            if data == True:
                messagebox.showinfo('Success', 'Datos insertados correctamente')
                self.__root.destroy()
            else:
                messagebox.showerror('Error', 'Datos no permitidos')

        button = Button(self.__frame)
        button.configure(
            bg='white',
            text='Editar',
            command=getData,)
        button.place(x=35, y=100)