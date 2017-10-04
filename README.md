# Поиск дублирующих файлов

Скрипт ищет повторяющиеся файлы в заданной папке и во всех вложенных папках. Сравнение происходить по имени и размеру файла.

# Как запускать

На вход подается путь к папке.

```
python3 duplicates.py -h
usage: duplicates.py [-h] -p PATH

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  start directory for searching duplicates

```

Скрипт выводит все найденные дубликаты в формате 
*<размер файла> <полный путь к файлу>*

Пример запуска

```
[lucky@lucky 11_duplicates]$ python3 duplicates.py -p /home/lucky/devman/
11 /home/lucky/devman/4_json/.git/COMMIT_EDITMSG
11 /home/lucky/devman/3_bars/.git/COMMIT_EDITMSG

```

# Цели проекта

Тренировочный код для проекта - [DEVMAN.org](https://devman.org)
