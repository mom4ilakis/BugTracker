# BugTracker
Tracks bugs🐜

Allows a user to create an account.
Allows a logged-in user to create, update and delete bugs.

Quickstart: [Run with docker](#Spin-up-the-whole-service) or continue reading

Structure
---

### Backend
Restful API written with Python, [FastApi](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/)
```text
src
├── constants/
├── dto/ # Data transfer objects
├── models/ # Database models
├── routers/ # Routing logic
├── security/ # Authentication
├── services/ # Business logic
├── tests/  # Unit tests
├── init.py
├── db.py # DB connection. Model sync logic when ran as script
├── dependencies.py 
└── main.py # Entrypoint for the app
```

### Frontend
React SPA with [Chakra UI components](https://www.chakra-ui.com/)
```text
src
├── assets/ # Icons and other static assets
├── components/ # UI and other React components
├── context/ # React context providers
├── api.ts
├── App.css
├── App.tsx
├── authService.ts
├── index.css
├── main.tsx
├── types.ts
└── vite-env.d.ts
```

# Backend dev setup

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
python -m venv .venv
```
3. Activate the virtual environment
```shell
source .venv/bin/activate
```
4. Install Python dependencies
```shell
pip install -r requirements.txt
```
5. Copy `example.env` and substitute any placeholders
```shell
cp example.env .env
```
6. Sync models and database
```shell
python src/db.py
```
7. Start the service, change the port using `--port 1234`
```shell
fastapi dev src/main.py
```
> [!TIP] 
> If you get `cannot find module` errors  
> Add `<absolute-path-to-repo>/`backend/src to `PYTHONPATH`


> [!NOTE] 
> To run tests and see a coverage report
> ```shell
> coverage run -m pytest
> coverage report -m
> ```

# Frontend dev setup

---
0. Install NodeJS and yarn
1. Navigate to frontend folder
2. Install dependencies
```shell
yarn 
```
3. Run locally
```shell
yarn dev
```

# Spin up the whole service

---
Both frontend and backend come with `Dockerfiles`, there is also a `docker-compose.yml` in the root of the project.
The official `mySQL` image is used in the docker compose.  
If there are concerns that it will be unavailable, an image repository could be used, like harbor, and the image copied there.

### Run with docker compose
Remember to either set any passwords directly in the `docker-compose.yml` or set them in the environment or via .env file with `--env-file`

In the root of the project run:
```shell
docker compose up -d
```
The default ports are `8000` for the server and `5173` for the UI

### To run either frontend or backend Dockerfile
1. Build the image after navigating to the correct folder(`frontend` or `backend`)
```shell
docker build -t <name> . 
```
2. Run the image and set any env needed with `-e` or pass an `.env` file with `--env-file`
```shell
docker run <image-sha-from-previous-step>
```

