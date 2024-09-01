from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        w = (file.read())
        file.close()
        return w

    def add(self, *products):
        file = open(Shop.__file_name, 'r')
        if len(file.read()) == 1:
            file.close()
            for z in products:
                file = open(Shop.__file_name, 'a')
                file.write(str(z) + '\n')
            file.close()
        else:
            for z in products:
                if z.name not in s1.get_products():
                    file = open(Shop.__file_name, 'a')
                    file.write(str(z) + '\n')
                    file.close()
                else:
                    print(f'Продукт: {z} уже есть ')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(f'\n{p2}\n')  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())





























