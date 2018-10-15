## Usage

```
import async_moip
import aiohttp
import asyncio

async def main(request):
    moip = moipLib.Moip(environment='<production or sandbox', key='<key>', token='<token>')
    customer = await moip.get_order('ORD-W121212121')
    print(customer)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```