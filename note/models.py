from flask_sqlalchemy import SQLAlchemy


def getNoteModel(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
    db = SQLAlchemy(app)

    class NoteModel(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        body = db.Column(db.String(1000), nullable=False)

        def __repr__(self) -> str:
            return 'Note(id={id}, title={title}, body={body})'

    return db, NoteModel
