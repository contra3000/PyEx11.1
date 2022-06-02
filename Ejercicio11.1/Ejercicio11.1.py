import sqlite3


def main():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("create table alumnos(id integer, nombre text, apellido text)")

    listaAlumnos = [(1, "María", "Pueyrredon"),
                    (2, "Jorge", "Figueroa"),
                    (3, "José", "Arias"),
                    (4, "Juan", "Gustamante"),
                    (5, "Francisco", "Tejerina"),
                    (6, "Alfredo", "Igarzabal"),
                    (7, "Florencia", "Coronel"),
                    (8, "Sofia", "Cespedes")]

    cursor.executemany("insert into alumnos values(?,?,?)", listaAlumnos)

    conn.commit()

    cursor.execute('SELECT * FROM alumnos WHERE apellido="Gustamante"')
    busquedaAlumno = cursor.fetchone()
    print(busquedaAlumno)

    cursor.close()

    conn.close()


if __name__ == '__main__':
    main()
