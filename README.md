# Travel Diaries - A Django app

This Django application narrates the process of using adding spacial data to your [Django Girls Tutorial blog](https://tutorial.djangogirls.org/en/) in order to create a map for you Travel Diaries blog. This is the accompanying sample app for the ["_Creating a Travel Diary With Django_"](https://jtemporal.com/creating-a-travel-diaries-blog-with-django/).

_Note:_ I left the secret key that Django creates for development in the `settings.py` to make it easier to run after cloning this repo... So please, please, please remember to update that before deploying this to production!!! You've been warned.

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

## Sample Data

You also have in this repository some sample data for both locations and blog posts, make sure to create your superuser then load them into your database like so:

```sh
python manage.py loaddata sample-data/blog.json
python manage.py loaddata sample-data/map.json
```

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
```

# TODO

- [x] Implement the Django Girls blog app
- [x] Implement the map app
    - [x] Create a Location model
- [x] Update blog post model to have a location (FK)
- [x] Create the map page

# Wishlist

- Deployment
- Tests
- Other users
- Use `uv` for project management
- Generate post path through slug as opposed to the pk https://docs.djangoproject.com/en/5.1/ref/urls/#django.urls.path 
