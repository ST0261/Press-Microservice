from flask import Blueprint, render_template, abort, jsonify, request
from Email_Generator import generator


press_router = Blueprint('press_api', 
                                import_name=__name__, 
                                url_prefix='/press/informative')


@press_router.route('/')
def index():
    return "press informative component"

'''

{
            "emails":[
                {
                    "subject": "Estamos en temporada!",
                    "content": "Vamos ha hacer maldades"
                },
                {
                    "subject": "Ya no",
                    "content": "No para dale"
                }
            ]
}
'''
@press_router.route('/send', methods=['POST'])
def send_comunicated():
    data = request.get_json()
    return jsonify(generator.send(data))