# TWITTER PYTHON TIPS NAVIGATOR

A web app that helps to navigate through collection of tips from [@python_tips](https://twitter.com/python_tip) on twitter.

### Setup

> #### Note:
> Make sure to use postgres database, as some features used in this project supports only postgres.
> Setup rabbitmq for job scheduling

- Create a `.env` file in the base directory - (`tips_navigator`), copy/paste the following fields, set them up and add their respective values.
```
DB_NAME=
DB_USERNAME=
DB_PASSWORD=
```
- Install dependencies using `pip install -r requirements.txt` from the project directory