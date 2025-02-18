-- Main query
SELECT 
  passenger_count,
  trip_distance,
  trip_type,
  PULocationID,
  DOLocationID,
  payment_type,
  fare_amount,
  tolls_amount,
  tip_amount
FROM `de-zoomcamp-follow-project.de_zoomcamp_w2.rides_21_3`
LIMIT 20;

--CREATE TABLE WITH APPROPRIATE DATAV TYPES
CREATE OR REPLACE TABLE `de-zoomcamp-follow-project.de_zoomcamp_w2.rides_21_3_ML` (
  `passenger_count` FLOAT64,
  `trip_distance` FLOAT64,
  `trip_type` STRING,
  `PULocationID` STRING,
  `DOLocationID` STRING,
  `payment_type` STRING,
  `fare_amount` FLOAT64,
  `tolls_amount` FLOAT64,
  `tip_amount` FLOAT64
) AS (
  SELECT passenger_count,
         trip_distance,
         CAST(trip_type AS STRING),
         CAST(PULocationID AS STRING),
         CAST(DOLocationID AS STRING),
         CAST(payment_type AS STRING),
         fare_amount,
         tolls_amount,
         tip_amount
   FROM `de-zoomcamp-follow-project.de_zoomcamp_w2.rides_21_3`
);


--CREATE ML MODEL (LINEAR REGRESSION)
CREATE OR REPLACE MODEL `de-zoomcamp-follow-project.de_zoomcamp_w2.lr_model` 
OPTIONS(

  model_type = 'linear_reg',
  input_label_cols = ['tip_amount'],
  DATA_SPLIT_METHOD = 'AUTO_SPLIT'
) AS
(
  SELECT * FROM `de-zoomcamp-follow-project.de_zoomcamp_w2.rides_21_3_ML` WHERE tip_amount IS NOT NULL
);


