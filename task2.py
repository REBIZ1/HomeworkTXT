def get_cook_book(filename: str) -> dict:
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            name = f.readline().strip()
            if not name or name == 'Фахитос':
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


def get_shop_list_by_dishes(dishes: list[str], person_count: int) -> dict:
    cook_book = get_cook_book('recipes.txt')
    menu = {}

    for dish in dishes:
        if dish not in cook_book:
            continue
        for i in cook_book[dish]:
            name = i['ingredient_name']
            quantity = i['quantity'] * person_count
            measure = i['measure']

            if name not in menu:
                menu[name] = {'measure': measure, 'quantity': quantity}
            else:
                menu[name]['quantity'] += quantity
    return menu


result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for i, v in result.items():
    print(i, v)


