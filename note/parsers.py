from flask_restful import reqparse

note_parser = reqparse.RequestParser(bundle_errors=True)
note_parser.add_argument('title', required=True,
                         type=str, help='note need title')
note_parser.add_argument('body', required=True,
                         type=str, help='note need body text')
