# Django REST Framework API Service

## Технологии проекта:

1. [Django REST Framework](https://www.django-rest-framework.org/)
2. [PostgreSQL](https://www.postgresql.org/)

## Установка и использование  

### При помощи [docker compose](https://docs.docker.com/compose/)
1. Необходимо скачать проект.  
   ```git clone https://github.com/Cthupby/drf-api-service.git```  
   ```cd drf-api-service```  
2. Создать образ.  
   ```docker build -t drf_api_service .```  
3. Создать и активировать контейнеры.  
   ```docker-compose up -d --build```  
4. Перейти на локальный адрес.   
   ```http://0.0.0.0:8000```
