To run the application, first
- edit 'settings.py' with your own EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.
- in the console, run "python manage.py createsuperuser"
- follow console instructions
- Then run "python manage.py runserver"

Then using Postman, use Basic Authentication with the given username and password and send a request to 
- /api/posts
- /api/posts/1/

Make sure to create a post using the POST method before trying to retreive any posts. After creating a post, check the email entered during creating the User.
