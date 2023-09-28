CREATE TABLE schezflix.warehouse.fact_matches AS (
	SELECT 
		matches.index AS id,
		matches.start_date,
		matches.end_date,
		-- matches.location -- dim_location_id,
		--matches.surface
		matches.prize_money,
		-- currency id
		matches.year,
		-- matches. player_id
		-- matches.opponent_id
		-- tournament 
		-- round
		matches.num_sets,
		matches.sets_won,
		matches.games_won,
		matches.games_against,
		matches.tiebreaks_won,
		matches.tiebreaks_total,
		matches.serve_rating,
		matches.aces,
		matches.double_faults,
		matches.first_serve_made,
		matches.first_serve_attempted,
		matches.first_serve_points_made,
		matches.first_serve_points_attempted,
		matches.second_serve_points_made,
		matches.second_serve_points_attempted,
		matches.break_points_saved,
		matches.break_points_against,
		matches.service_games_won,
		matches.return_rating INTEGER,
		matches.first_serve_return_points_made,
		matches.first_serve_return_points_attempted,
		matches.second_serve_return_points_made,
		matches.second_serve_return_points_attempted,
		matches.break_points_made,
		matches.break_points_attempted,
		matches.return_games_played,
		matches.service_points_won,
		matches.service_points_attempted,
		matches.return_points_won,
		matches.return_points_attempted,
		matches.total_points_won,
		matches.total_points,
		matches.duration
        -- matches.player_victory 
        -- matches.retirement 
        -- matches.seed
        -- matches.won_first_set
        -- matches.doubles
        -- matches.masters
        -- matches.round_num
        -- matches.nation
	FROM schezflix.public.matches	
);

ALTER TABLE schezflix.warehouse.fact_matches
ADD PRIMARY KEY (id);



SELECT * FROM schezflix.warehouse.fact_matches

SELECT * FROM schezflix.public.matches_nu

SELECT * FROM schezflix.public.countries
SELECT * FROM schezflix.public.matches_nu LIMIT 100

CREATE TABLE schezflix.warehouse.fact_matches AS (
	SELECT 
		matches_nu.index AS id,
		matches_nu.start_date,
		matches_nu.end_date,
		dim_countries.index,
		-- matches.location -- dim_location_id,
		
		-- IDs
		warehouse.dim_surfaces.surface_id
		matches_nu.prize_money,
		-- currency id
		matches_nu.year,
		-- matches. player_id
		-- matches.opponent_id
		-- tournament 
		-- round
		matches_nu.num_sets,
		matches_nu.sets_won,
		matches_nu.games_won,
		matches_nu.games_against,
		matches_nu.tiebreaks_won,
		matches_nu.tiebreaks_total,
		matches_nu.serve_rating,
		matches_nu.aces,
		matches_nu.double_faults,
		matches_nu.first_serve_made,
		matches_nu.first_serve_attempted,
		matches_nu.first_serve_points_made,
		matches_nu.first_serve_points_attempted,
		matches_nu.second_serve_points_made,
		matches_nu.second_serve_points_attempted,
		matches_nu.break_points_saved,
		matches_nu.break_points_against,
		matches_nu.service_games_won,
		matches_nu.return_rating INTEGER,
		matches_nu.first_serve_return_points_made,
		matches_nu.first_serve_return_points_attempted,
		matches_nu.second_serve_return_points_made,
		matches_nu.second_serve_return_points_attempted,
		matches_nu.break_points_made,
		matches_nu.break_points_attempted,
		matches_nu.return_games_played,
		matches_nu.service_points_won,
		matches_nu.service_points_attempted,
		matches_nu.return_points_won,
		matches_nu.return_points_attempted,
		matches_nu.total_points_won,
		matches_nu.total_points,
		matches_nu.duration
        -- matches.player_victory 
        -- matches.retirement 
        -- matches.seed
        -- matches.won_first_set
        -- matches.doubles
        -- matches.masters
        -- matches.round_num
        -- matches.nation
	FROM schezflix.public.matches_nu
	LEFT JOIN dim_countries ON schezflix.public.matches_nu.location = schezflix.warehouse.dim_countries.code
);

SELECT DISTINCT location FROM matches_nu

SELECT ali.location, cou.code 
FROM schezflix.public.matches_nu ali
LEFT JOIN schezflix.warehouse.dim_countries cou ON ali.location = cou.code
WHERE cou.code IS NULL AND ali.location IS NOT NULL

SELECT * FROM schezflix.warehouse.dim_countries WHERE code = 'RSA'


ALTER TABLE schezflix.warehouse.fact_matches
ADD PRIMARY KEY (id);


SELECT * FROM schezflix.warehouse.fact_matches LIMIT 10


