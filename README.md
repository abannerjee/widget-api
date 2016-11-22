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

## Testing
API endpoints can be tested by running the following command:
(Note, the postgresql DB must be running locally to execute tests)

```sh
python -m unittest test/{endpoint}.py

e.g.
python -m unittest test/category.py
python -m unittest test/*.py
```
## Endpoints

| VERB | URL | DESCRIPTION |
| --- | --- | --- |
| GET | /widget/:id | Returns a widget specified by ID |
| POST | /widget | Creates a new widget |
| | | { data: { name: STR, type: ID, props: [ID] } } |
| GET | /widgets?PARAMS | Returns all widgets matching query parameters |
| | | PARAMS are expected to match 'p_category=p_name' |
| | | Refer to 'Property' table for p_category, p_name |
| GET | /categories?widget=ID | Returns all categories |
| | | Optional param 'widget' to get all categories for a widget |
| GET | /sub_categories | Returns all sub categories |
| POST | /widget_categories | NOT Implemented |
| DELETE | /widget_categories | NOT Implemented |
| GET | /order/:id | Returns an order specified by ID |
| POST | /order | Creates a new order |
| | | { data: [{ w_id: ID, p_ids: [ID] }] } |
| GET | /inventory/:id | Returns inventory for all widgets or specified widget by ID |
| POST | /inventory | Updates widget stock on an existing inventory record |
| | | { w_id: ID, stock: INT } |
