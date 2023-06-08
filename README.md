# practPythonServ
Как можно работать с таблицами в MySQL на Python с http.server

Пример не требует web-сервера Apache, поскольку сам содержит web-сервер. Достаточно запустить serv.bat и открыть страницу http://localhost:8082/

Внешний вид экрана:

![image](https://github.com/alex1543/practPythonServ/assets/10297748/cad89de2-7ab6-43c1-b1c7-a931d7b2da68)

Пример гарантированно работает при след. действиях:
1) установить python-3.10.11-amd64.exe
2) потом устновить C:\Users\alex\AppData\Local\Programs\Python\Python310\Scripts\pip install mysql-connector

Для работы с таблицей из базы данных, необходимо экспортировать файл import_test.sql в phpMyAdmin.

# practPythonApache
Дополнительно есть возможность работы скрипта через Apache. Для этого необходимо:

1) найти секцию < IfModule mime_module > в файле httpd.conf и добавить две строки:

    AddHandler cgi-script .py
    ScriptInterpreterSource Registry-Strict

2) исправить в файле practPythonApache/index.py путь к Python. Например, так:

    #! C:/Users/alex/AppData/Local/Programs/Python/Python310/python.exe

Этот пример гаранированно работает в XAMPP Version 7.4.27 с Python 3.10.

# practPythonApache/noFileOut
Проект повторяет practPythonApache, но без создания временного файла out.html

# practPythonServ/mac
Возможна работа на macOS. Нужно установить XAMPP, например, из файла: xampp-osx-8.2.4-0-installer.dmg

Запустить MySQL Database на вкладке Manage Servers, настроить открытие файлов *.sh через программу Терминал, разрешить права на запуск: chmod +x mac_serv.sh

Внешний вид сайта на macOS Ventura 13.4:

<img width="1147" alt="mac" src="https://github.com/alex1543/practPythonServ/assets/10297748/17560fc7-bf76-4103-b388-e3ab135728f4">

После установки Python (например, python-3.11.3-macos11.pkg), необходимо выполнить команды:

    1) python3 -m ensurepip
    2) pip3 install mysql-connector

В родном браузере Safari 16.5:

<img width="1283" alt="Снимок экрана 2023-06-07 в 22 49 06" src="https://github.com/alex1543/practPythonServ/assets/10297748/f9456bac-62af-4207-bda0-ba0730a12925">
