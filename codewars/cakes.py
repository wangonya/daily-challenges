# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python


def cakes(recipe: dict, available: dict) -> int:
    recipe_items = list(recipe.keys())
    available_items = list(available.keys())

    if not all(item in available_items for item in recipe_items):
        return 0

    result = []

    for item in recipe_items:
        print(f"item = {item}")
        n = available[item] // recipe[item]
        result.append(n)

    return min(result)


if __name__ == "__main__":
    # must return 2
    result = cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
    print(result)

    # must return 0
    result = cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
    print(result)

# return min(available.get(k, 0)/recipe[k] for k in recipe)
