from flask import Blueprint, jsonify, request 
from db.mongodb_service import MongoDBService

mongo_client = MongoDBService() 

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
    try:
        content = request.get_json()
        if not content:
            return jsonify(
                {
                    "message": "Content is required to add a note."
                }
            ), 400
        id = mongo_client.upload_content(content = content) 
        if not id:
            return jsonify(
                { 
                    "message": "Failed to add the note."
                }
            ), 500
        return jsonify(
            {
                "message": "Note added successfully!",
                "note": content, 
                "note_id": str(id) 
            }
        ), 201 
    except Exception as e:
        return jsonify(
            {
                "message": f"An error occurred while adding the note: {str(e)}"
            }
        ), 500

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