Новостной сайт с информацией об известных женщинах мира.
Релизован механизм регистрации и добавления новых статей авторзованными пользвателями.
Осуществлена оптимизация нагрузки на СУБД

Для запуска проекта с GitHub:
1) Открыть командную строку или терминал
   

2) В интересующей директории создать папку с проектом


    mkdir coolsite   

3) Перейти в папку


    cd coolsite
   
4) Создать виртуальное окружение


    python -m venv venv   

5) Активировать виртуальное окружение

На Windows:

    .\venv\Scripts\activate
На Linux:

    source venv/bin/activate

6) Клонировать репозиторий


    git clone https://github.com/aboronilov/django_basic_coolsite   

7) Установить зависимости


    pip install -r requirements.txt

6) Клонировать репозиторий 


    git clone https://github.com/aboronilov/django_basic_coolsite

7) Запустить сервер


    cd coolsite
    python manage.py runserver