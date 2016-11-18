# Widget REST API Server

API Server for a Widget Factory application.

## Setup
The API Server is designed to work with the following:
- python3.5
- postgresql (v9.5)

### PostgreSQL
For local testing, the DB server must first be initialized using the following commands:

```sh
initdb /path/to/db/directory
pg_ctl -D /path/to/db/directory -l /path/to/log start

createuser widgetapi
createdb -O widgetapi widgetdb

psql -U widgetapi -d widgetdb -f db/init.sql
psql -U widgetapi -d widgetdb -f db/seed.sql
```

### API Server
Start the server using the following command:

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
