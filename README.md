# gestor-de-productos

1. git clone https://github.com/paezdavid/gestor-de-productos.git
2. cd gestor-de-productos
3. python3 -m venv venv
4. source ./venv/bin/activate
5. pip install -r requirements.txt
6. python3 manage.py migrate
7. python3 manage.py createsuperuser (admin user)
8. python3 manage.py runserver
10. POST ```http://127.0.0.1:8000/api/token/``` (post with the admin credentials to get bearer access token)
11. If using Postman, add bearer access token to Auth tab
12. POST ```http://127.0.0.1:8000/usuarios/``` (user registration) ```{ "email": "example@mail.com", "username": "example", "password": "12345678" }```

- With the access token set up, add products POSTing to ```http://127.0.0.1:8000/productos/```
- As an admin, approve users with a POST request to ```http://127.0.0.1:8000/usuarios/{id}/approve/```
- Filter results with a GET req. to ```http://127.0.0.1:8000/productos?search={query}```
