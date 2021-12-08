from tkinter import ttk
from system.views.abstract_view import AbstractView


class CustomerView(AbstractView):
    def __init__(self, root, frame, controller):
        self.root = root
        self.frame = frame
        self.controller = controller
        self.setup_view()

    def setup_view(self):
        user_name = self.controller.access_controller.user.get_user_name()
        self.root.title("Wholesaler System - " + user_name)
        self.load_labels()
        self.load_interactions()

    def load_labels(self):
        product_label = ttk.Label(self.frame, text="Choose a product")
        product_label.grid(row=0, column=0, padx=10, pady=10)
        product_quantity_label = ttk.Label(self.frame, text="Quantity")
        product_quantity_label.grid(row=0, column=2, padx=10, pady=10)

    def load_interactions(self):
        product_combobox = ttk.Combobox(self.frame, width=34, state="readonly",
                                        textvariable=self.controller.input["product_name"])
        product_combobox["values"] = self.controller.fill_products()
        product_combobox.grid(row=0, column=1, pady=10)
        product_quantity_entry = ttk.Entry(self.frame, width=18,
                                           textvariable=self.controller.input["product_quantity"])
        product_quantity_entry.grid(row=0, column=3, padx=10, pady=10)
        product_tree_view = ttk.Treeview(self.frame, column=("c1", "c2", "c3"),
                                         show='headings', height=21)
        product_tree_view.column("c1", width=190)
        product_tree_view.column("c2", width=85)
        product_tree_view.column("c3", width=85)
        product_tree_view.heading("c1", text="Product Name")
        product_tree_view.heading("c2", text="Quantity")
        product_tree_view.heading("c3", text="Price")
        product_tree_view.grid(row=1, rowspan=5, column=0, columnspan=2, padx=10, pady=2)
        add_product_button = ttk.Button(self.frame, width=20, text="Add to Basket", command=lambda:
                                        self.controller.add_product(product_tree_view))
        add_product_button.grid(row=1, column=2, columnspan=3, padx=10)
        remove_product_button = ttk.Button(self.frame, width=20, text="Remove from Basket",
                                           command=lambda:
                                           self.controller.remove_product(product_tree_view))
        remove_product_button.grid(row=2, column=2, columnspan=3, padx=10)
        checkout_button = ttk.Button(self.frame, width=20, text="Checkout",
                                     command=lambda: self.controller.checkout(product_tree_view))
        checkout_button.grid(row=3, column=2, columnspan=3, padx=10)
        log_out_button = ttk.Button(self.frame, width=20, text="Logout",
                                    command=self.controller.logout_user())
        log_out_button.grid(row=5, column=2, columnspan=3, padx=10)

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
