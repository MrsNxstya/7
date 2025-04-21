cars = {
    "Toyota Camry": {"hp": 133, "price": 12000},
    "Honda Civic": {"hp": 98, "price": 9500},
    "Ford Focus": {"hp": 110, "price": 10000},
    "BMW 320i": {"hp": 150, "price": 16000},
    "Skoda Octavia": {"hp": 105, "price": 11500},
    "Renault Clio": {"hp": 75, "price": 7000},
    "Mazda 6": {"hp": 145, "price": 12500},
    "Kia Rio": {"hp": 90, "price": 8800},
    "Audi A4": {"hp": 170, "price": 18500},
    "Volkswagen Golf": {"hp": 102, "price": 9900}
}

def show_all_data(cars_dict):
    for model, info in cars_dict.items():
        print(f"{model}: Потужність = {info['hp']} к.с., Вартість = {info['price']}$")

def add_car(cars_dict, model, hp, price):
    cars_dict[model] = {"hp": hp, "price": price}
    print(f"Автомобіль {model} додано.")

def delete_car(cars_dict, model):
    if model in cars_dict:
        del cars_dict[model]
        print(f"Автомобіль {model} видалено.")
    else:
        print(f"Автомобіль {model} не знайдено.")

def show_sorted_cars(cars_dict):
    for model in sorted(cars_dict.keys()):
        info = cars_dict[model]
        print(f"{model}: Потужність = {info['hp']} к.с., Вартість = {info['price']}$")

def total_price_above_100hp(cars_dict):
    total = sum(info['price'] for info in cars_dict.values() if info['hp'] > 100)
    print(f"Загальна вартість авто з потужністю понад 100 к.с.: {total}$")
    return total

print("=== Усі автомобілі ===")
show_all_data(cars)

print("\n=== Сортований список автомобілів ===")
show_sorted_cars(cars)

print("\n=== Додаємо новий автомобіль ===")
add_car(cars, "Hyundai Elantra", 108, 9700)

print("\n=== Після додавання ===")
show_all_data(cars)

print("\n=== Видаляємо автомобіль Renault Clio ===")
delete_car(cars, "Renault Clio")

print("\n=== Після видалення ===")
show_all_data(cars)

print("\n=== Обчислення загальної вартості авто з потужністю понад 100 к.с. ===")
total_price_above_100hp(cars)
