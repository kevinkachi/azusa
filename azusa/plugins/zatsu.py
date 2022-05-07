from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Message, MessageSegment

#帮助信息
help = on_keyword(['/help'],priority = 5)
@help.handle()
async def help_handle():
    help_msg = "/help 【帮助信息】 \n"
    help_msg +="来点二次元 或者 ldecy 【随机二次元图片】 \n"
    help_msg +="/echo 【复读（需@bot）】"
    await help.finish(help_msg)

#随机二次元图片
some_nijigenn = on_keyword(['ldecy','来点二次元'],priority = 20)
@some_nijigenn.handle()
async def some_nijigenn_handle():
    msg1 = '二次元来辣~'
    msg2 = MessageSegment.image('https://www.dmoe.cc/random.php')
    msg = msg1 + msg2
    await some_nijigenn.finish(msg)
