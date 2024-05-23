class Product:
    """
    Класс для описания товара в магазине
    """

    quantity = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.quantity = quantity

    @classmethod
    def new_product(cls, products):
        return cls(products["name"], products["description"], products["price"], products["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = price


