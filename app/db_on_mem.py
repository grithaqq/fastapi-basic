class Product():
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id} {self.name} {self.price}"
    

class ListProduct():
    products = []

    def get_products(self):
        return self.products
    
    def add_product(self, product):
        self.products.append(product.model_dump(exclude_unset=True))
        return f"{product.name} was added"
    
    
    def update_product(self, product_id: int, new_product: Product):
        for index, product in enumerate(self.products):
            print(self.products[index]['id'] == int(product_id))
            if int(product_id) == self.products[index]['id']:
                self.products[index] = new_product.model_dump(exclude_unset=True)
                return f"product was updated"
        return "product is not found"

    
    def delete_product(self, product_id: int):
        for index, product in enumerate(self.products):
            if int(product_id) == self.products[index]['id']:
                self.products.pop(index)
                return f"product was deleted"
        return "product is not found"
        
db_product = ListProduct()