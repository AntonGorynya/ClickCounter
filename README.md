# Обрезка ссылок с помощью Битли

Данный скрипт позволяет обрезать ссылки с помощью сервиса Битли, либо получить статистику переходов если ссылка уже является укороченной.

### Как установить

Перед установкой зерегестрируйтесь в сервисе https://bitly.com/. После чего перейдите в личный кабинет *Setting - Developer Settings - API*,  где сгенерируйте токен.
После чего создайте файл **.env** вида:
```
TOKEN_BITLY='<Ваш токен>'
```
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Пример запуска

Ниже представлен пример запуска для получения количества переходов по Битли ссылке
```
C:\Users\UserName\PycharmProjects\ClickCounter> python ./main.py bit.ly/3j57iVZ
5

```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).