
# Bitcoin Technical Indicators
![](img\%.png)

## Project purpose: 

The purpose of the project is provide the user with a number of technical indcators for bitcoins price action and encourage them to pay to access the premium metric. The premium metric is a risk indicator, combining the
other metrics into one and indicating optimal buying and selling oportinities.

The project contains the following apps:
* Dashboard
    * Explains the purpose of the site and encourages the user to register.

* Login / registration
    * Allows user to create an account and login.

* Metrics
    * Displays all of the currently available metrics.

* Metric Details
    * Renders a Plotly chart with Bitcoins price and selected indicator.

* Admin CRUD
    * Administrators can add price data as required (currently this is not automated)
    * Administrators can edit the details of existing metrics

* Checkout
    * Users can purchase lifetime access to the premium indicator


## UX

### User stories
* As a user, I want to be able to register to the site, so that I can securely login.


* As a user, I want to be able to sign into my account, so that I have access to the metrics available.


* As a user, I would like the user experience on the website to be
intuitive, so that I can quickly navigate to the metric I wish.


* As a user, I want to be able to view bitcoin price data, so that I can spot trends in the price action.


* As a user, I want to be able to view my chosen metric overlayed onto the chart, so that I can easily comprehend the metric.


* As an administrator, I want full CRUD functionality of the price data, so that the metrics are kept up to date.


* As the site owner, I want the checkout functionality to be secure, so that a user cannot access the premium metric without paying.


### Strategy
__Goal__: Show the user how valuable technical indicators can be when predicating Bitcoin price movements and encourage them to purchase the premium metric.


### Scope
* A dynmic web app that implements the Plotly API to display Bitcoin price data in conjunction with relvent technical indicators. 

### Design and colors:

#### Colors:

* background: #1F2833;
* font: #C5C6C7;
* header: #66FCF1;
* navbar: #C5C6C7;


#### Wireframes
* [Mobile View](https://github.com/Wbwren/bitcoin-technical-indicators/blob/main/blob/master/wireframes/mobile-wireframes.png)

* [Tablet View](https://github.com/Wbwren/bitcoin-technical-indicators/blob/main/blob/master/wireframes/tablet-wireframes.png)

* [Desktop View](https://github.com/Wbwren/bitcoin-technical-indicators/blob/main/blob/master/wireframes/desktop-wireframes.png)


### Features:

#### Plotly graphing

To display the price charts, the Plotly API for Python was used.

### Technology Used:

#### Languages:

* HTML5
* CSS3
* JavaScript
* Python
* SQL

#### Libraries, Frameworks and Tools

* <a href="https://www.heroku.com/">Heroku</a> for hosting the deployed application
* <a href="https://www.djangoproject.com/">Django</a> for the project configuration
* <a href="https://jinja.palletsprojects.com/en/3.0.x/">Jinja2</a> as a templating engine
* <a href="https://plotly.com/python/">Plotly</a> for graphing the data with Python
* <a href="https://stripe.com/">Stripe</a> for payments
* <a href="https://pypi.org/project/psycopg2/">Psycopg2</a> as database adapter
* <a href="https://gunicorn.org/">Gunicorn</a> as a python web server
* <a href="https://code.visualstudio.com/">VSCode</a> as the IDE
* <a href="https://git-scm.com/">Git</a> for version control
* <a href="https://github.com">Github</a> remote git storage service
* <a href="https://validator.w3.org/">W3C Validator</a> Used to check the validity of my HTML and CSS.
* <a href="http://pep8online.com/">PEP 8 Online Validator</a> Used to validate the Python code.
* <a href="https://moqups.com">Balsamiq</a> for creating the wireframes.
* <a href="https://aws.amazon.com/s3/">AWS S3 Bucket</a> for storage of static files
* <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html">Boto3 </a>to make use of Amazon S3
* <a href="https://getbootstrap.com/">Bootstrap</a> for developing a responsive, mobile-first website
* <a href="https://jquery.com/">jQuery</a> JavaScript library
* <a href="https://fonts.google.com/specimen/Nunito">Google Fonts</a>
* <a href="https://fontawesome.com/">FontAwesome</a>

#### Databases
* <a href="https://www.sqlite.org/">SQlite3</a> django database queries
* <a href="https://www.postgresql.org/">PostgreSQL</a> Heroku database service




## Testing

### Code Validation
* HTML was validated using W3C Markup Validation Service.

* CSS was validated using W3C CSS Validation Service - Jigsaw

* JavaScript was passed through the linter jshint with no warnings
### Functionality test

| Num | Test                                                                         | Action                              | Outcome image                                                                                                                        | Result |
|-----|------------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------|
|1|As a user, I want to be able to register to the site, so that I can securely login.|Navigate to registration page and attempt to register with a valid email and password | [Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/login.png) | Pass
|2|As a user, I want to be able to sign into my account, so that I have access to the metrics available.|Navigate to the login page and attempt to login with the previously registered user|[Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/registration.png)|Pass|
|3|As a user, I would like the user experience on the website to be intuitive, so that I can quickly navigate to the metric I wish.|Once logged in, click on the metrics icon in the navbar|[Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/nav-to-metrics.png)|Pass|
|4|As a user, I want to be able to view bitcoin price data, so that I can spot trends in the price action.|Select an indicator from the metrics page and view the chart displayed|[Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/price-visible.png)|Pass|
|5|As a user, I want to be able to view my chosen metric overlayed onto the chart, so that I can easily comprehend the metric.|Navigate to a given metric and assess whether the moving average lines are visible|[Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/moving-averages.png)|Pass|
|6|As an administrator, I want full CRUD functionality of the price data, so that the metrics are kept up to date.|Login as super user, navigate to the edit price data page and attmept to add, edit and delete a given price|[Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/edit-price.png)|Pass|
|7|As the site owner, I want the checkout functionality to be secure, so that a user cannot access the premium metric without paying.|Login as non-super user and attempt to access endpoints which are restricted to super users|[Image](https://github.com/Wbwren/bitcoin-technical-indicators/blob/master/test-images/super-user-nav.png)|Pass|

<br>

### Browser Compatibility
| Num | Browser         | Test result |
| ---|:-------------:| :----: |
| 1 | Chrome | Passed
| 2 | Opera | Passed
| 3 | Mozzilla | Passed

<br>

### Responsiveness Testing
* Chrome developer tools was used to test a wide variety of device sizes and resolutions.

* The website has been tested on a Samsung Galaxy s10, Lenovo Legion and a desktop PC with a 1080p and 4k monitor, respectfully.




### Deployment

#### Running Code Locally


1. Follow this link to my [Repository on Github](https://github.com/Wbwren/bitcoin-technical-indicators) and open it.

2. Click `Clone or Download`.

3. In the Clone with HTTPs section, click the `copy` icon.

4. In your local IDE open Git Bash.

5. Change the current working directory to where you want the cloned directory to be made.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press enter and your local clone will be ready.

8. Create and start a new environment:  
python -m .venv venv  
source env/bin/activate

9. Install the project dependencies:  
pip install -r requirements.txt

10. Create a new file, called `env.py` and add your environment variables:

import os  
os.environ.setdefault("DJANGO_SECRET_KEY", "secret key here")
os.environ.setdefault("DATABASE_URL", "secret key here")
os.environ.setdefault("SQLITE_URL", "secret key here")
os.environ.setdefault("CACHE_URL", "secret key here")
os.environ.setdefault("REDIS_URL", "secret key here")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "secret key here")
os.environ.setdefault("STRIPE_SECRET_KEY", "secret key here")
os.environ.setdefault("STRIPE_WH_SECRET", "secret key here")
os.environ.setdefault("DATABASE_URL", "secret key here")
os.environ.setdefault("EMAIL_HOST_USER", "secret key here")
os.environ.setdefault("EMAIL_HOST_PASS", "secret key here")
os.environ.setdefault("DEFAULT_FROM_EMAIL", "secret key here")

11. Go to `settings.py` file and add your environment variables.

12. Add `env.py` to .gitignore file

13. Go to terminal and run the following: `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

14. Create a superuser: `python3 manage.py createsuperuser`

15. Run it with the following command:  
`python manage.py runserver`

16. Open `localhost:8000` on your browser

17.  Add `/admin` to the end of the url address and login with your superuser account to edit the models.

#### Deployment to Heroku

The following steps were taken in order to deploy this site to Heroku:

1. Created a new app in `Heroku` with a unique name, chose my region

2. Went to `Resources`, within Add-ons searched `Heroku Postgres`, chose Hobby Dev - Free version, then clicked `Provision` button.

3. In `Settings` clicked on `Reveal Config Vars` button, and copied the value of `DATABASE_URL`

4. Returned to terminal window and run `sudo pip3 install dj_database_url`

5. Also run `sudo pip3 install psycopg2`. Created a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`

6. Went to `settings.py` and added `import dj_database_url` and updated `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` also
updated `env.py` with `os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")`

7. I run `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

8. I created a superuser: `python3 manage.py createsuperuser`

9. Logged in to `Amazon AWS`, went to `S3` and created a new `S3` bucket.

10. Returned to terminal window and run `sudo pip3 install django-storages` and `sudo pip3 install boto3`. Went to `settings.py` and added `storages` to `INSTALLED_APPS`.

11. Also in `settings.py` the following lines are added:

AWS_S3_OBJECT_PARAMETERS = {
    "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
    "CacheControl": "max-age=94608000",
}

AWS_STORAGE_BUCKET_NAME = "bitcoin-technical-indicators"
AWS_S3_REGION_NAME = "eu-west-1"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_STORAGE = "custom_storages.StaticStorage"
STATICFILES_LOCATION = "static"
DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
MEDIAFILES_LOCATION = "media"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

12. Updated `env.py` with `AWS` keys (these keys are from `S3`).

13. Created `custom_storages.py` at the top level containing the following code:

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

14. Went to `settings.py` and added:
  
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'

DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

15. Returned to terminal window and run `python3 manage.py collectstatic`

16. Returned to `Heroku`. In `Settings` clicked on `Reveal Config Vars` button, and added all the following config vars from `env.py`:

| Key         | Value | 
|:-------------:| :----: | 
|  AWS_ACCESS_KEY_ID | secret key here  |
|  AWS_SECRET_ACCESS_KEY | secret key here |
|  DATABASE_URL | secret key here |
|  DISABLE_COLLECTSTATIC| 1 |
|  SECRET_KEY | secret key here |
|  STRIPE_PUBLISHABLE | secret key here |
|  STRIPE_SECRET| secret key here |

17. Clicked to `Deploy`, then `GitHub`, searched for my repository and clicked to `Connect` button.

18. Returned to terminal window and run `sudo pip3 install gunicorn` and added to `requirements.txt`

19. Created a `Procfile` using the following command: `echo web: gunicorn ms4.wsgi:application`

20. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

20. Return to `Heroku` and click `Deploy Branch`

21. Once the build is complete, click on `Open app`

22. Went to `settings.py` and added `bitcoin-technical-indicators.herokuapp.com` to `ALLOWED_HOSTS`

23. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

24. Returned to `Heroku` and hit `Deploy Branch` again.


## Clone
1. Follow this link to my [Github Repository](https://github.com/Wbwren/bitcoin-technical-indicators).

2. Click 'Clone or Download'.

3. In the Clone with HTTPs section, click the 'copy' icon.

4. In your local Integrated Development Environment open Git Bash.

5. Change the current working directory to where you want the cloned directory to be located.

6. Type 'git clone', and paste the URL you copied before.

7. Press enter and your local clone will be available.

# Loading Bitcoin Price Data
- download bitcoin historical data csv from prefered source (e.g. investing.com)
- edit csv to include the following cols: date, price
- delete header row (just include the data rows)
- set the date col to the format Y-m-d
- set all other cols to a type of number (otherwise prices may have ',' symbol which can cause errors)
- install sqlite extension for visual studio code
- load the csv to the project root directory
- use the following commands to load the data into the postgres database:
    .\sqlite3.exe metrics_bitcoin_price
    .mode csv
    .import <path/to/csv> metrics_bitcoin_price;

    Note if using postgres, the copy command is:
    \copy metrics_bitcoinprice from '<path/to/csv>' csv header;

# Accessing administration CRUD functionality
* Login to the site with the username and and password of 'wren233@gmail.com' and 'Atlantic99' respectfully.
* Click 'Edit Price Data' in the navbar.

# Acknowledgments
A special thanks to my mentor Brian Macharia for his invaluable guidance throughout this project and the the entire program.