from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import webbrowser
from win10toast import ToastNotifier
from utils.logger import Logger
#Здесь был Вася
class Overwatch:
    	contenders = "https://overwatchleague.com/en-us/contenders"
	league = "https://overwatchleague.com/en-us/"
	support = "https://discord.com/invite/skWQrNgXtS"

	Logger.info("Проверяем есть ли стримы Overwatch Contenders и Overwatch League")

	def contenders_parsing(self):
		try:
			options = Options()
			options.headless = True
			driver = webdriver.Firefox(options=options, executable_path=r'C:\webDrivers\geckodriver.exe') #Файл нужно добавить в патч, ищите в гугле под свой браузер
			driver.get(self.contenders)
			hr = ToastNotifier()
			isLive = False

			full_page = driver.page_source
			soup = BeautifulSoup(full_page, "html.parser")
			items = soup.find_all("h3", {"class": "video-playerstyles__LiveText-sc-14q9if3-9", "class": "iJdBvU"})

			if not len(items) == 0 and items[0].text == "Live Now":
				if isLive:
					Logger.info(
						"Стрим Overwatch Conteders успешно найден! Но скорей всего он уже открыт, я не стану открывать повторно страничку! Иду проверять Overwatch League \n"
						f"Если страничка не открыта то вот ссылка - {self.contenders}")
					hr.show_toast("Успешно...", "Подробности смотреть в консоле")
					driver.quit()

					overwatchleague = Overwatch()
					overwatchleague.league_parsing()
				if not isLive:
					Logger.info("Стрим Overwatch Contenders найден! Открываю страничку")
					hr.show_toast("Успешно!", "Стрим по Overwatch Contenders найден! Открываю страничку")
					webbrowser.open(self.contenders)
					driver.quit()
					isLive = True
					overwatchleague = Overwatch()
					overwatchleague.league_parsing()

			else:
				Logger.error("Стрим по Overwatch Contenders не найден! Проверю через 5 минут, иду проверять Overwatch League")
				hr.show_toast("Упс...", "Стрим по Overwatch Contenders не найден!")
				isLive = False
				driver.quit()
				overwatchleague = Overwatch()
				overwatchleague.league_parsing()
				time.sleep(300)
				overwatchleague.contenders_parsing()

		except Exception as err:
			Logger.error("Произошла неизвестная ошибка! \n"
						f"Ошибка - {err} \n"
						"Перезапуск кода...")
			hr.show_toast("Произошла ошибка", "Подробности смотреть в консоле!")
			driver.quit()
			overwatchleague = Overwatch()
			overwatchleague.contenders_parsing()

	def league_parsing(self):
		try:
			options = Options()
			options.headless = True
			driver = webdriver.Firefox(options=options, executable_path=r'C:\webDrivers\geckodriver.exe')
			driver.get(self.league)
			hr = ToastNotifier()
			isLive = False

			full_page = driver.page_source
			soup = BeautifulSoup(full_page, "html.parser")
			items = soup.find_all("h3", {"class": "video-playerstyles__LiveText-sc-14q9if3-9", "class": "iJdBvU"})


			if not len(items) == 0 and items[0].text == "Live Now":
				if isLive:
					Logger.info("Стрим Overwatch League успешно найден! Но скорей всего он уже открыт, я не стану открывать повторно страничку! Иду проверять Overwatch Conteders \n"
								f"Если страничка не открыта то вот ссылка - {self.league}")
					hr.show_toast("Успешно...", "Подробности смотреть в консоле")
					driver.quit()

					overwatchleague = Overwatch()
					overwatchleague.contenders_parsing()
				if not isLive:
					Logger.info("Стрим Overwatch League найден! Открываю страничку")
					hr.show_toast("Успешно!", "Стрим по Overwatch League найден! Открываю страничку")
					webbrowser.open(self.contenders)
					driver.quit()
					isLive = True
					overwatchleague = Overwatch()
					overwatchleague.contenders_parsing()

			else:
				Logger.error("Стрим по Overwatch League не найден! Проверю через 5 минут иду проверять Overwatch conteders")
				hr.show_toast("Упс...", "Стрим по Overwatch League не найден!")
				isLive = False
				driver.quit()
				overwatchleague = Overwatch()
				overwatchleague.contenders_parsing()
				time.sleep(300)
				overwatchleague.league_parsing()

		except Exception as err:
			Logger.error("Произошла неизвестная ошибка! \n"
						f"Ошибка - {err} \n"
						"Перезапуск кода...")
			hr.show_toast("Произошла ошибка", "Подробности смотреть в консоле!")
			driver.quit()
			overwatchleague = Overwatch()
			overwatchleague.league_parsing()

overwatchleague = Overwatch()
overwatchleague.contenders_parsing()
overwatchleague.league_parsing()
