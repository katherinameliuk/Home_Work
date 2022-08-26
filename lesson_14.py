from random import randint, sample
from time import sleep


STORAGE = ['apple', 'fish', 'meat', 'water', 'beer', 'honey', 'tomato', 'watermelon', 'milk']
STORAGE_VOLUME = len(STORAGE)


def menu() -> list:
    menu_list = sample(STORAGE, randint(3, STORAGE_VOLUME))
    return menu_list    # ['honey', 'water', 'beer', 'watermelon', 'milk', 'meat', 'tomato']


def create_recipe(menu_list: list) -> dict:
    recipe_products = sample(menu_list, randint(3, len(menu_list)))
    products_count = [randint(10, 200) for _ in range(len(recipe_products))]
    recipe = dict(zip(recipe_products, products_count))
    return recipe


def cook(recipe: dict) -> str:
    print("Cooking...")
    sleep(5)
    return f"Dish with {recipe} ready. Bon appetite!"



menu_store = menu()
print(menu_store)

recipe = create_recipe(menu_store)
print(recipe)

print(cook(recipe))


