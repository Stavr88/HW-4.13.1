import json

from src.settings import OPERATION_PATH
from utils.category_class import Category
from utils.product_class import Product


def load_json(path: str) -> list[dict]:
    with open(path, encoding="UTF-8") as file:
        return json.load(file)


def creat_list_product(data: list[dict]) -> list[Product]:
    """
    Создаем список экземпляров продукции
    :param data:
    :return:
    """
    list_product = []
    for product in data:
        for prod_1 in product['products']:
            pr = Product(
                name=prod_1['name'],
                description=prod_1['description'],
                price=prod_1['price'],
                quantity=prod_1['quantity']
            )
            list_product.append(pr)
    return list_product


def creat_list_category_product(data: list[dict]) -> list[Category]:
    """
    Создаем список экземпляров категорий продукции
    :param data:
    :return:
    """
    list_product = []
    for cat in data:
        pr = Category(
            name=cat['name'],
            description=cat['description'],
            products=cat['products']
        )
        list_product.append(pr)
    return list_product


if __name__ == "__main__":
    print(load_json(OPERATION_PATH))
    print(creat_list_product(load_json(OPERATION_PATH)))
    print(creat_list_category_product(load_json(OPERATION_PATH)))
    print(creat_list_category_product(load_json(OPERATION_PATH))[0].products)
    print(creat_list_category_product(load_json(OPERATION_PATH))[1].product_count)
