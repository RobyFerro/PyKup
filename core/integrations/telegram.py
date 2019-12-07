import telegram.ext

from modules import env


class TelegramBot:

	def __init__(self, config_file):
		self.config = env.get_config(config_file)["TELEGRAM_BOT"]
		self.bot = telegram.Bot(token=self.config["ACCESS_TOKEN"])
		self.updater = telegram.ext.Updater(self.config["ACCESS_TOKEN"])

	def send_confirm_message(self, message):
		self.bot.send_message(chat_id=self.config['USER_ID'], text=message)

	def start_polling(self):
		self.updater.start_polling()
