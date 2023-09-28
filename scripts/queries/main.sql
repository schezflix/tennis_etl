DO $$
-- dim_calendar
DECLARE 
    min_date DATE;
    max_date DATE;
    cur_date DATE;
BEGIN
    -- Find the minimum and maximum date values
    SELECT MIN(start_date), MAX(end_date)
    INTO min_date, max_date
    FROM matches_nu;

    -- Create a calendar dimension table
    CREATE TABLE schezflix.warehouse.dim_calendar (
        date_id date PRIMARY KEY,
        year integer,
        quarter integer,
        month integer,
        day integer,
		day_of_week integer,
		is_weekend boolean
    );

    -- Populate the calendar dimension table
    cur_date := min_date;
    WHILE cur_date <= max_date LOOP
        INSERT INTO schezflix.warehouse.dim_calendar (date_id, year, quarter, month, day, day_of_week, is_weekend)
        VALUES (cur_date,
				EXTRACT(YEAR FROM cur_date),
				EXTRACT(QUARTER FROM cur_date),
				EXTRACT(MONTH FROM cur_date),
				EXTRACT(DAY FROM cur_date),
				EXTRACT(DOW FROM cur_date), 
				EXTRACT(ISODOW FROM cur_date) IN (6, 7));
        cur_date := cur_date + 1;
    END LOOP;


-- dim_currencies
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


-- dim_rounds
    CREATE TABLE schezflix.warehouse.dim_rounds AS (
	SELECT DISTINCT round_ round
	FROM
    (SELECT DISTINCT round,
		CASE WHEN round = '0' THEN NULL
			WHEN round = '1' THEN '1st Round Qualifying'
			WHEN round = '2' THEN '2nd Round Qualifying'
			WHEN round = '3' THEN '3rd Round Qualifying'
		ELSE round END AS round_
	FROM matches_nu) r
	WHERE round_ IS NOT NULL
    );

    ALTER TABLE schezflix.warehouse.dim_rounds
    ADD rounds_id SERIAL PRIMARY KEY;

-- dim_surfaces
    CREATE TABLE schezflix.warehouse.dim_surfaces AS (
        SELECT DISTINCT(court_surface) AS surface FROM matches_nu WHERE court_surface IS NOT NULL
    );

    ALTER TABLE schezflix.warehouse.dim_surfaces
    ADD surface_id SERIAL PRIMARY KEY;
END $$;