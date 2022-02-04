from flask_restful import fields

noteFields = {
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String,
}
