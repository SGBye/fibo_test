# Django + DRF + docker-compose + redis-cache fibonacci sequence
test for Wargaming

Это Джанго-проект, который реализует 1 эндпоинт - /fibonachi?from_={}&to={}. В качестве ограничения я выделил себе ровно 2 часа на "проектирование" и реализацию.
P.S. я бы, вероятно, писал fibonacci, но в проекте старался придерживаться ТЗ.

# Как запустить?
Спулить проект и выполнить 
```docker-compose up --build```

Тесты: ```docker-compose exec backend pytest```

# Что можно улучшить?
- Обычно в своих проектах я реализовываю версионирование API (api/v1/fibonachi...), но тут сделал url в соответствии с ТЗ.

- Для упрощения логики я наполняю кэш во время 1-ого запроса. Тут можно было бы усложнить и наполнять его постепенно с каждым запросом, 
а не хранить всегда полностью, но тогда нужно отслеживать то, что уже записано, а что нет.

- Проект выглядит немного сумбурно, обычно все же есть и фронт, и бэк, поэтому все выглядит лучше - папки frontend, backend, docker, docs на верхнем уровне.

- Можно сделать простенький CI с тестами и заливкой документов на сервер.

- Можно сделать разные docker-compose.yml и файлы с переменными окружения для разных сред разработки - локалки, дева и прода.

- Я добавил в зависимости redis-cache, но по сути его не использую - масштабируемость! :)

# Что хотелось бы отметить
- Написан swagger.yml
- Используются встроенные структуры redis, что позволяет ускорить работу эндпоинта: при 10000 чисел запись в кэш через cache.set занимает более секунды, 
а через con.rpush < 0.5 секунд. Я детально не тестировал, но десереализация и сериализация по идее должны быть дольше.


