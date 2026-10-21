from src.tavern import Tavern
from src.customer import Customer
from src.adventurer import Adventurer
from src.troublemaker import Troublemaker


def main():
    tavern = Tavern("П'яний дракон")

    # Створення відвідувачів
    lira = Customer("Ліра", "Ельф", 50, "Медовуха")
    aragorn = Adventurer("Арагорн", "Людина", 200, 5)
    grumble = Troublemaker("Грумбл", "Гоблін", 20, 8)
    gimli = Customer("Гімлі", "Гном", 120, "Темний ель")

    for visitor in (lira, aragorn, grumble, gimli):
        tavern.add_visitor(visitor)

    print(tavern)
    print()

    print("Усі відвідувачі:")
    for v in tavern.get_all():
        print(v)
    print()

    print("Поліморфізм - кожен замовляє своє:")
    for line in tavern.serve_all():
        print(line)
    print()

    print("Унікальні методи підкласів:")
    print(aragorn.tell_story())
    print(grumble.start_fight())
    print()

    print("Пошук 'гном':")
    for v in tavern.search("гном"):
        print(v)
    print()

    print("Тільки пригодники:")
    for v in tavern.filter_by_type(Adventurer):
        print(v)
    print()

    print("Відвідувачі з золотом >= 100:")
    for v in tavern.filter_by_min_gold(100):
        print(v)
    print()

    print("Сортування за золотом (від більшого):")
    for v in tavern.sort_by_gold(reverse=True):
        print(v)
    print()

    print(f"Сума чайових: {tavern.total_tips()}")
    print()

    print("Видалення Грумбла")
    tavern.remove_visitor(grumble)
    print(tavern)
    print()

    print("Спроба додати неправильний тип:")
    try:
        tavern.add_visitor("Це не відвідувач")
    except TypeError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()