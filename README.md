# Тестовое задание автотестирование

## SeleniumWebDriver
Для работы тестов необходимо установить SeleniumWebDriver. Конкретно в этом коде был использован ChromeDriver, помещенный в папку ./Python/Python-version/Scripts.
Сам драйвер был скачан с https://chromedriver.chromium.org/.

## Запуск
Благодаря размещению ChromeDriver в папке с Python, запуск тестов значительно упростился. Код запускается из корневого каталога проекта при помощи команды:
```
python -m pytest tests/
```

## Тестовая конфигурация

+ ОС: Windows 7 (Build 7601: SP1)
+ Браузер: Google Chrome ver. 103.0.5060.66 (64-bit)
+ Среда: PyCharm Build #PC-221.5921.27, Runtime version: 11.0.15+10-b2043.56
