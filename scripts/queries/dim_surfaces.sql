CREATE TABLE schezflix.warehouse.dim_surfaces AS (
	SELECT DISTINCT(court_surface) AS surface FROM matches_nu WHERE court_surface IS NOT NULL
);

ALTER TABLE schezflix.warehouse.dim_surfaces
ADD surface_id SERIAL PRIMARY KEY;