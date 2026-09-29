
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

productos = {
    "Laptop": {
        "precio": 15000,
        "descripcion": "Laptop para trabajo y estudio"
    },
    "Mouse Gamer": {
        "precio": 500,
        "descripcion": "Mouse RGB"
    },
    "Teclado Mecánico": {
        "precio": 1200,
        "descripcion": "Teclado gamer"
    },
    "Monitor": {
        "precio": 4000,
        "descripcion": "Monitor Full HD"
    },
    "Audifonos": {
        "precio": 800,
        "descripcion": "Audifonos con microfono"
    }
}


def calcular_total():
    try:
        producto = combo_producto.get()
        cantidad = int(txt_cantidad.get())

        precio = productos[producto]["precio"]

        subtotal = precio * cantidad
        iva = subtotal * 0.16
        total = subtotal + iva

        txt_iva.delete(0, tk.END)
        txt_iva.insert(0, f"{iva:.2f}")

        txt_total.delete(0, tk.END)
        txt_total.insert(0, f"{total:.2f}")

    except:
        pass


def limpiar():
    txt_folio.delete(0, tk.END)
    txt_usuario.delete(0, tk.END)
    txt_cliente.delete(0, tk.END)
    txt_cantidad.delete(0, tk.END)
    txt_iva.delete(0, tk.END)
    txt_total.delete(0, tk.END)

    combo_producto.set("")


def guardar():
    try:
        calcular_total()

        folio = txt_folio.get()
        fecha = datetime.now().strftime("%d/%m/%Y")
        usuario = txt_usuario.get()
        cliente = txt_cliente.get()
        producto = combo_producto.get()
        cantidad = txt_cantidad.get()
        iva = txt_iva.get()
        total = txt_total.get()

        tabla.insert(
            "",
            tk.END,
            values=(
                folio,
                fecha,
                usuario,
                cliente,
                producto,
                cantidad,
                iva,
                total
            )
        )

        carpeta = r"C:\Users\diazc\Documents\trabajosc#"

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        archivo = os.path.join(
            carpeta,
            f"Venta_{folio}.txt"
        )

        with open(archivo, "w", encoding="utf-8") as f:

            f.write("PUNTO DE VENTA TECNOLOGIA\n")
            f.write("-----------------------\n\n")

            f.write(f"Folio: {folio}\n")
            f.write(f"Fecha: {fecha}\n")
            f.write(f"Usuario: {usuario}\n")
            f.write(f"Cliente: {cliente}\n")
            f.write(f"Producto: {producto}\n")
            f.write(f"Cantidad: {cantidad}\n")
            f.write(f"IVA: {iva}\n")
            f.write(f"Total: {total}\n")

        messagebox.showinfo(
            "Guardado",
            "Venta guardada correctamente"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


ventana = tk.Tk()

ventana.title("Punto de Venta Tecnologia")
ventana.geometry("1000x650")
ventana.configure(bg="#D6EAF8")

fuente_titulo = ("Segoe UI", 18, "bold")
fuente = ("Segoe UI", 11)

titulo = tk.Label(
    ventana,
    text="PUNTO DE VENTA TECNOLOGIA",
    bg="#D6EAF8",
    font=fuente_titulo
)
titulo.pack(pady=15)

frame = tk.Frame(
    ventana,
    bg="#D6EAF8"
)
frame.pack()

tk.Label(frame, text="Folio", bg="#D6EAF8", font=fuente).grid(row=0, column=0)
txt_folio = tk.Entry(frame, font=fuente)
txt_folio.grid(row=0, column=1)

tk.Label(frame, text="Usuario", bg="#D6EAF8", font=fuente).grid(row=1, column=0)
txt_usuario = tk.Entry(frame, font=fuente)
txt_usuario.grid(row=1, column=1)

tk.Label(frame, text="Cliente", bg="#D6EAF8", font=fuente).grid(row=2, column=0)
txt_cliente = tk.Entry(frame, font=fuente)
txt_cliente.grid(row=2, column=1)

tk.Label(frame, text="Producto", bg="#D6EAF8", font=fuente).grid(row=3, column=0)

combo_producto = ttk.Combobox(
    frame,
    values=list(productos.keys()),
    font=fuente
)
combo_producto.grid(row=3, column=1)

tk.Label(frame, text="Cantidad", bg="#D6EAF8", font=fuente).grid(row=4, column=0)
txt_cantidad = tk.Entry(frame, font=fuente)
txt_cantidad.grid(row=4, column=1)

tk.Label(frame, text="IVA", bg="#D6EAF8", font=fuente).grid(row=5, column=0)
txt_iva = tk.Entry(frame, font=fuente)
txt_iva.grid(row=5, column=1)

tk.Label(frame, text="Total", bg="#D6EAF8", font=fuente).grid(row=6, column=0)
txt_total = tk.Entry(frame, font=fuente)
txt_total.grid(row=6, column=1)

btn_guardar = tk.Button(
    frame,
    text="Guardar Venta",
    command=guardar,
    bg="#3498DB",
    fg="white",
    font=fuente
)
btn_guardar.grid(row=7, column=0, pady=10)

btn_limpiar = tk.Button(
    frame,
    text="Limpiar",
    command=limpiar,
    bg="#E74C3C",
    fg="white",
    font=fuente
)
btn_limpiar.grid(row=7, column=1)

columnas = (
    "Folio",
    "Fecha",
    "Usuario",
    "Cliente",
    "Producto",
    "Cantidad",
    "IVA",
    "Total"
)

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=10
)

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=110)

tabla.pack(pady=20)

ventana.mainloop()

