import tkinter as tk
from tkinter import messagebox
import csv

CUSTOMERS_FILE = "customers.csv"

class CustomersApp:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Gestión de Clientes")
        self.root.geometry("400x400")

        tk.Label(self.root, text="Gestión de Clientes", font=("Arial", 14)).pack(pady=10)

        # Campos de entrada

        tk.Label(self.root, text="Nombre").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Email").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        tk.Label(self.root, text="Teléfono").pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        tk.Button(self.root, text="Agregar Cliente", command=self.add_customer).pack(pady=10)
        tk.Button(self.root, text="Mostrar Clientes", command=self.show_customers).pack(pady=5)
        tk.Button(self.root, text="Cerrar", command=self.root.destroy).pack(pady=10)

        self.customers_list = tk.Text(self.root, width=50, height=10)
        self.customers_list.pack()

        self.root.mainloop()

    def add_customer(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not email or not phone:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        with open(CUSTOMERS_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone])

        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        self.clear_fields()

    def show_customers(self):
        try:
            with open(CUSTOMERS_FILE, mode="r") as file:
                reader = csv.reader(file)
                self.customers_list.delete("1.0", tk.END)
                self.customers_list.insert(tk.END, "Nombre\tEmail\tTeléfono\n")
                self.customers_list.insert(tk.END, "-" * 40 + "\n")
                for row in reader:
                    self.customers_list.insert(tk.END, f"{row[0]}\t{row[1]}\t{row[2]}\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "No hay datos disponibles")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
