import tkinter as tk

def calcular(total,porcentaje):
    total=float(total)
    resultado.config(text=f"Propina: ${((porcentaje*total)/100)}") 

root= tk.Tk()
root.title("Calculadora")

titulo=tk.Label(root,text="Calculadora de propinas")

entrada=tk.Entry(root)
resultado=tk.Label(root)

boton_10=tk.Button(root,text="10%",command=lambda: calcular(entrada.get(),10))
boton_20=tk.Button(root,text="20%", command=lambda: calcular(entrada.get(),20))
boton_50=tk.Button(root,text="50%", command=lambda: calcular(entrada.get(),50))


titulo.pack()
entrada.pack()
boton_10.pack()
boton_20.pack()
boton_50.pack()
resultado.pack()
root.mainloop()