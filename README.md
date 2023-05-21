# practPythonServ
Как можно работать с таблицами в MySQL на Python с http.server

Пример не требует web-сервера Apache, поскольку сам содержит web-сервер. Достаточно запустить serv.bat и открыть страницу http://localhost:8082/

Внешний вид экрана:

![image](https://github.com/alex1543/practPythonServ/assets/10297748/cad89de2-7ab6-43c1-b1c7-a931d7b2da68)

Пример гарантированно работает при след. действиях:
1) уснановить python-3.10.11-amd64.exe
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
