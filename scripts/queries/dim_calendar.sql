DO $$ 
DECLARE 
    min_date DATE;
    max_date DATE;
    cur_date DATE;
BEGIN
    -- Step 1: Find the minimum and maximum date values
    SELECT MIN(start_date), MAX(end_date)
    INTO min_date, max_date
    FROM matches_nu;

    -- Step 2: Create a calendar dimension table
    CREATE TABLE schezflix.warehouse.dim_calendar (
        date_id date PRIMARY KEY,
        year integer,
        quarter integer,
        month integer,
        day integer,
		day_of_week integer,
		is_weekend boolean
    );

    -- Step 3: Populate the calendar dimension table
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
END $$;