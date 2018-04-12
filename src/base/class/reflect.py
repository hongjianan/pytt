# coding: UTF-8


def reflect_tt():
    animal_model = __import__("animal", fromlist = False)
    Animal = getattr(animal_model, "Animal")
    animal = Animal()
    get_age = getattr(animal, "get_age")
    grow = getattr(animal, "grow")
    age = getattr(animal, "age")
    get_count = getattr(Animal, "get_count")
    print(get_count())

    print(age, get_age())
    grow()
    print(age, get_age())

    age = getattr(animal, "age")
    print(age, get_age())


def run():
    reflect_tt()


if __name__ == "__main__":
    run()
    

