import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

SALES_FILE = "sales.csv"
PRODUCTS_FILE = "products.csv"
CUSTOMERS_FILE = "customers.csv"

class SalesApp:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Gestión de Ventas")
        self.root.geometry("500x500")
        
        tk.Label(self.root, text="Gestión de Ventas", font=("Arial", 14)).pack(pady=10)
        
        # Campos de selección
        tk.Label(self.root, text="Cliente").pack()
        self.customer_var = tk.StringVar()
        self.customer_menu = tk.OptionMenu(self.root, self.customer_var, *self.load_customers())
        self.customer_menu.pack()
        
        tk.Label(self.root, text="Producto").pack()
        self.product_var = tk.StringVar()
        self.product_menu = tk.OptionMenu(self.root, self.product_var, *self.load_products())
        self.product_menu.pack()
        
        tk.Label(self.root, text="Cantidad").pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()
        
        tk.Button(self.root, text="Registrar Venta", command=self.add_sale).pack(pady=10)
        tk.Button(self.root, text="Mostrar Ventas", command=self.show_sales).pack(pady=5)
        tk.Button(self.root, text="Cerrar", command=self.root.destroy).pack(pady=10)
        
        self.sales_list = tk.Text(self.root, width=60, height=15)
        self.sales_list.pack()
        
        self.root.mainloop()
    
    def load_customers(self):
        try:
            with open(CUSTOMERS_FILE, mode="r") as file:
                reader = csv.reader(file)
                return [row[0] for row in reader]
        except FileNotFoundError:
            return []
    
    def load_products(self):
        try:
            with open(PRODUCTS_FILE, mode="r") as file:
                reader = csv.reader(file)
                return [row[0] for row in reader]
        except FileNotFoundError:
            return []
    
    def add_sale(self):
        customer = self.customer_var.get()
        product = self.product_var.get()
        quantity = self.quantity_entry.get()
        
        if not customer or not product or not quantity:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return
        
        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero")
            return
        
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(SALES_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([customer, product, quantity, date])
        
        messagebox.showinfo("Éxito", "Venta registrada correctamente")
        self.quantity_entry.delete(0, tk.END)
    
    def show_sales(self):
        try:
            with open(SALES_FILE, mode="r") as file:
                reader = csv.reader(file)
                self.sales_list.delete("1.0", tk.END)
                self.sales_list.insert(tk.END, "Cliente\tProducto\tCantidad\tFecha\n")
                self.sales_list.insert(tk.END, "-" * 50 + "\n")
                for row in reader:
                    self.sales_list.insert(tk.END, f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "No hay datos disponibles")
