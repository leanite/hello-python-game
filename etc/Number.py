import random


class Number:

    @staticmethod
    def round(number: float) -> int:
        return round(number)

    @staticmethod
    def random_with_lower_zero(limit: int) -> int:
        return Number.__generate_random(0, limit - 1)

    @staticmethod
    def random_with_lower_one(limit: int) -> int:
        return Number.__generate_random(1, limit)

    @staticmethod
    def __generate_random(lower: int, limit: int) -> int:
        return random.randint(lower, limit)