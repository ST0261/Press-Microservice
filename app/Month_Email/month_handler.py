from flask import Blueprint, render_template, abort, jsonify, request
import requests
from Email_Generator import generator

press_router_month = Blueprint('press_api_month', 
                                import_name=__name__, 
                                url_prefix='/press/month')

@press_router_month.route('/')
def index():
    return "press month component"


@press_router_month.route('/send')
def send_month():
    res_get = requests.get('http://fiel.tk/discounts/products/month_products')
    status, data = res_get.status_code, res_get.json()

    content = getEmailContent(data['products_discount'])

    generator.send({"emails":
                [
                    {
                        "subject": "Descuentos del mes!",
                        "content": content
                    }
                ]
            }
        )

    return jsonify({'status':'ok'})

def getEmailContent(data):
    body ='<table style="width:100%">'
    body = body + "<tr><th>Product name</th><th>Discount</th><th>SoyLocatel</th></tr>" + '\n'

    for element in data:
        body = body + '<tr>'+ '\n'
       

        product = requests.get('http://3.86.32.97/posts/' + str(element['_id']))
        product = product.json()['product']

        body = body + '<th>'+ product + '</th>' + '\n'
        body = body + '<th>'+ str(element['discount']) + '</th>' + '\n'
        body = body + '<th>'+ str(element['discount']) + '</th>' + '\n'

        body = body + '</tr>' +'\n'
    
    body = body + '</table>' +'\n'
    
    print(body)

    return body



    