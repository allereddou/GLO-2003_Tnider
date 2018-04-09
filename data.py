from server import *
from persistance.tableCleanup import createTables, deleteAllTables
from persistance.insertRandomUsers import insertUsers
from persistance.insertRandomAnimals import insertAnimal
from persistance.imageLinks import insertBirbPics


with app.app_context():

    def setupDatabase():
        # ouverture connexion
        cursor = get_db()

        # supprimer les tables
        deleteAllTables(cursor)
        createTables(cursor)

        # insérer des users
        insertUsers(cursor, 100)

        # insérer des animaux
        insertAnimal(cursor, 100)

        # insérer des photos d'oiseaux
        insertBirbPics(cursor)


    setupDatabase()

    sql = "SELECT * FROM user"
    cursor = get_db()

    cursor.execute(sql)
    for row in cursor:
        if row['email'] == 'admin@hotmail.com':
            print(row)
