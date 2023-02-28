## Асинхронный парсер PEP-документации с помощью фрймворка Scrapy

## Описание:
### Парсер выводит список всех PEP: номер, название и статус, а также считает количесто статусов. Парсер выводит информацию в csv-формате.  
### Начало работы с проектом: 
```python
git clone git@github.com:AnnPovor/scrapy_parser_pep.git
```
```python
# Для Windows:

- python -m venv venv

- . venv/Scripts/activate
```
```python
pip install -r requirements.txt
```
### Парсер запускается командой:
```python
scrapy crawl pep
```
#### После чего в папке results/ появятся два csv-файла.