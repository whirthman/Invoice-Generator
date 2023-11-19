import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from docxtpl import DocxTemplate

root = tk.Tk()


# Centering Window
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = (screen_width - width) // 2
    center_y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{center_x}+{center_y}")

# Create Window
def create_windows():
    # Creatin frame container
    container = tk.Frame(root)
    container.pack(padx=10, pady=20)


    # Task  Functions
    invoice_list = []

    # Clear Item
    def clear_item():
        quantity_spinner.delete(0,tk.END)
        description_entry.delete(0,tk.END)
        unit_price_spinner.delete(0,tk.END)

    # Add Items
    def add_items():
        quantity = int(quantity_spinner.get())
        description = description_entry.get()
        unit_price = int(unit_price_spinner.get())
        total = quantity * unit_price

        items = [quantity, description, unit_price, total]

        invoice_list.append(items)

        tabview.insert("", "end", values=items)   

        clear_item()

    # New Invoice
    def new_invoice():
        firstname_entry.delete(0,tk.END)
        lastname_entry.delete(0,tk.END)
        phone_entry.delete(0,tk.END)
        clear_item()
        tabview.delete(*tabview.get_children())

    # Generate Invoice
    def generate_invoice():
        doc = DocxTemplate("./invoice_template/invoice_template.docx")

        name = firstname_entry.get() + " " + lastname_entry.get()
        phone = phone_entry.get()
        salestax = 0.1
        subtotal = 0
        for items in invoice_list:
             subtotal += items[3]
        print(subtotal)

        total = subtotal - (subtotal * salestax)

        doc.render({
            "name" : name,
            "phone" : phone,
            "invoice_list" : invoice_list,
            "subtotal" : subtotal,
            "salestax" : salestax,
            "total" : total
        })

        # Saving file with windows dialog
        save_path = filedialog.asksaveasfilename(title="Save Invoice As", defaultextension=".docx")
        
        if save_path:
            doc.save(save_path)
            messagebox.showinfo("Success", "Invoice Generated and Saved Successfully!")
            


    # Creating Labels & Input
    # First Row
    # First Name
    firstname_label = tk.Label(container, text="First Name")
    firstname_label.grid(row=0, column=0)

    firstname_entry = tk.Entry(container)
    firstname_entry.grid(row=1, column=0, pady=8)

    # Last Name
    lastname_label = tk.Label(container, text="Last Name")
    lastname_label.grid(row=0, column= 1)

    lastname_entry = tk.Entry(container)
    lastname_entry.grid(row=1, column=1)

    # Phones
    phone_label = tk.Label(container, text="Phone")
    phone_label.grid(row=0, column=2)

    phone_entry = tk.Entry(container)
    phone_entry.grid(row=1, column=2)

    # Second Row
    quantity_label = tk.Label(container, text="Quantity")
    quantity_label.grid(row=3, column=0)

    quantity_spinner = tk.Spinbox(container, from_= 0, to=100)
    quantity_spinner.grid(row=4, column=0, pady=5)

    description_label = tk.Label(container, text="Description")
    description_label.grid(row=3, column=1)

    description_entry = tk.Entry(container)
    description_entry.grid(row=4, column=1)

    unit_price_label = tk.Label(container, text="Unit Price")
    unit_price_label.grid(row=3, column=2)

    unit_price_spinner = tk.Spinbox(container, from_=0, to=10000, increment=0.5)
    unit_price_spinner.grid(row=4, column=2)

    # Row 3 // BTN
    add_items_btn = tk.Button(container, text="Add Item", padx=12, pady=2, command=add_items)
    add_items_btn.grid(row=5, column=2)

    # Row 4 // Table
    columns = ("description", "quantity", "unit_price", "total")
    tabview = ttk.Treeview(container, columns=columns, show="headings")
    tabview.heading("description", text="Description")
    tabview.heading("quantity", text="Quantity")
    tabview.heading("unit_price", text="Unit Price")
    tabview.heading("total", text= "Total")

    tabview.grid(row=6, columnspan=3, padx=16, pady=20)

    # Row 5 / Button
    generate_invoice_btn = tk.Button(container, text="Generate Invoice", padx=2, pady=6, command=generate_invoice)
    generate_invoice_btn.grid(row=7, sticky="news", columnspan=3)

    new_invoice_btn = tk.Button(container, padx=2, pady=6, text="New Invoice", command=new_invoice)
    new_invoice_btn.grid(row=8, sticky="news", columnspan=3, pady=5)


    # Windows Details
    root.title("Invoice Generator App")
    root.iconbitmap("./icon/favicon.ico")    

    # Centering Windows on Screen
    center_window(root, 800, 600)

    # Creating Windows
    root.mainloop()

# Render Windows
create_windows()

