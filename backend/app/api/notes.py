# Notes CRUD endpoints

from flask import Blueprint, jsonify

notes_bp = Blueprint("notes", __name__) 

# GET - List Books
@notes_bp.route("/", methods = ["GET"])
def list_books():
    return jsonify(
        {
            "message": "This endpoint will list down all the notes"
        }
    )

# POST - Let you add books
@notes_bp.route("/", methods = ["POST"])
def add_note():
    return jsonify(
        {
            "message": "This endpoint is gonna add a book into the database"
        }
    )

# PUT - Let you update the book
@notes_bp.route("/<id>", methods = ["PUT"])
def update_book(id):
    return jsonify(
        {
            "message": f"This endpoint will let you update a notebook with id {id}" 
        }
    ) 

# DELETE - Let you delete a notebook
@notes_bp.route("/<id>", methods = ["DELETE"])
def delete_note(id):
    return jsonify(
        {
            "message": f"This endpoint will let you delete a notebook with id {id}" 
        }
    ) 