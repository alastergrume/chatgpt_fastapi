---------------------------------------------------------------------------
Для запуска приложения в IDE на локальной машине выполните следующие шаги:
---------------------------------------------------------------------------
Создайте новый проект в Вашем IDE

Настройте и запустите виртуальное окружение

Склонируйте репозиторий через терминал следующей командой:

    git clone https://github.com/alastergrume/chatgpt_fastapi.git

Зайдите в папку с проектом, выполнив команду в терминале:

    cd .\chatgpt_fastapi\

После успешного клонирования, для запуска приложения введите команду в терминале:

    docker compose up --build

Приложение будет доступно по адресу:

    http://127.0.0.1:8000

Для остановки приложения в терминале нажмите сочетание клавиш 

    CTRL+C
    
После этого выполните команду:

    docker-compose dowm

---------------------------------------------------------------------------
Алгоритм действий для запуска приложения на сервере Linux Ubuntu:
---------------------------------------------------------------------------

Для успешного запуска и работы приложения необходимо предустановленые docker и unzip

Для установки unzip воспользуйтеся стандартной утилитой

    sudo apt install unzip

Для установки Docker воспользуйтесь официальной документацией: 

    https://docs.docker.com/engine/install/ubuntu/

Для клонирования приложения выполните поочередно следующие команды в терминале:

    wget https://github.com/alastergrume/chatgpt_fastapi/archive/master.zip  
    unzip master.zip
    rm master.zip

Войдите в папку с фалами приложения 

    cd chatgpt_fastapi-main

Выполните команду для запуска контейнера
    
    docker compose up --build

Для запуска в фономвом режиме 

    docker-compose up -d

Приложение будт доступно по адресу: 

    http://YOUR_HOST_IP:8000/

-----------------------------------------------------------------------------
Работа с приложением
-----------------------------------------------------------------------------

Введите Ваш OPENAI_API_TOKEN
Нажмите Send

После успешной установки ключа откроется страница чата.

При закрытии соединения обновите страницу либо перейдите на главную страницу по адресу:

     http://YOUR_HOST_IP:8000/


