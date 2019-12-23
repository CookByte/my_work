# my_work
这是一个可以在Web端提交数据并且能够“直接粘贴Excel表格”数据的Demo，同时也实现了前端增删改、分页查看的功能。
 - 工具：后端用Django，前端用Bootstrap，数据库SQLite3。
 - 功能：每周提交3条“工单量TOP3对应的产品名称”记录，每1页显示2周的数据。

# 使用方法：
 - Clone之后，进入my_work目录
 - 执行：python manage.py makemigrations
 - 执行：python manage.py migrate
 - 执行：python manage.py runserver
 - 浏览器访问http://127.0.0.1:8000/
 
