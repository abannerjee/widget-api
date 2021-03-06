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
  w_inherit integer[] DEFAULT ARRAY[currval('widget.widget_w_id_seq')]
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
  p_name varchar UNIQUE NOT NULL,
  p_value varchar
);

-- WidgetProperty
CREATE TABLE widget.widget_property (
  wp_id SERIAL PRIMARY KEY,
  wp_widget_id integer REFERENCES widget.widget,
  wp_property_id integer REFERENCES widget.property
);

-- User Orders
CREATE TABLE widget.user_order (
  u_id SERIAL PRIMARY KEY,
  u_created_on timestamp DEFAULT current_timestamp
);

-- Orders
CREATE TABLE widget.order (
  o_id SERIAL PRIMARY KEY,
  o_created_on timestamp DEFAULT current_timestamp,
  o_widget_id integer REFERENCES widget.widget,
  o_configuration integer[],
  o_user_order_id integer REFERENCES widget.user_order
);


-- TEST SCHEMA (test)

-- Widgets
CREATE TABLE test.widget (
  w_id SERIAL PRIMARY KEY,
  w_name varchar NOT NULL,
  w_inherit integer[] DEFAULT ARRAY[currval('test.widget_w_id_seq')]
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

-- User Orders
CREATE TABLE test.user_order (
  u_id SERIAL PRIMARY KEY,
  u_created_on timestamp DEFAULT current_timestamp
);

-- Orders
CREATE TABLE test.order (
  o_id SERIAL PRIMARY KEY,
  o_created_on timestamp DEFAULT current_timestamp,
  o_widget_id integer REFERENCES test.widget,
  o_configuration integer[],
  o_user_order_id integer REFERENCES test.user_order
);
