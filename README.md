# Widget REST API Server

API Server for a Widget Factory application.

## Setup
The API Server dependencies:
- python3.5
- postgresql (v9.5)

### PostgreSQL
For local testing, run the following commands to initialize and seed the DB:

```sh
initdb /path/to/db/directory
pg_ctl -D /path/to/db/directory -l /path/to/log start

createuser widgetapi
createdb -O widgetapi widgetdb

psql -U widgetapi -d widgetdb -f db/init.sql
psql -U widgetapi -d widgetdb -f db/seed.sql
```

### API Server
Switch to a python3.5 environment if needed and install python dependencies:
```sh
pip install -r requirements.txt
```

Start the server:

```sh
python server.py
```


## Endpoints

| VERB | URL | DESCRIPTION |
| --- | --- | --- |
| GET | /user/:id | Returns a user specified by ID |
| POST | /user | Creates a new user |
| GET | /widget/:id | Returns a widget specified by ID |
| POST | /widget | Creates a new widget |
| PUT | /widget/:id | Updates a widget specifed by ID |
| GET | /widgets | Returns all widgets |
| GET | /categories | Returns all categories |
| GET | /sub_categories | Returns all sub categories |
| POST | /widget_categories | Creates a new category |
| DELETE | /widget_categories | Deletes widget categories |
| GET | /order/:id | Returns an order specified by ID |
| POST | /order | Creates a new order |
| PUT | /order/:id | Updates an order |
| DELETE | /order/:id | Deletes an order |
