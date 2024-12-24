class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        with open(self.__file_name, 'a'):
            pass

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        existing_products = self.get_products()
        added_products = []

        for product in products:
            product_line = str(product)
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                added_products.append(product_line)

        if added_products:
            with open(self.__file_name, 'a') as file:
                file.writelines(f"{line}\n" for line in added_products)


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
