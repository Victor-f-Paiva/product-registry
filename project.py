import tkinter as tk
from tkinter import ttk

# save list
save_list = []
def save(name_entry:tk.Entry, type_un_entry:tk.Entry, qtt_entry:tk.Entry, price_entry:tk.Entry):
    code = f'{len(save_list)+1:04d}'
    product = name_entry.get()
    type_u = type_un_entry.get()
    qtt = qtt_entry.get()
    price = price_entry.get()
    save_list.append((code, product, type_u, qtt, price))


def open_registry():
    ...

def main():
    #list of types of units
    list_types_of_units = ["pcs", "pack", "box", "kg"]

    # init the window and add a title
    root = tk.Tk()
    root.title("Product Registration")

    # product description and entry
    product_name_label = tk.Label(text="Product Name")
    product_name_label.grid(row=1, column=0, padx=10, pady=10, columnspan=6, sticky="nswe")
    product_name_entry = tk.Entry()
    product_name_entry.grid(row=2, column=0, padx=10, pady=10, columnspan=6, sticky="nswe")

    # types of units for the product (piece, pack, box, kilogram) and entry
    type_of_unit_label = tk.Label(text="Unit Type")
    type_of_unit_label.grid(row=3, column=0, padx=10, pady=10, columnspan=1, sticky="nswe")
    type_of_unit_entry = ttk.Combobox(values=list_types_of_units)
    type_of_unit_entry.grid(row=3, column=2, padx=10, pady=10, columnspan=3, sticky="nswe")

    # quantity of products and entry
    quantity_label = tk.Label(text="Quantity")
    quantity_label.grid(row=4, column=0, padx=10, pady=10, columnspan=1, sticky="nswe")
    quantity_entry = tk.Entry()
    quantity_entry.grid(row=4, column=2, padx=10, pady=10, columnspan=3, sticky="nswe")

    # price and entry
    price_label = tk.Label(text="Price - US$")
    price_label.grid(row=5, column=0, padx=10, pady=10, columnspan=1, sticky="nswe")
    price_entry = tk.Entry()
    price_entry.grid(row=5, column=2, padx=10, pady=10, columnspan=3, sticky="nswe")

    #save, quit and open buttom
    save_buttom = tk.Button(
        text="Save", 
        command= lambda: save(
            name_entry=product_name_entry, 
            type_un_entry=type_of_unit_entry, 
            qtt_entry= quantity_entry, 
            price_entry=price_entry))
    save_buttom.grid(row=6, column=0, padx=10, pady=10, columnspan=2, sticky="nswe")

    quit_buttom = tk.Button(text="Quit", command=root.destroy)
    quit_buttom.grid(row=6, column=2, padx=10, pady=10, columnspan=2, sticky="nswe")
    
    root.mainloop()


if __name__ == "__main__":
    main()
    print(save_list)