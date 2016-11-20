-- MAIN SCHEMA (widget)

INSERT INTO widget.widget (w_name, w_parent, w_depth) VALUES
  ('prime', NULL, 0),
  ('elite', NULL, 0),
  ('extreme edition', NULL, 0);

INSERT INTO widget.property (p_type, p_name, p_value) VALUES
  ('color', 'red', NULL),
  ('color', 'white', NULL),
  ('color', 'blue', NULL),
  ('color', 'chrome', NULL),
  ('size', 'invisibly small', '1'),
  ('size', 'slightly medium', '5'),
  ('size', 'somewhat large', '10'),
  ('size', 'galactically huge', '100');

-- TEST SCHEMA (test)

INSERT INTO test.widget (w_name, w_parent, w_depth) VALUES
  ('test-widget', NULL, 0);

INSERT INTO test.property (p_type, p_name, p_value) VALUES
  ('test-type', 'test-property', '1');

INSERT INTO test.inventory (i_widget_id, i_stock) VALUES
  (1, 100);

INSERT INTO test.widget_property (wp_widget_id, wp_property_id) VALUES
  (1, 1);

INSERT INTO test.order (o_widget_id, o_configuration) VALUES
  (1, [1,5]);