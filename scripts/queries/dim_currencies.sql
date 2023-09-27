CREATE TABLE schezflix.warehouse.dim_currencies AS (
	SELECT DISTINCT currency_ AS currency, currency AS symbol
	FROM(
	SELECT DISTINCT currency,
		CASE WHEN currency = '$' THEN 'us_dollar'
			WHEN currency = '£' THEN 'pounds'
			WHEN currency = '€' THEN 'euros'
			WHEN currency = 'A$' THEN 'au_dollar'
		ELSE NULL END AS currency_
	FROM matches_nu
	) r
	WHERE currency_ IS NOT NULL AND currency IN ('$', '£','€','A$')
);

ALTER TABLE schezflix.warehouse.dim_currencies
ADD currencies_id SERIAL PRIMARY KEY;