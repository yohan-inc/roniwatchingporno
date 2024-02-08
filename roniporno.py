import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.messages = True
intents.message_content = True  # Включение intent message_content
intents.guilds = True

# Токен вашего бота
bot_token = "MTIwNTE5NTQyNDEyMjUzNjAyNg.GqeJnr._6JeGaFlfL1ufE2gJp7hXEworXc6037-34SJHY"

# ID канала, который нужно мониторить
source_channel_id = 970741964725186681

# ID канала, куда нужно пересылать сообщения
destination_channel_id = 1205209480716091494

# Создание экземпляра бота
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

# Функция обработчик события "сообщение"
# Функция обработчик события "сообщение"
@bot.event
async def on_message(message):
    # Проверяем, что сообщение пришло из нужного канала и что автор не бот
    if message.channel.id == source_channel_id and not message.author.bot:
        # Получаем объект канала, куда нужно отправить сообщение
        destination_channel = bot.get_channel(destination_channel_id)
        if destination_channel:
            # Отправляем сообщение в другой канал

            msgauthor = message.author.display_name
            msg = message.content
            

            embed = disnake.Embed(
            title="Новая сообщение!!! 300м от вас 😋",
            description=f'Автор: {msgauthor}\n\n{msg}\n',
            color=disnake.Colour.yellow(),
            )

            await destination_channel.send(embed=embed)  # Используем метод send для отправки сообщения

# Запуск бота
bot.run(bot_token)
