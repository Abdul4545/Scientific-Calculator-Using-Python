from tkinter import *
import math
from PIL import Image
main = Tk()
main.configure(bg='grey')
main.title("Scientific Calculator")
# photo = PhotoImage(file = "logo.png")
# main.iconphoto(True, photo)

# for input field
entryFiled = Entry(main, font=("arial", 22, "bold"), bg="black",  fg="white", bd=5, width=40)
entryFiled.grid(row=0, column=0, columnspan=7, pady= 22)

# functions for buttons
def click(value):
    try:
        val = entryFiled.get()
        ans = ""
        if(value == "C"):
            val = entryFiled.get()
            val = val[0:len(val)-1]
            entryFiled.delete(0,END)
            entryFiled.insert(0,val)
            return            
        
        elif(value == "Clear"):
            entryFiled.delete(0,END)
        
        elif(value == "sqrt"):
            ans = math.sqrt(eval(val))
            
        elif(value == "π"):
            ans = math.pi
            
        elif(value == "sin"):
            ans = math.sin(math.radians(eval(val)))
            
        elif(value == "cos"):
            ans = math.cos(math.radians(eval(val)))
            
        elif(value == "tan"):
            ans = math.tan(math.radians(eval(val)))
            
        elif(value == "2π"):
            ans = 2 * math.pi
            
        elif(value == "asin"):
            ans = math.asin(eval(val))
            
        elif(value == "acos"):
            ans = math.acos(eval(val))
            
        elif(value == "atan"):
            ans = math.atan(eval(val))
            
        elif(value == "x\u00b2"):
            ans = eval(val) ** 2
        
        elif(value == "ln"):
            ans = math.log2(eval(val)) 
            
        elif(value == "deg"):
            ans = math.degrees(eval(val))
            
        elif(value == "rad"):
            ans = math.radians(eval(val))
        
        elif(value == "e"):
            ans = math.e 
            
        elif(value == "log10"):
            ans = math.log10(eval(val))
            
        elif(value == chr(247)):
            entryFiled.insert(END,"/")
            return
        
        elif(value == "x\u00B3"):
            ans = eval(val) ** 3
                            
        elif(value == "="):
            ans = eval(val)
            
        elif(value == "exp"):
            ans = math.exp(eval(val))
        
        elif(value == "flor"):
            ans = math.floor(eval(val))
            
        elif(value == "Abs"):
            ans = abs(eval(val))
            
        elif(value == "ceil"):
            ans = math.ceil(eval(val))
            
        elif(value =="x\u02b8"):
            entryFiled.insert(END, '**')
            entryFiled.get(val)
        
        else:
            entryFiled.insert(END, value)
            return
               
        entryFiled.delete(0,END)
        entryFiled.insert(0,ans)
        
    except SyntaxError:
        pass
        
#for the values to be on buttons
buttonList = ["Clear", "log10", "(", ")","sin", "cos", "tan", "x\u02b8", "x\u00B3", "x\u00b2", "ln", "//", "/", "%", "asin", "sqrt",  "7", "8", "9", "*", "2π", "acos","Abs", "4", "5", "6", "+", "π", "atan", "ceil", "1", "2", "3", "-", "deg", "C", "flor", "e", "0", ".", "=", "rad"]


rowValue = 1
columnValue = 0

for i in buttonList:
    button = Button(main, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg="black", fg="white", font=("arial", 18, 'bold'), command= lambda button = i: click(button))
    button.grid(row = rowValue, column=columnValue, pady=2, padx=2)
    columnValue = columnValue+1
    if columnValue > 6:
        rowValue = rowValue + 1
        columnValue = 0

main.mainloop()
