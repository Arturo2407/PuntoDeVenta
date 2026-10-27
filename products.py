import tkinter as tk
from tkinter import messagebox
import csv

PRODUCTS_FILE = "products.csv"

class ProductsApp:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Gestión de Productos")
        self.root.geometry("400x400")

        tk.Label(self.root, text="Gestión de Productos", font=("Arial", 14)).pack(pady=10)

        # Campos de entrada
        tk.Label(self.root, text="Nombre").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Precio").pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()

        tk.Label(self.root, text="Stock").pack()
        self.stock_entry = tk.Entry(self.root)
        self.stock_entry.pack()

        tk.Button(self.root, text="Agregar Producto", command=self.add_product).pack(pady=10)
        tk.Button(self.root, text="Mostrar Productos", command=self.show_products).pack(pady=5)
        tk.Button(self.root, text="Cerrar", command=self.root.destroy).pack(pady=10)

        self.products_list = tk.Text(self.root, width=50, height=10)
        self.products_list.pack()

        self.root.mainloop()

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        stock = self.stock_entry.get()

        if not name or not price or not stock:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número y Stock un entero")
            return

        if self.product_exists(name):
            messagebox.showwarning("Advertencia", "El producto ya existe")
            return

        with open(PRODUCTS_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, price, stock])

        messagebox.showinfo("Éxito", "Producto agregado correctamente")
        self.clear_fields()

    def product_exists(self, name):
        try:
            with open(PRODUCTS_FILE, mode="r") as file:
                reader = csv.reader(file)
                return any(row and row[0].strip().lower() == name.strip().lower() for row in reader)
        except FileNotFoundError:
            return False

    def show_products(self):
        try:
            with open(PRODUCTS_FILE, mode="r") as file:
                reader = csv.reader(file)
                self.products_list.delete("1.0", tk.END)
                self.products_list.insert(tk.END, "Nombre\tPrecio\tStock\n")
                self.products_list.insert(tk.END, "-" * 30 + "\n")
                for row in reader:
                    self.products_list.insert(tk.END, f"{row[0]}\t{row[1]}\t{row[2]}\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "No hay datos disponibles")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)