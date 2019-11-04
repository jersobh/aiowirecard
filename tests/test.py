import asyncio
import json
import os
import random

import aiowirecard


async def main():
    wirecard = aiowirecard.Wirecard(environment='sandbox', key=os.environ['WIRECARD_KEY'],
                                    token=os.environ['WIRECARD_TOKEN'])
    print('Creating customer...')
    customer = {
        "ownId": "%0.11d" % random.randint(0, 99999999999),
        "fullname": "Maria Oliveira",
        "email": "maria@email.com",
        "birthDate": "1980-5-10",
        "taxDocument": {
            "type": "CPF",
            "number": "%0.11d" % random.randint(0, 99999999999)
        },
        "phone": {
            "countryCode": "55",
            "areaCode": "11",
            "number": "22226842"
        },
        "shippingAddress": {
            "city": "Rio de Janeiro",
            "district": "Ipanema",
            "street": "Avenida Atlântica",
            "streetNumber": "60",
            "zipCode": "02446000",
            "state": "RJ",
            "country": "BRA"
        },
        "fundingInstrument": {
            "method": "CREDIT_CARD",
            "creditCard": {
                "expirationMonth": "06",
                "expirationYear": "22",
                "number": "6362970000457013",
                "cvc": "123",
                "holder": {
                    "fullname": "Maria Oliveira",
                    "birthdate": "1980-05-10",
                    "taxDocument": {
                        "type": "CPF",
                        "number": "10013390023"
                    },
                    "billingAddress": {
                        "city": "Rio de Janeiro",
                        "district": "Copacabana",
                        "street": "Rua Raimundo Corrêa",
                        "streetNumber": "1200",
                        "zipCode": "05246200",
                        "state": "RJ",
                        "country": "BRA"
                    },
                    "phone": {
                        "countryCode": "55",
                        "areaCode": "11",
                        "number": "22226842"
                    }
                }
            }
        }
    }
    print('Customer data: ', customer)
    create_user = await wirecard.post_customer(parameters=customer)
    user_id = json.loads(create_user)['id']
    print('Customer id: ', user_id)
    get_user = await wirecard.get_customer(user_id)
    print('Customer info:', get_user)
    order = {
        "ownId": "%0.11d" % random.randint(0, 99999999999),
        "amount": {
            "currency": "BRL",
            "subtotals": {
                "shipping": 1500
            }
        },
        "items": [
            {
                "product": "Descrição do pedido",
                "category": "CLOTHING",
                "quantity": 1,
                "detail": "Camiseta estampada branca",
                "price": 9500
            }
        ],
        "customer": {
            "id": user_id
        }
    }
    new_order = await wirecard.post_order(order)
    print('Creating an order... ')
    order_id = json.loads(new_order)['id']
    print('Order id: ', order_id)
    order = await wirecard.get_order(order_id)
    print('Getting order info: ', order)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
