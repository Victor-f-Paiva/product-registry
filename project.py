import tkinter as tk
from tkinter import ttk
import datetime as dt


def save():
    ...


def quit():
    ...


def open_registry():
    ...

def main():
    #list of types of units
    list_types_of_units = ["pcs", "pack", "box", "kg"]

    # init the window and add a title
    root = tk.Tk()
    root.title("Product Registration")

    # product description and entry
    product_name_label = tk.Label(text="Product Name").grid(row=1, column=0, padx=10, pady=10, columnspan=6, sticky="nswe")
    product_name_entry = tk.Entry().grid(row=2, column=0, padx=10, pady=10, columnspan=6, sticky="nswe")

    # types of units for the product (piece, pack, box, kilogram) and entry
    type_of_unit_label = tk.Label(text="Unit Type").grid(row=3, column=0, padx=10, pady=10, columnspan=1, sticky="nswe")
    type_of_unit_entry = ttk.Combobox(values=list_types_of_units).grid(row=3, column=2, padx=10, pady=10, columnspan=3, sticky="nswe")

    # quantity of products and entry
    quantity_label = tk.Label(text="Quantity").grid(row=4, column=0, padx=10, pady=10, columnspan=1, sticky="nswe")
    quantity_entry = tk.Entry().grid(row=4, column=2, padx=10, pady=10, columnspan=3, sticky="nswe")

    # price and entry
    price_label = tk.Label(text="Price - US$").grid(row=5, column=0, padx=10, pady=10, columnspan=1, sticky="nswe")
    price_entry = tk.Entry().grid(row=5, column=2, padx=10, pady=10, columnspan=3, sticky="nswe")

    #save, quit and open buttom
    save_buttom = tk.Button(text="Save").grid(row=6, column=0, padx=10, pady=10, columnspan=2, sticky="nswe")
    
    root.mainloop()


if __name__ == "__main__":
    main()