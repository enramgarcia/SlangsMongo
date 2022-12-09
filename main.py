from pymongo import MongoClient

SERVER = "SERVER"
PORT = "27017"
USER = "root"
PASSWORD = "example"


def seed():
    words = [
        {'word': 'Xopa', 'description': 'Forma coloquial de decir Hola.'},
        {'word': 'Chantin', 'description': 'Casa'}
    ]

    for definition in words:
        result_set = slangs.find_one({"word": definition["word"]})

        if result_set is not None:
            continue

        slangs.insert_one(definition)


def show(word):
    result_set = slangs.find_one({"word": word})

    if result_set is None:
        print(f"No se encontró la palabra: {word}")

    print(result_set)


def show_all():
    for slang in slangs.find():
        print(slang)


def update(word, description):
    result_set = slangs.find_one({"word": word})

    if result_set is None:
        print(f"No se encontró la palabra: {word}")

    slangs.update_one(result_set, {"$set": {'word': word, 'description': description}})


def add():
    word = input('Palabra: ')
    description = input('Definicion: ')

    result_set = slangs.find_one({"word": word})

    if result_set is not None:
        print(f"La palabra, {word}, ya existe")
        return

    slangs.insert_one({"word": word, "description": description})


def delete(word):
    result_set = slangs.find_one({"word": word})

    if result_set is None:
        print(f"No se encontró la palabra: {word}")

    slangs.delete_one(result_set)


if __name__ == '__main__':
    mongo_client = MongoClient(
        f"mongodb://{SERVER}:{PORT}/",
        username=USER,
        password=PASSWORD
    )

    database = mongo_client["slangs"]
    slangs = database["dictionary"]

    seed()

    while True:
        print('Menu')
        print('1- Mostrar todo')
        print('2- Agregar')
        print('3- Buscar palabra')
        print('4- Actualizar palabra')
        print('5- Borrar palabra')
        print('6- Salir')
        option = int(input('Opcion (1-6): '))

        if option == 1:
            show_all()
        elif option == 2:
            add()
        elif option == 3:
            search_word = input('Palabra: ')
            show(search_word)
        elif option == 4:
            search_word = input('Palabra: ')
            update_description = input('Definicion: ')
            update(search_word, update_description)
        elif option == 5:
            search_word = input('Palabra: ')
            delete(search_word)
        else:
            break

