-- MAIN SCHEMA (widget)

INSERT INTO widget.widget (w_name) VALUES
  ('super saver'),
  ('super deluxe'),
  ('ultra saver'),
  ('supreme deluxe');

INSERT INTO widget.widget (w_name, w_inherit) VALUES
  ('improved super save', '{1,5}');

INSERT INTO widget.property (p_category, p_name, p_value) VALUES
  ('type', 'prime', NULL),
  ('type', 'elite', NULL),
  ('type', 'extreme edition', NULL),
  ('color', 'red', NULL),
  ('color', 'white', NULL),
  ('color', 'blue', NULL),
  ('color', 'chrome', NULL),
  ('size', 'invisibly small', '1'),
  ('size', 'slightly medium', '5'),
  ('size', 'somewhat large', '10'),
  ('size', 'galactically huge', '100');

INSERT INTO widget.widget_property (wp_widget_id, wp_property_id) VALUES
  (1, 1), (1, 4), (1, 5), (1, 8),
  (2, 2), (2, 5), (2, 6), (2, 9),
  (3, 3), (3, 4), (3, 5), (3, 10),
  (4, 2), (4, 7), (4, 9),
  (5, 1), (5, 6), (5, 7), (5, 11);

-- TEST SCHEMA (test)

INSERT INTO test.widget (w_name) VALUES
  ('test-widget-1');

INSERT INTO test.widget (w_name, w_inherit) VALUES
  ('test-widget-2', '{2,1}');

INSERT INTO test.property (p_category, p_name, p_value) VALUES
  ('type', 'test-type-1', '1'),
  ('type', 'test-type-2', '2'),
  ('color', 'test-color-1', '1'),
  ('color', 'test-color-2', '2'),
  ('color', 'test-color-3', '3'),
  ('size', 'test-size-1', '1'),
  ('size', 'test-size-2', '2');

INSERT INTO test.inventory (i_widget_id, i_stock) VALUES
  (1, 100), (2, 50);

INSERT INTO test.widget_property (wp_widget_id, wp_property_id) VALUES
  (1, 1), (1, 3), (1, 4), (1, 6),
  (2, 2), (2, 5), (2, 7);

INSERT INTO test.order (o_widget_id, o_configuration) VALUES
  (1, '{1,5}');