-- Clear Existing Schema
DROP SCHEMA IF EXISTS widget CASCADE;
CREATE SCHEMA widget AUTHORIZATION widgetapi;

-- Grant permissions
GRANT ALL privileges ON ALL TABLES IN SCHEMA widget TO widgetapi;
GRANT USAGE ON SCHEMA widget TO widgetapi;

-- Users
CREATE TABLE widget.user (
  id SERIAL PRIMARY KEY,
  name varchar NOT NULL,
  pw varchar NOT NULL
);

-- Widgets
CREATE TABLE widget.widget (
  id SERIAL PRIMARY KEY,
  name varchar NOT NULL
);

-- Properties
CREATE TABLE widget.property (
  id SERIAL PRIMARY KEY,
  category varchar NOT NULL,
  display_name varchar NOT NULL,
  value varchar,
  parent integer REFERENCES widget.property (id),
  depth smallint DEFAULT 0
);

-- WidgetProperty
CREATE TABLE widget.widget_property (
  id SERIAL PRIMARY KEY,
  widget_id integer REFERENCES widget.widget (id),
  property_id integer REFERENCES widget.property (id)
);

-- Orders
CREATE TABLE widget.order (
  id SERIAL PRIMARY KEY,
  created_on timestamp default current_timestamp,
  user_id integer REFERENCES widget.user (id),
  widget_id integer REFERENCES widget.widget (id),
  quantity integer NOT NULL
);