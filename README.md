# TWITTER PYTHON TIPS NAVIGATOR

A web app that helps to navigate through collection of tips from [@python_tips](https://twitter.com/python_tip) on twitter, but from their [spreadsheet](https://t.co/oARrOmrin7).

These spreadsheets are to be downloaded and saved in the `./data_files/` folder. Then the app fetches the csv files inside the folder periodically every 1 minute using celery and saves in the database. The csv layout should be in this format:

|   Timestamp           |   Python Tip  |   Your name or Twitter id |   Your email          |
|   ---                 |   ---         |   ---                     |   ---                 |
|   2/3/2017 0:50:25    |   Tip         |   @OnojaDaniel20          |   example@mail.com    |


### Setup

> #### NOTE:
> - Make sure to use postgres database, as some features used in this project supports only postgres.
> - Setup rabbitmq for message queueing. Find out how to install rabbitmq [here](https://www.rabbitmq.com/download.html)

- Setup virtual environment using using `virtualenv` or `pipenv` or any other.
- Create a `.env` file in the base directory - (`./tips_navigator/`), copy/paste the following fields, set them up and add their respective values.
```
DB_NAME=
DB_USERNAME=
DB_PASSWORD=
RABBITMQ_USER=
RABBITMQ_PASS=
RABBITMQ_HOST=
```
- Install dependencies using `pip install -r requirements.txt` from the project directory
- Start up Celery process with `source ./start-celery.sh`: This script will start celery worker and celery beat in detached mode.
- Celery logs will be found in `celery.log`, while celery-beat in `celery.beat.log`
- If you wish to stop celery from running, issue a `pkill` command like this - `kill -9 $(ps aux | grep celery | grep -v grep | awk '{print $2}' | tr '\n'  ' ') > /dev/null 2>&1`