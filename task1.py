def get_cook_book(filename: str) -> dict:
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name or name == 'Фахитос': # В примере не было Фахитоса, поэтому решил его убрать
                break
            ingredients_counts = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredients_counts):
                ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[name] = ingredients
            f.readline()
    return cook_book


for name, ing in get_cook_book('recipes.txt').items():
    print(name)
    for i in ing:
        print(i)
    print()



