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

-- Widgets
CREATE TABLE widget.widget (
  w_id SERIAL PRIMARY KEY,
  w_name varchar NOT NULL,
  w_parent integer REFERENCES widget.widget,
  w_depth smallint DEFAULT 0
);

-- Inventory
CREATE TABLE widget.inventory (
  i_id SERIAL PRIMARY KEY,
  i_widget_id integer REFERENCES widget.widget,
  i_stock integer DEFAULT 0
);

-- Properties
CREATE TABLE widget.property (
  p_id SERIAL PRIMARY KEY,
  p_category varchar NOT NULL,
  p_name varchar NOT NULL,
  p_value varchar
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
  o_widget_id integer REFERENCES widget.widget,
  o_configuration integer[]
);


-- TEST SCHEMA (test)

-- Widgets
CREATE TABLE test.widget (
  w_id SERIAL PRIMARY KEY,
  w_name varchar NOT NULL,
  w_parent integer REFERENCES test.widget,
  w_depth smallint DEFAULT 0
);

-- Inventory
CREATE TABLE test.inventory (
  i_id SERIAL PRIMARY KEY,
  i_widget_id integer REFERENCES test.widget,
  i_stock integer DEFAULT 0
);

-- Properties
CREATE TABLE test.property (
  p_id SERIAL PRIMARY KEY,
  p_category varchar NOT NULL,
  p_name varchar NOT NULL,
  p_value varchar
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
  o_widget_id integer REFERENCES test.widget,
  o_configuration integer[]
);
