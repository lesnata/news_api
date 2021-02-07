## Table of contents
* [General info](#general-info)
* [Link to project](#link-to-project)
* [Postman collection](#postman-collection)
* [Functionality](#functionality)
* [Endpoints](#endpoints)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple news API app listing news with functionality to 
upvote and comment on them. Similar platform to HackerNews.
Including registration and Token request verification.
All news upvotes are resetting to '0' at 00:00 daily as a recurring task.

## Link to project
LIVE: https://news-api-123.herokuapp.com/api/account/register

## Postman collection
Postman Prod collection link: 
https://www.getpostman.com/collections/ff6e8490c84b1a5916ae

## Functionality
- CRUD API to manage news posts. 
- CRUD API to manage comments on them. 
- Endpoint to upvote the post
- Once a day to reseting post upvotes count

## Endpoints

##### REGISTRATION

/api/account/register -> POST request to create a new user
- new registered account needs to be approved manually. Please, refer to 'TODO refactor' section
For test requests please use in Headers:

```Authorisation: Token 11ecdb72f09813fcb4896d984f6231b41d81226c ```

##### NEWS

[COLLECTION] /api/news/  -> GET all news | POST new news
    
[ELEMENT] /news/<news_id>/  -> GET news/id | PUT news/id | DELETE news/id
    
   
##### COMMENTS

[COLLECTION] /api/news/<news_id>/comment/ -> POST comment
    
[ELEMENT] /api/comment/<comment_id>/ -> GET comment/id | PUT comment/id | DELETE comment/id
    
##### UPVOTE

[ELEMENT] /api/upvote/<news_id>/ -> PUT upvote/id


## Technologies
Project is created with:
* Django==3.1.6
* djangorestframework==3.12.2
* black==20.8b1
* flake8==3.8.4
* psycopg2-binary==2.8.6
* django-celery-beat==2.2.0
* celery==5.0.5
	
## Setup
To run this project locally, make the following:

```
$ git clone https://github.com/lesnata/news_api.git
$ cd news_api
$ virtualenv venv_news
$ source venv_news/bin/activate
$ (env)$ pip install -r requirements.txt
$ (env)$ python manage.py runserver

```


## TODO refactor:
- New registered user needs manual 'Activate' box ticking in Admin panel. Need to set it automatically.
For test requests please use in Headers:

```Authorisation: Token 11ecdb72f09813fcb4896d984f6231b41d81226c ```
- rewrite serializer with serializers.Serializer and read_only fields
- views.py/registration - Enable automatic Token generation in models.py with @receiver(post_save)
- views.py/news_element/PUT - make only one field update necessary
- views.py/news_element/DELETE - add info message when deleted
- views.py/upvote/PUT - make body params unnecessary