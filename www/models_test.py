import orm, asyncio
from models import User,Blog, Comment

async def test():
    await orm.create_pool(loop=loop, user='root', password='root', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank')

    await u.save()

# 获取EventLoop
loop = asyncio.get_event_loop()
# 把协程丢到EventLoop中执行
loop.run_until_complete(test())
# 关闭EventLoop
loop.close()

