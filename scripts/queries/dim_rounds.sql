CREATE TABLE schezflix.warehouse.dim_rounds AS (
	SELECT DISTINCT round_ round
	FROM(
	SELECT DISTINCT round,
		CASE WHEN round = '0' THEN NULL
			WHEN round = '1' THEN '1st Round Qualifying'
			WHEN round = '2' THEN '2nd Round Qualifying'
			WHEN round = '3' THEN '3rd Round Qualifying'
		ELSE round END AS round_
	FROM matches_nu
	) r
	WHERE round_ IS NOT NULL
);

ALTER TABLE schezflix.warehouse.dim_rounds
ADD rounds_id SERIAL PRIMARY KEY;