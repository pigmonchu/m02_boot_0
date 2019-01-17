from tkinter import *
from tkinter import ttk, font
import getpass

_PADDING = 10

def aceptar():
    global clave, userTxt, pwdTxt
    
    
    if clave.get() == 'tkinter':
        print("Acceso permitido")
        print("Usuario: {}\nClave: {}".format(userTxt.get(), pwdTxt.get()))
    else:
        print("Acceso denegado")


#Creamos ventana
mainWindow = Tk()
mainWindow.title("Acceso")

#Creamos widgets (controles)
fuente = font.Font(weight='bold')

userLabel = ttk.Label(mainWindow, text="Usuario:", font=fuente)
pwdLabel = ttk.Label(mainWindow, text="Contraseña:", font=fuente)

usuario = StringVar()
clave = StringVar()

usuario.set(getpass.getuser())

userTxt = ttk.Entry(mainWindow, textvariable=usuario, width=30)
pwdTxt = ttk.Entry(mainWindow, textvariable=clave, width=30, show="*")

separ1 = ttk.Separator(mainWindow, orient=HORIZONTAL)

btnAceptar = ttk.Button(mainWindow, text="Aceptar", command=aceptar)
btnCancel = ttk.Button(mainWindow, text="Cancelar", command=quit)


# Situar widgets en ventana

userLabel.pack(side=TOP, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)
userTxt.pack(side=TOP, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)

pwdLabel.pack(side=TOP, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)
pwdTxt.pack(side=TOP, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)

separ1.pack(side=TOP, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)

btnAceptar.pack(side=LEFT, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)
btnCancel.pack(side=LEFT, fill=BOTH, expand=True, padx=_PADDING, pady=_PADDING)

# Posicionar el cursor en un control determinado
userTxt.focus_set()

mainWindow.mainloop()
