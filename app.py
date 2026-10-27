import tkinter as tk

from products import ProductsApp
from customers import CustomersApp
from sales import SalesApp

class MainMenuApp :
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Tienda")
        self.root.geometry("300x300")

        self.CrearTitulo()
        self.CrearMenu()
        self.CrearPiePagina()

    def CrearTitulo(self) :
        print("Creando titulo...")
        frameTitulo = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        frameTitulo.pack(pady=10, fill= "x")
        tk.Label(frameTitulo, text="Menú Principal", font=("Arial",16), bg="lightblue").pack()

    def CrearMenu(self) :
        print("Creando Menu...")
        frameMenu = tk.Frame(self.root, bg="lightgreen", padx=10, pady=10)
        frameMenu.pack(pady=10, fill= "x")

        tk.Button(frameMenu, text="Productos", command=self.openProductos, width=25, bg="skyblue", fg="black").pack(pady=5)
        tk.Button(frameMenu, text="Clientes", command=self.openClientes, width=25, bg="skyblue", fg="black").pack(pady=5)
        tk.Button(frameMenu, text="Ventas", command=self.openVentas, width=25, bg="skyblue", fg="black").pack(pady=5)

    
    def CrearPiePagina(self) :
        print("Creando pie de pagina...")
        framePie = tk.Frame(self.root, bg="lightcoral", padx=10, pady=10)
        framePie.pack(pady=10, fill= "x")

        tk.Button(framePie, text="Salir", command=self.close, width=25, bg="tomato", fg="white").pack(pady=5)

    def openProductos(self) :
        print("Abriendo ventana Productos...")
        ProductsApp()

    def openClientes(self) :
        print("Abriendo ventana Clientes...")
        CustomersApp()
    
    def openVentas(self) :
        print("Abriendo ventana Ventas...")
        SalesApp()

    def close(self) :
        print("Cerrando sesión...")
        self.root.quit()

def main() :
    root = tk.Tk()
    #Instancia de una clase
    app = MainMenuApp(root)
    root.mainloop()

if __name__ == "__main__" :
    main()
    
    
print("Hola papus")