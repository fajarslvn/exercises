## Setup Project in Django

1. Make a folder project `mkdir project00`
2. cd to folder and make environment -> `virtualenv env`
3. Activate virtualenv - `source env/bin/activate`
4. Install django -> `pip3 install django`
5. Create a project -> `django-admin startproject tutorial'
6. Rename "tutorial" folder (root) to "src"
7. cd to src folder > settings.py
8. Set -> ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
9. and hide SECRET_KEY in sk.txt and place it in "src"-> 
```
sk = f'{BASE_DIR}/sk.txt'
with open(sk) as f:
    SECRET_KEY = f.read().strip()
```
10. Build django configuration -> `python3 manage.py migrate`
11. Run the django server -> `python3 manage.py runserver`

## How to make a module in django

1. Create posts module for blog posts -> `python3 manage.py startapp posts`
2. Add "posts" (folder) in settings configuration ->
```
INSTALLED_APPS = [
  ....
  ....
  ....
  'posts',
]
```
3. Create class Posts (database) in posts > models.py (Set 1)
4. To create the module type `python3 manage.py makemigrations`
5. Add it to configuration `python3 manage.py migrate`
6. Create admin page with `python3 manage.py createsuperuser`
7. Fill the credentials (you can skip it for email)
8. Run the server `python3 manage.py runserver`
9. Open admin page by access it on localhost:8000/admin
10. Add Posts model to admin page -> posts > admin.py (Set 2)
11. Add code -> posts > views.py (Set 3)
```
def post_list(request):
    context = {}
    return render(request, 'post_list.html', context)
```
12. Add path for post_list view -> tutorial > urls.py (Set 4)
13. Create file and function -> posts > urls.py (Set 4)
14. Create folder and html file in posts > templates (new) > posts (new) > post_list.html (New and add simple html)
15. Update the path on posts > views.py (Set 4) -> `posts/post_list.html`
16. Create the context from the models/database (Set 5)