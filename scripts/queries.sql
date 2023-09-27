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




