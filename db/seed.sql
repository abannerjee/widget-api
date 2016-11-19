-- MAIN SCHEMA (widget)

INSERT INTO widget.property (p_category, p_display_name) VALUES
  ('type', 'prime'),
  ('type', 'elite'),
  ('type', 'extreme edition'),
  ('color', 'red'),
  ('color', 'white'),
  ('color', 'blue'),
  ('color', 'chrome');

INSERT INTO widget.property (p_category, p_display_name, p_value) VALUES
  ('size', 'small', '1'),
  ('size', 'medium', '5'),
  ('size', 'large', '10'),
  ('size', 'x-large', '12');

-- TEST SCHEMA (test)

INSERT INTO test.property (p_category, p_display_name, p_value)
VALUES ('type', 'test-type', '1');

INSERT INTO test.property (p_category, p_display_name, p_value, p_parent, p_depth)
VALUES ('sub-type', 'prime-sub', '2', '1', '1');

INSERT INTO test.widget (w_name)
VALUES ('test-widget');

INSERT INTO test.inventory (i_widget_id, i_stock)
VALUES (1, 100);

INSERT INTO test.widget_property (wp_widget_id, wp_property_id)
VALUES (1, 1);

INSERT INTO test.order (o_widget_id, o_quantity)
VALUES (1, 10);