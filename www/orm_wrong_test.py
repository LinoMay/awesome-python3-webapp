from orm import Model, StringField, IntegerField, create_pool
import asyncio 

class User(Model):
    __table__ = 'user'
    id = IntegerField(primary_key=True)
    name = StringField()

if __name__ == '__main__':

    u = User(id=123, name='Lino')
    print(u.id)
    print(u.name)
    loop = asyncio.get_event_loop()
    dt_dict = {'user': 'root', 'password': 'root', 'db': 'test'}
    tasks = [create_pool(loop, **dt_dict ), u.save()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_forever()