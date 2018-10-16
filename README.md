## async_moip
asyncio/aiohttp (Python3.5+) Moip API wrapper based on [moip](https://pypi.org/project/moip/) providing asyncronous requests.

## Usage

```python
import async_moip
import aiohttp
import asyncio

async def main(request):
    moip = async_moip.Moip(environment='<production or sandbox', key='<key>', token='<token>')
    order = await moip.get_order('ORD-W121212121')
    print(order)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
## Functions 

```python
post_customer(params) # create new customer 
get_customer(parameters) # get customer data
post_creditcard(customer_id, parameters) # add new credit card to customer account
delete_creditcard(creditcard_id) # delete credit card
post_order(parameters) # create a new order
get_order(order_id) # get order by id
post_payment(order_id, parameters) # create a payment
get_payment(payment_id) # get payment data by id
capture_payment(payment_id) # capture of a preauthorized payment
void_payment(payment_id) # cancel the capture of a preauthorized payment
account_exists(account_id) # check if account exists
```
### params examples [here](https://dev.moip.com.br/page/api-reference)