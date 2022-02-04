# Note Restful Api

This is a Restful Api written on Flask where you can send GET, POST, PUT and DELETE requests for notes CRUD operations. Used flask, flask-restful, flask-sqlalchemy.

---

# Documentations

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
  
- [Flask Restful Documentation](https://flask-restful.readthedocs.io/en/latest/index.html)
  
- [Flask Sqlalchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

# Install requirements

``$ pip install -r requirements.txt``

# Examples

Get all notes

``$ curl --request GET "{URL}/notes"``

Get note by id

``$ curl --request GET "{URL}/note/{id}"``

Create note by id

``$ curl --request POST "{URL}/note/{id}" --form "title={title}" --form "body={body}"``

Update note by id

``$ curl --request PUT "{URL}/note/{id}" --form "title={title}" --form "body={body}"``

Delete note by id

``$ curl --request Delete "{URL}/note/{id}"``