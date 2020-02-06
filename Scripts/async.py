async def ola():
    return 'Olaa'

async def get_ola():
    ret = await ola()
    print(ret)


