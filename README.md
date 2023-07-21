#### Настроить .env
#### Выполнить в терминале:
- создать БД
- `python manage.py migrate`
- `python manage.py loaddata fixtures/full_data.json`
- `python manage.py csu`
##### Пароль суперюзера:
```Python
LOGIN = admin@admin.com
PASS = admin
```
- Создать в админке или зарегистрировать юзеров и назначить им группы