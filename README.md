# practPythonServ
Как можно работать с таблицами в MySQL на Python с http.server

Пример не требует web-сервера Apache, поскольку сам содержит web-сервер. Достаточно запустить serv.bat и открыть страницу http://localhost:8082/

Внешний вид экрана:

![image](https://github.com/alex1543/practPythonServ/assets/10297748/cad89de2-7ab6-43c1-b1c7-a931d7b2da68)

Пример гарантированно работает при след. действиях:
1) уснановить python-3.10.11-amd64.exe
2) потом устновить C:\Users\alex\AppData\Local\Programs\Python\Python310\Scripts\pip install mysql-connector

Для работы с таблицей из базы данных, необходимо экспортировать файл import_test.sql в phpMyAdmin.
