class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_list = [x for x in self.products if x.startswith(first_letter)]
        return filtered_list

    def __repr__(self):
        sorted_products = sorted(self.products)
        products_str = '\n'.join(sorted_products)
        return f"Items in the {self.name} catalogue:\n{products_str}"
