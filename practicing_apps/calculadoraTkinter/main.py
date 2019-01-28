from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68

class CalcDisplay(ttk.Frame):
    __value = "0"
    # __contComas = 0
    __hayComa = False
    
    def __init__(self, parent, **args):
        
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn * 4)
        self.pack_propagate(0)
        
        s = ttk.Style()
        s.configure('my.TLabel', font=('Helvetica', 42))
        self.__lbl = ttk.Label(self, text=self.__value, style='my.TLabel', anchor=E)
        
        self.__lbl.pack(fill=BOTH, expand=1)
    
    def reset(self):
        self.__value = '0'
        self.__hayComa = False
        self.__lbl.config(text=self.__value)
    
    def getValue(self):
        resultado = self.__value.replace(',', '.')
        try:
            return float(resultado)
        except Exception:
            return 0

    def setValue(self, value):
        try:
            float(value)
            value = str(value)
            value = value.replace('.', ',')
            
            self.__hayComa = ',' in value
            
            self.__value = value
            self.__lbl.config(text=self.__value)
            
        except Exception:
            pass
        
    def __concatena(self, value):
        self.__value += value
        self.__lbl.config(text=self.__value)

    def addDigit(self, value):
        '''
        if self.__value == '0':
            if value.isdigit():
                self.__value = value      
                self.__lbl.config(text=value)
        else:
            if value.isdigit():
                self.__concatena(value)
        '''
        
        if value.isdigit():
            if self.__value == '0':
                self.__value = value      
                self.__lbl.config(text=value)
            else:
                self.__concatena(value)

        if value == ',':
            if not self.__hayComa:
                self.__hayComa = True
                self.__concatena(value)
                
        print("value: {}".format(self.__value))


class CalcButton(ttk.Frame):
    __initProperties = None
    
    def __init__(self, parent, **args):
        self.__initProperties = args
        
        ttk.Frame.__init__(self, parent, height=_heightBtn * self.__getArg("cHeight", 1), width=_widthBtn * self.__getArg("cWidth", 1))
        self.pack_propagate(0)
        
        self.__btn = ttk.Button(self, text=args["text"], command=self.__getArg("command"))
        self.__btn.pack(fill=BOTH, expand=1)

    def __getArg(self, nameArg, default=None):
        if nameArg in self.__initProperties:
            return self.__initProperties[nameArg]
        else:
            return default
        
class MainApp(Tk):
    
    __v1 = 0
    __v2 = 0
    __op = ""
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry("272x300")
        
        CalcButton(self, text="0", cWidth=2, command=lambda: self.numberDisplay("0")).place(x=0, y=250)
        CalcButton(self, text="1", command=lambda: self.numberDisplay("1")).place(x=0, y=200)
        CalcButton(self, text="2", command=lambda: self.numberDisplay("2")).place(x=68, y=200)
        CalcButton(self, text="3", command=lambda: self.numberDisplay("3")).place(x=136, y=200)
        CalcButton(self, text="4", command=lambda: self.numberDisplay("4")).place(x=0, y=150)
        CalcButton(self, text="5", command=lambda: self.numberDisplay("5")).place(x=68, y=150)
        CalcButton(self, text="6", command=lambda: self.numberDisplay("6")).place(x=136, y=150)
        CalcButton(self, text="7", command=lambda: self.numberDisplay("7")).place(x=0, y=100)
        CalcButton(self, text="8", command=lambda: self.numberDisplay("8")).place(x=68, y=100)
        CalcButton(self, text="9", command=lambda: self.numberDisplay("9")).place(x=136, y=100)
        
        CalcButton(self, text="C", cWidth=2, command=self.test).place(x=0, y=50)
        CalcButton(self, text="+/-").place(x=136, y=50)
        CalcButton(self, text="÷", command=lambda: self.opera('/')).place(x=204, y=50)
        CalcButton(self, text="x", command=lambda: self.opera('x')).place(x=204, y=100)
        CalcButton(self, text="-", command=lambda: self.opera('-')).place(x=204, y=150)
        CalcButton(self, text="+", command=lambda: self.opera('+')).place(x=204, y=200)
        CalcButton(self, text="=").place(x=204, y=250)
        CalcButton(self, text=",", command=lambda: self.numberDisplay(",")).place(x=136, y=250)
        
        self.__display = CalcDisplay(self)
        self.__display.place(x=0, y=0)

    def test(self):
        print("Por aquí pasa")

    def start(self):
        self.mainloop()
        
    def numberDisplay(self, numberValue):
        print(numberValue)
        self.__display.addDigit(numberValue)
    
    def opera(self, operador):
        if self.__v1 == 0:
            self.__v1 = self.__display.getValue()
            self.__op = operador
            self.__display.reset()
        else:
            self.__v2 = self.__display.getValue()
            if self.__op == '+':
                total = self.__v1 + self.__v2
            elif self.__op == '-':
                total = self.__v1 - self.__v2
            elif self.__op == 'x':
                total = self.__v1 * self.__v2
            elif self.__op == '/':
                total = self.__v1 / self.__v2
            self.__display.setValue(total)
            #Actualizar estado
            self.__op = operador
            self.__v1 = total
            self.__v2 = 0
            

        
    def add(self):
        if self.__v1 == 0:
            self.__v1 = self.__display.getValue()
            self.__op = '+'
            self.__display.reset()
        else:
            self.__v2 = self.__display.getValue()
            if self.__op == '+':
                total = self.__v1 + self.__v2
                self.__display.setValue(total)
            
        print('v1: {}, v2: {}, op: {} '.format(self.__v1, self.__v2, self.__op))
        
        
        
if __name__ == '__main__':
    calc = MainApp()
    calc.start()