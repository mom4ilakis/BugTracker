# BugTracker
Tracks bugs🐜

Allows a user to create an account.
Allows a logged-in user to create, update and delete bugs.

Structure
---

### Backend
Restful API written with Python

### Frontend
React SPA

Backend dev setup
---

### Set up the DB
1. Install mySQL
2. Open CLI
3. Create a user
```SQL
CREATE USER <user-name>@localhost IDENTIFIED BY <password>; 
```
4. Create the database for the service
```SQL
CREATE DATABASE <db-name>;
```
5. Grant access to the database
```SQL
GRANT ALL PRIVILEGES on <db-name>.* to <user-name>@'localhost'; 
```

### Set up the .env
1. Navigate to the `backend` folder
```shell
cd backend
```
2. Copy the `example.env` to `.env`
```shell
cp example.env .env
```
3. Substitute the placeholders in `.env` with the values from the previous set-up


### Set up Python and service dependencies
0. Install Python 3.13
1. Navigate to the `backend` folder
```shell
cd backend
```
2. Create a virtual environment
```shell
python -m venv venv
```
3. Activate the virtual environment
```shell
source venv/bin/activate
```
4. Install Python dependencies
```shell
pip install -r requirements.txt
```
5. Start the service
```shell
python main.py
```

Frontend dev setup
---
0. Install NodeJS
1. Install dependencies
2. Run locally