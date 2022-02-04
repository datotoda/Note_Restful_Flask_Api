from flask import Flask
from flask_restful import Resource, Api, abort, marshal_with
from models import getNoteModel
from parsers import note_parser
from fields import noteFields

app = Flask(__name__)
api = Api(app)
db, NoteModel = getNoteModel(app)


class Notes(Resource):
    # Read All
    @marshal_with(noteFields)
    def get(self):
        return NoteModel.query.all(), 200


class Note(Resource):
    # Read
    @marshal_with(noteFields)
    def get(self, note_id):
        note = self.note_or_abort_if_note_doesnt_exist(note_id)

        return note, 200

    # Create
    @marshal_with(noteFields)
    def post(self, note_id):
        if NoteModel.query.filter_by(id=note_id).first() is not None:
            abort(404, message=f"Note {note_id} already exist")
        args = note_parser.parse_args()

        if args['title'] != '' and args['body'] != '':
            note = NoteModel(id=note_id, **args)
            db.session.add(note)
            db.session.commit()
            return note, 201

        abort(406, message=f"Fill fields")

    # Update
    @marshal_with(noteFields)
    def put(self, note_id):
        note = self.note_or_abort_if_note_doesnt_exist(note_id)
        args = note_parser.parse_args()

        if args['title'] != '' and args['body'] != '':
            note.title = args['title']
            note.body = args['body']
            db.session.commit()
            return note, 202

        abort(406, message=f"Fill fields")

    # Delete
    def delete(self, note_id):
        note = self.note_or_abort_if_note_doesnt_exist(note_id)
        db.session.delete(note)
        db.session.commit()
        return {"message": "Deleted!"}, 200

    @staticmethod
    def note_or_abort_if_note_doesnt_exist(note_id):
        note = NoteModel.query.filter_by(id=note_id).first()
        if note is None:
            abort(404, message=f"Note with id={note_id} doesn't exist")
        else:
            return note


api.add_resource(Notes, '/notes')
api.add_resource(Note, '/note/<int:note_id>')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
