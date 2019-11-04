## aiowirecard

Asyncio wirecard API wrapper based on [moip](https://pypi.org/project/moip/) providing asyncronous requests.

## Usage
```bash
$ export WIRECARD_KEY=<your_wirecard_key>
$ export WIRECARD_TOKEN=<your_wirecard_token>
```
```python
import aiowirecard
import aiohttp
import asyncio

async def main():
    wirecard = aiowirecard.Wirecard(environment='<production or sandbox', key='<key>', token='<token>')
    order = await wirecard.get_order('ORD-W121212121')
    print(order)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
## Functions 

```python
post_customer(parameters) # create new customer 
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
