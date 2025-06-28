# Notes CRUD endpoints

from flask import Blueprint, jsonify, request 

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
    data = request.get_json()
    content = data.get("content", "")

    if not content:
        return jsonify({"error": "Content is required"}), 400
    return jsonify(
        {
            "message": "This endpoint will let you add a new note",
            "content": content 
        }
    ), 201 

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