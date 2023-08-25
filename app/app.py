from tkinter import Tk, Frame, Label, Entry, Button, StringVar, messagebox, Toplevel
from tkinter.font import Font
from modules.mysql import connection as con
from modules.mysql import insert_data, show_all, delete_data
from app.edit import Edit

class Window:
    def __init__(self) -> None:
        self.fonts = '..resources/fonts/PressStart2P.ttf'
        self.__root = Tk()
        self.__root.title('Hola mundo')
        self.__root.resizable(False, False)
        self.font = Font(family='Press Start 2P')
        self.__frame = Frame(self.__root,
                             width=1000,
                             height=720,
                             border='5',
                             relief='solid',
                             bg='#0f101a',)
        self.__frame.pack(
            expand=True,
            fill='both',)
        self.__Components()
        self.__mainloop = self.__root.mainloop()

    def __Components(self) -> None:
        self.__Frames()
        self.__Labels()
        self.__Entrys()
        self.__Table()
        self.__Buttons()
    
    def __Labels(self) -> None:
        label = Label(self.__frame)
        label.configure(
            text='Gestion de Personal',
            fg='#e80058',
            bg='#2D3044',
            padx=237,
            pady=10,
            font=(self.font, 20),)
        label.place(x=0, y=0)

    def __Frames(self):
        self.__frame_table = Frame(self.__frame)
        self.__frame_table.configure(width=300, height=400, bg='#939395',)
        self.__frame_table.place(x=30, y=80)

        self.__frame_entrys = Entry(self.__frame)
        self.__frame_entrys.place(x=700, y=80)

    def __Table(self) -> None:
        if con():

            def edit_data(id):
                edit_window = Toplevel()
                Edit(edit_window, con(), id)
                edit_window.wait_window(edit_window)
                self.updating_table()

            def del_data(id):
                message = messagebox.askyesno('.', '¿Estás seguro que quieres eliminar este usuario?')
                if message:
                    delete_data(con(), id)
                    self.updating_table()
                else:
                    return
            
            data = show_all(con())

            def headers() -> None:
                header_id = Label(self.__frame_table)
                header_id.configure(
                    text='Id',
                    font=('JetBrainsMono Nerd Font', 14),
                    bg='#383845',
                    fg='#ffffff',
                    padx=15,
                    pady=5,)
                header_id.grid(row=0, column=0)

                header_name = Label(self.__frame_table)
                header_name.configure(
                    text='Nombre',
                    font=('JetBrainsMono Nerd Font', 14),
                    bg='#383845',
                    fg='#ffffff',
                    padx=15,
                    pady=5,)
                header_name.grid(row=0, column=1)

                header_ape = Label(self.__frame_table)
                header_ape.configure(
                    text='Apellido',
                    font=('JetBrainsMono Nerd Font', 14),
                    bg='#383845',
                    fg='#ffffff',
                    padx=15,
                    pady=5,)
                header_ape.grid(row=0, column=2)

                header_num = Label(self.__frame_table)
                header_num.configure(
                    text='Número',
                    font=('JetBrainsMono Nerd Font', 14),
                    bg='#383845',
                    fg='#ffffff',
                    padx=15,
                    pady=5,)
                header_num.grid(row=0, column=3)
                
                header_action = Label(self.__frame_table)
                header_action.configure(
                    text='Acción',
                    font=('JetBrainsMono Nerd Font', 14),
                    bg='#383845',
                    fg='#ffffff',
                    padx=15,
                    pady=5,)
                header_action.grid(row=0, column=4)

            def buildTable() -> None:
                for i, d in enumerate(data):
                    id = Label(self.__frame_table)
                    name = Label(self.__frame_table)
                    ape = Label(self.__frame_table)
                    num = Label(self.__frame_table)

                    id.configure(
                        text=d[0],
                        bg='#939395',
                        padx=15,
                        pady=5,
                        width=2,)
                    id.grid(row=i+1, column=0, sticky='w')

                    name.configure(
                        text=d[1],
                        bg='#939395',
                        padx=15,
                        pady=5,
                        width=9,)
                    name.grid(row=i+1, column=1, sticky='w')

                    ape.configure(
                        text=d[2],
                        bg='#939395',
                        padx=15,
                        pady=5,
                        width=9,)
                    ape.grid(row=i+1, column=2, sticky='w')

                    num.configure(
                        text=d[3],
                        bg='#939395',
                        padx=15,
                        pady=5,
                        width=9,)
                    num.grid(row=i+1, column=3, sticky='w')

                    delete = Button(self.__frame_table)
                    delete.configure(
                        text='Delete',
                        bg='red',
                        padx=10,
                        pady=5,
                        command=lambda d0=d[0]: del_data(d0),)
                    delete.grid(row=i+1, column=5)

                    edit = Button(self.__frame_table)
                    edit.configure(
                        text='Edit',
                        bg='Blue',
                        padx=10,
                        pady=5,
                        command=lambda d0=d[0]: edit_data(d0),)
                    edit.grid(row=i+1, column=4)
            headers()
            buildTable()
        else:
            messagebox.showerror('Error', 'Ocurrió un error al conectar con la base de datos')

    def updating_table(self):
        for w in self.__frame_table.winfo_children():
            w.destroy()
        self.__Table()

    def __Entrys(self) -> None:
        self.__name = StringVar()
        self.__ape = StringVar()
        self.__num = StringVar()

        entry_name = Entry(self.__frame_entrys,
                      textvariable=self.__name) 
        entry_name.configure(bg='white')
        entry_name.grid(row=0, column=0)

        entry_ape = Entry(self.__frame_entrys,
                          textvariable=self.__ape)
        entry_ape.configure(bg='white')
        entry_ape.grid(row=1, column=0)

        entry_num = Entry(self.__frame_entrys,
                          textvariable=self.__num)
        entry_num.configure(bg='white')
        entry_num.grid(row=2, column=0)

    def __Buttons(self) -> None:
        def get_data():
            if con():
                name = self.__name.get()
                ape = self.__ape.get()
                num = self.__num.get()
                result = insert_data(con(), name, ape, num)
                if result == True:
                    self.updating_table()
                    messagebox.showinfo('.', 'Datos insertados correctamente')
                    self.__name.set('')
                    self.__ape.set('')
                    self.__num.set('')
                else:
                    messagebox.showwarning('.', 'Datos no permitidos')
            else:
                messagebox.showerror('Error', 'No puedes insertar datos mientras no haya conexión')

        button = Button(self.__frame, 
                        command=get_data)
        button.configure(
            bg='white',
            text='Insertar',)
        button.place(
            x=550,
            y=350,)