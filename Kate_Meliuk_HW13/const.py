from random import randint
from models import House, Consumer
from annotations import HouseAnnotation, ConsumerAnnotation

NAMES = ["Alex", "Jhon", "Peter", "Victor", "James", "Oliver"]
NAMES_COUNT = len(NAMES)

def generate_house_lst(house_count: int) -> list[HouseAnnotation]:
    house_lst = []
    for _ in range(1, house_count):
        house_lst.append(House(price=randint(10_000, 250_000), square=randint(25, 200)))
    return house_lst

def generate_consumer() -> ConsumerAnnotation:
    consumer = Consumer(name=NAMES[randint(0, NAMES_COUNT - 1)], account=randint(10_000, 250_000))
    return consumer