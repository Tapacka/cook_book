from pprint import pprint

def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, encoding='utf-8') as file:

        for line in file:

            dish_name = line.strip()
            ingredients_quantity = int(file.readline())

            dish_list = []
            for ingr in range(ingredients_quantity):
                ingredient, quantity, unit = file.readline().split('|')

                dish_list.append({"ingredient_name": ingredient, "quantity": int(quantity), "measure": unit.strip()})
            result[dish_name] = dish_list
            file.readline()

    return result


cook_book = prepare_dict("recipes.txt")


# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    res_dict = {}
    for dish_ in dishes:
        for dict2 in cook_book[dish_]:
            count_list = []
            if dict2['ingredient_name'] not in res_dict.keys():
                res_dict[dict2['ingredient_name']] = {'quantity': dict2['quantity'] * person_count,
                                                      'measure': dict2['measure']}
            else:
                r = res_dict[dict2['ingredient_name']]
                count_list.append(r['quantity'])
                res_dict[dict2['ingredient_name']] = {'quantity': sum(count_list) + dict2['quantity'] * person_count,
                                                      'measure': dict2['measure']}
    return res_dict


pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос', 'Фахитос'], 3))