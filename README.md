# Travel Diaries - A Django app

This Django application narrates the process of using adding spacial data to your [Django Girls Tutorial blog](https://tutorial.djangogirls.org/en/) in order to create a map for you Travel Diaries blog.

## Pages

- `/`: standard blog from the Django Girls tutorial - this list all blog entries;
- `/map`: a page containing the map for all the blog entries - this shows each location you visited with their associated blog entries;
- `/admin`: the standard Django Admin page.

## Development

Using Python 3.12.1, and the following libraries:

```txt
Package  Version
-------- -------
asgiref  3.8.1
Django   5.1.7
folium   0.19.5
pip      25.0.1
sqlparse 0.5.3
```

Running locally:
```sh
python -m venv .env && source .env/bin/activate  # On Windows: .env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Login to the admin and add posts and locations then visit both `/` and `/map`.

## Models

Blog in the beginning:

```txt
Post
--------
title
content
author
created_at
published_date
```

After we add everything for the spacial data you should have the following models:

```txt
Post
--------
title
content
author
created_at
published_date
location


Location
--------
name
latitude
longitude
posts
```

# TODO

- [x] Implement the Django Girls blog app
- [ ] Implement the map app
    - [ ] Create a Location model
- [ ] Update blog post model to have a location (FK)
- [ ] Create the map page

# Wishlist

- Deployment
- Tests
- Other users
- Use `uv` for project management
- Generate post path through slug as opposed to the pk https://docs.djangoproject.com/en/5.1/ref/urls/#django.urls.path 
- Once a blog post is created with a pre-existing local, add that blog post to the list in the local automatically
