from annotations import HouseAnnotation, ConsumerAnnotation
from const import generate_house_lst, generate_consumer


def get_recommendations(house_lst: list[HouseAnnotation], consumer: ConsumerAnnotation) -> dict[ConsumerAnnotation, HouseAnnotation ]:
    rec_house = [house for house in house_lst if house.price < consumer.account]
    rec_house.sort(key=lambda x: x.square)
    return {"Consumer": consumer, "Recommendations": rec_house[::-1]}

print(get_recommendations(generate_house_lst(10), generate_consumer()))