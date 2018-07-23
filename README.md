# My-Diary
MyDiary is an online journal where users can pen down their thoughts and feelings.
# Diary
[![Build Status](https://travis-ci.org/Rodgerkilzone/My-Diary.svg?branch=master)](https://travis-ci.org/Rodgerkilzone/My-Diary)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ff4526e8237a4772addbc76d89edf6e2)](https://www.codacy.com/app/Rodgerkilzone/My-Diary?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Rodgerkilzone/My-Diary&amp;utm_campaign=Badge_Grade)
## Endpoints

| Functionality        |    Method     |         Endpoint                   |
| :------------------- |:-------------:| ----------------------------------:|
| Get all entries      | GET           | /mydiary/api/v1/entries            |
| Get specific entry   | GET           | /mydiary/api/v1/entries/-entryId-  |
| Add an entry         | POST          | /mydiary/api/v1/entries            |
| Modify an entry      | PUT           | /mydiary/api/v1/entries/-entryId-  |
| Delete an entry      | DELETE        | /mydiary/api/v1/entries/-entryId-  |

## How to setup it up:

To set it up in your machine:

1.sudo install python3

2.pip install virtualenv

Clone this repository:

git clone https://github.com/Rodgerkilzone/My-Diary.git

cd My-Diary/

## Create a virtual environment in the root directory:

virtualenv [name of virtualenv]

## On your terminal run:
command for installing dependancy modules

pip install -r requirements.txt

## Run the application:

flask run

or

python run.py

## Run the test:
python test.py -unit

## Heroku Link:
https://floating-meadow-65335.herokuapp.com/mydiary/api/v1/entries


<h2>Landing page</h2>
<p>gh-pages https://rodgerkilzone.github.io/My-Diary/UI/index.html</p>
<br/>
<h2>Login page</h2>
<p>gh-pages https://rodgerkilzone.github.io/My-Diary/UI/login.html</p>
<br/>
<h2>Sign up page</h2>
<p>gh-pages https://rodgerkilzone.github.io/My-Diary/UI/sign_up.html</p>
<br/>
<h2>Home page</h2>
<p>gh-pages https://rodgerkilzone.github.io/My-Diary/UI/home.html</p>
<br/>
<h2>profile page</h2>
<p>gh-pages https://rodgerkilzone.github.io/My-Diary/UI/profile.html</p>
<br/>
