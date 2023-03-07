# website

```cd owl```  
```python manage.py makemigrations```  
```python manage.py migrate```  
```python manage.py createsuperuser```  
```python manage.py runserver```

### Go to <a href="http://localhost:8000/admin">localhost:8000/admin</a> for adding new monuments
### <a href="http://localhost:8000/id">localhost:8000/id</a> will give the corresponding monument

## To modify with slug
1. Delete db.sqlite3

```
python manage.py makemigrations web
python manage.py migrate
```
