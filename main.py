from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import webbrowser
from win10toast import ToastNotifier
from utils.logger import Logger

class Overwatch:
	contenders = "https://overwatchleague.com/en-us/contenders"
	league = "https://overwatchleague.com/en-us/"
	support = "https://discord.com/invite/skWQrNgXtS"

	Logger.info("Проверяем есть ли стримы Overwatch Contenders и Overwatch League")

	def contenders_parsing(self):
		try:
			options = Options()
			options.headless = True
			driver = webdriver.Firefox(options=options, executable_path=r'C:\webDrivers\geckodriver.exe')
			driver.get(self.contenders)
			hr = ToastNotifier()


			full_page = driver.page_source
			soup = BeautifulSoup(full_page, "html.parser")
			items = soup.find_all("h2", {"class": "section-titlestyles__Title-sc-1wlp19u-3", "class": "bJDlju"})

			if items[0].text == "Live now":
				Logger.info("Стрим Overwatch Contenders найден! Открываю страничку")
				hr.show_toast("Успешно!", "Стрим по Overwatch Contenders найден! Открываю страничку")
				webbrowser.open(self.contenders)
				overwatchleague = Overwatch()
				overwatchleague.league_parsing()
			else:
				Logger.error("Стрим по Overwatch Contenders не найден! Проверю через 5 минут")
				hr.show_toast("Упс...", "Стрим по Overwatch Contenders не найден!")
				time.sleep(300)
				overwatchleague = Overwatch()
				overwatchleague.contenders_parsing()

		except Exception as err:
			Logger.error("Произошла неизвестная ошибка! \n"
						f"Ошибка - {err} \n"
						"Открываю саппорт сервер через 3 секунды... \n"
						"Советуем вам перезапустить код...")
			hr.show_toast("Произошла ошибка", "Подробности смотреть в консоле!")

			time.sleep(3)
			webbrowser.open(self.support)
			overwatchleague = Overwatch()
			overwatchleague.contenders_parsing()

	def league_parsing(self):
		try:
			options = Options()
			options.headless = True
			driver = webdriver.Firefox(options=options, executable_path=r'C:\webDrivers\geckodriver.exe')
			driver.get(self.contenders)
			hr = ToastNotifier()

			full_page = driver.page_source
			soup = BeautifulSoup(full_page, "html.parser")
			items = soup.find_all("h2", {"class": "section-titlestyles__Title-sc-1wlp19u-3", "class": "bJDlju"})

			if items[0].text == "Live Now": 
				Logger.info("Стрим Overwatch League найден! Открываю страничку")
				hr.show_toast("Успешно!", "Стрим по Overwatch League найден! Открываю страничку")

				webbrowser.open(self.league)
				overwatchleague = Overwatch()
				overwatchleague.contenders_parsing()

			else:
				Logger.error("Стрим по Overwatch League не найден! Проверю через 5 минут")
				hr.show_toast("Упс...", "Стрим по Overwatch League не найден!")
				time.sleep(300)
				overwatchleague = Overwatch()
				overwatchleague.league_parsing()

		except Exception as err:
			Logger.error("Произошла неизвестная ошибка! \n"
						f"Ошибка - {err} \n"
						"Открываю саппорт сервер через 3 секунды... \n"
						"Советуем вам перезапустить код...")
			hr.show_toast("Произошла ошибка", "Подробности смотреть в консоле!")

			time.sleep(3)
			webbrowser.open(self.support)
			overwatchleague = Overwatch()
			overwatchleague.league_parsing()

overwatchleague = Overwatch()
overwatchleague.contenders_parsing()
overwatchleague.league_parsing()
