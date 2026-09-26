lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}
collection_of_coins = {1, 2, 25}

sorted_variables: dict = {}


def sort_variables(**named_variables) -> dict:
    mutable_variables = [list, dict, set]
    immutable_variables = [int, float, str, bool, tuple]

    for value in named_variables.values():
        if type(value) in mutable_variables:
            if "mutable" not in sorted_variables:
                sorted_variables["mutable"] = []
            sorted_variables["mutable"].append(value)
        elif type(value) in immutable_variables:
            if "immutable" not in sorted_variables:
                sorted_variables["immutable"] = []
            sorted_variables["immutable"].append(value)

    return sorted_variables


print(sort_variables(
    lucky_number=lucky_number,
    pi=pi,
    one_is_a_prime_number=one_is_a_prime_number,
    name=name,
    my_favourite_films=my_favourite_films,
    profile_info=profile_info,
    marks=marks,
    collection_of_coins=collection_of_coins
))
