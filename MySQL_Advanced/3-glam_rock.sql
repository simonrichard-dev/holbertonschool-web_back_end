-- script that creates a trigger that decreases
-- the quantity of an item after adding a new order.

SELECT  band_name,(ifnull(split,2020) - ifnull(formed,0)) lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
