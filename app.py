from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Repositorio temporal de datos
# Esto no representa persistencia de datos
libros = {
    101: {
        "id": 101, "titulo": "Clean Code", "autor": "Robert C. Martin", "disponible": True,
    },
102: {
        "id": 102, "titulo": "Python Crash Course", "autor": "Billie Eilish", "disponible": True,
    },
103: {
        "id": 103, "titulo": "Solo me dejastes baby", "autor": "King Flyp", "disponible": True,
    },
}

@app.get("/")
def inicio():
    return jsonify({
      "mensaje": "API REST de Biblioteca Universitaria",
        "version": 1.0,
        "endpoints": [
            "GET /libros",  # Muestra todos los libros
            "GET /libros/<id>",  # Información de un libro
            "POST /libros",  # Crea un nuevo libro
            "PUT /libros/<id>",  # Modificar la disponibilidad
            "DELETE /libros/<id>"  # Borrar un libro
        ]
    })

@app.get("/libros/<int:id>")
def get_book_by_id(id):
    if id not in libros:
        return make_response(f"El libro con el id {id} no existe", 404)

    return jsonify(libros[id])

@app.get("/libros")
def list_books():
    return jsonify(libros)

@app.post("/libros")
def create_book():
    data = request.get_json()

    id = data.get("id")

    if id in libros:
        return make_response(f"El libro con el identificador {id} ya existe.",409)

    name = data.get("titulo")
    autor = data.get("autor")
    available = data.get("disponible")

    new_book = {
        "id": id,
        "titulo": name,
        "autor": autor,
        "disponible": available
    }

    libros[id] = new_book
    return make_response(f"Libro registrado: {jsonify(new_book)}", 200)


@app.put("/libros")
def update_book():
    data = request.get_json()

    id = data.get("id")

    if id not in libros:
        return make_response(f"El libro con el identificador {id} no existe.",404)

    name = data.get("titulo")
    autor = data.get("autor")
    available = data.get("disponible")

    new_book = {
        "id": id,
        "titulo": name,
        "autor": autor,
        "disponible": available
    }

    libros[id] = new_book
    return make_response(f"Libro registrado: {jsonify(new_book)}", 200)

@app.delete("/libros/<int:id>")
def delete_book(id):
    if id not in libros:
        return make_response(f"El libro con el identificador {id} no existe.",404)

    libros.pop(id, None)

    return make_response(f"Libro con el identificador {id} eliminado", 200)



if __name__ == "__main__":
    app.run(debug=True)