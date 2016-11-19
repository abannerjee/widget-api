-- Clear Existing Schema
DROP SCHEMA IF EXISTS widget CASCADE;
DROP SCHEMA IF EXISTS test CASCADE;
CREATE SCHEMA widget AUTHORIZATION widgetapi;
CREATE SCHEMA test AUTHORIZATION widgetapi;

-- Grant permissions
GRANT ALL privileges ON ALL TABLES IN SCHEMA widget TO widgetapi;
GRANT ALL privileges ON ALL TABLES IN SCHEMA test TO widgetapi;
GRANT USAGE ON SCHEMA widget TO widgetapi;
GRANT USAGE ON SCHEMA test TO widgetapi;

-- MAIN SCHEMA (widget)

-- Users
CREATE TABLE widget.user (
  u_id SERIAL PRIMARY KEY,
  u_name varchar NOT NULL,
  u_pw varchar NOT NULL
);

-- Widgets
CREATE TABLE widget.widget (
  w_id SERIAL PRIMARY KEY,
  w_name varchar NOT NULL
);

-- Properties
CREATE TABLE widget.property (
  p_id SERIAL PRIMARY KEY,
  p_category varchar NOT NULL,
  p_display_name varchar NOT NULL,
  p_value varchar,
  p_parent integer REFERENCES widget.property,
  p_depth smallint DEFAULT 0
);

-- WidgetProperty
CREATE TABLE widget.widget_property (
  wp_id SERIAL PRIMARY KEY,
  wp_widget_id integer REFERENCES widget.widget,
  wp_property_id integer REFERENCES widget.property
);

-- Orders
CREATE TABLE widget.order (
  o_id SERIAL PRIMARY KEY,
  o_created_on timestamp default current_timestamp,
  o_user_id integer REFERENCES widget.user,
  o_widget_id integer REFERENCES widget.widget,
  o_quantity integer NOT NULL
);


-- TEST SCHEMA (test)

-- Users
CREATE TABLE test.user (
  u_id SERIAL PRIMARY KEY,
  u_name varchar NOT NULL,
  u_pw varchar NOT NULL
);

-- Widgets
CREATE TABLE test.widget (
  w_id SERIAL PRIMARY KEY,
  w_name varchar NOT NULL
);

-- Properties
CREATE TABLE test.property (
  p_id SERIAL PRIMARY KEY,
  p_category varchar NOT NULL,
  p_display_name varchar NOT NULL,
  p_value varchar,
  p_parent integer REFERENCES test.property,
  p_depth smallint DEFAULT 0
);

-- WidgetProperty
CREATE TABLE test.widget_property (
  wp_id SERIAL PRIMARY KEY,
  wp_widget_id integer REFERENCES test.widget,
  wp_property_id integer REFERENCES test.property
);

-- Orders
CREATE TABLE test.order (
  o_id SERIAL PRIMARY KEY,
  o_created_on timestamp default current_timestamp,
  o_user_id integer REFERENCES test.user,
  o_widget_id integer REFERENCES test.widget,
  o_quantity integer NOT NULL
);