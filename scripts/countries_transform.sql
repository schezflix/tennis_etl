SELECT DISTINCT matches_nu.location m_name, countries.code AS c_code, countries.name AS c_name,
	CASE WHEN countries.code IS NULL AND schezflix.public.matches_nu.location = 'Lesser Antilles' THEN 'LALL'
		WHEN countries.code IS NULL THEN matches_nu.location
		ELSE matches_nu.location END AS nu_code,
	CASE WHEN matches_nu.location  = '01A' THEN 'Other' 
		WHEN matches_nu.location  = 'AHO' THEN 'Netherlands Antilles'
		WHEN matches_nu.location = 'ALG' THEN 'Algeria' 
		WHEN matches_nu.location = 'ARU' THEN 'Aruba' 
		WHEN matches_nu.location = 'BAH' THEN 'Bahrain' 
		WHEN matches_nu.location = 'BAN' THEN 'Bangladesh' 
		WHEN matches_nu.location = 'BAR' THEN 'Barbados' 
		WHEN matches_nu.location = 'BER' THEN 'Bermuda' 
		WHEN matches_nu.location = 'BOT' THEN 'Botswana' 
		WHEN matches_nu.location = 'BRU' THEN 'Bru' 
		WHEN matches_nu.location = 'BUL' THEN 'Bul' 
		WHEN matches_nu.location = 'CAL' THEN 'Cal' 
		WHEN matches_nu.location = 'CAM' THEN 'Cambodia' 
		WHEN matches_nu.location = 'CAY' THEN 'Cayman Islands' 
		WHEN matches_nu.location = 'CHI' THEN 'China' 
		WHEN matches_nu.location = 'CRC' THEN 'Costa Rica' 
		WHEN matches_nu.location = 'CRO' THEN 'Croatia' 
		WHEN matches_nu.location = 'DEN' THEN 'Denmark' 
		WHEN matches_nu.location = 'ESA' THEN 'El Salvador' 
		WHEN matches_nu.location = 'FIJ' THEN 'Fiji' 
		WHEN matches_nu.location = 'GRE' THEN 'Greece' 
		WHEN matches_nu.location = 'GUA' THEN 'Guadalupe' 
		WHEN matches_nu.location = 'GUD' THEN 'Gud' 
		WHEN matches_nu.location = 'HON' THEN 'Honduras' 
		WHEN matches_nu.location = 'INA' THEN 'Indonesia' 
		WHEN matches_nu.location = 'IRI' THEN 'Iran' 
		WHEN matches_nu.location = 'KSA' THEN 'Saudi Arabia' 
		WHEN matches_nu.location = 'KUW' THEN 'Kuwait' 
		WHEN matches_nu.location = 'LAT' THEN 'Latvia' 
		WHEN matches_nu.location = 'LBA' THEN 'Lybia' 
		WHEN matches_nu.location = 'Lesser Antilles' THEN matches_nu.location 
		WHEN matches_nu.location = 'MAS' THEN 'Malasya' 
		WHEN matches_nu.location = 'MRI' THEN 'Mauritius' 
		WHEN matches_nu.location = 'MRN' THEN 'Mrn' 
		WHEN matches_nu.location = 'NCA' THEN 'Nicaragua' 
		WHEN matches_nu.location = 'NED' THEN 'Netherlands' 
		WHEN matches_nu.location = 'NGR' THEN 'Nigeria' 
		WHEN matches_nu.location = 'NMI' THEN 'Nmi' 
		WHEN matches_nu.location = 'OMA' THEN 'Oman' 
		WHEN matches_nu.location = 'PAR' THEN 'Paraguay' 
		WHEN matches_nu.location = 'PHI' THEN 'Phillipines' 
		WHEN matches_nu.location = 'POR' THEN 'Portugal' 
		WHEN matches_nu.location = 'PUR' THEN 'Puerto rico' 
		WHEN matches_nu.location = 'RSA' THEN 'South Africa' 
        WHEN matches_nu.location = 'SCG' THEN 'Scg' 
		WHEN matches_nu.location = 'SIN' THEN 'Singapore' 
		WHEN matches_nu.location = 'SLO' THEN 'Slovenia' 
		WHEN matches_nu.location = 'SRI' THEN 'Sri Lanka' 
		WHEN matches_nu.location = 'SUD' THEN 'Sudan' 
		WHEN matches_nu.location = 'SUI' THEN 'Switzerland' 
		WHEN matches_nu.location = 'TCH' THEN 'Tch' 
		WHEN matches_nu.location = 'TOG' THEN 'Togo' 
		WHEN matches_nu.location = 'TPE' THEN 'Taiwan' 
		WHEN matches_nu.location = 'TRI' THEN 'Cal' 
		WHEN matches_nu.location = 'UAE' THEN 'United Arab Emirates' 
		WHEN matches_nu.location = 'URU' THEN 'Uruguay' 
		WHEN matches_nu.location = 'VIE' THEN 'Vietnam' 
		WHEN matches_nu.location = 'VIN' THEN 'Saint Vincent and the Grenadines' 
		WHEN matches_nu.location = 'YUG' THEN 'Yugoslavia' 
		WHEN matches_nu.location = 'ZAM' THEN 'Zambia' 
		WHEN matches_nu.location = 'ZIM' THEN 'Zimbabwe' 
		ELSE countries.name END AS nu_name
FROM schezflix.public.matches_nu
LEFT JOIN schezflix.public.countries 
	ON schezflix.public.countries.code = schezflix.public.matches_nu.location
ORDER BY matches_nu.location;


-- add values to antartica region and subregion
UPDATE schezflix.warehouse.dim_countries
SET sub_region = 'Antartica'
WHERE sub_region IS NULL;

UPDATE schezflix.warehouse.dim_countries
SET region = 'Antartica'
WHERE region IS NULL;


-- CREATE dim_countries:
CREATE TABLE schezflix.warehouse.dim_countries AS (
	SELECT al.ind AS ID,
		al.nu_code AS code,
		al.nu_name AS name,
		al.region AS region,
		al.sub_region AS sub_region
	FROM 
	(SELECT DISTINCT matches_nu.location m_name, countries.code AS c_code, countries.name AS c_name, countries.index AS ind, countries.region AS region,
	 countries.sub_region AS sub_region,
		CASE WHEN countries.code IS NULL AND schezflix.public.matches_nu.location = 'Lesser Antilles' THEN 'LALL'
			WHEN countries.code IS NULL THEN matches_nu.location
		ELSE countries.code END AS nu_code,
		CASE WHEN matches_nu.location  = '01A' THEN 'Other' 
			WHEN matches_nu.location  = 'AHO' THEN 'Netherlands Antilles'
			WHEN matches_nu.location = 'ALG' THEN 'Algeria' 
			WHEN matches_nu.location = 'ARU' THEN 'Aruba' 
			WHEN matches_nu.location = 'BAH' THEN 'Bahrain' 
			WHEN matches_nu.location = 'BAN' THEN 'Bangladesh' 
			WHEN matches_nu.location = 'BAR' THEN 'Barbados' 
			WHEN matches_nu.location = 'BER' THEN 'Bermuda' 	
			WHEN matches_nu.location = 'BOT' THEN 'Botswana' 
			WHEN matches_nu.location = 'BRU' THEN 'Bru' 
			WHEN matches_nu.location = 'BUL' THEN 'Bul' 
			WHEN matches_nu.location = 'CAL' THEN 'Cal' 
			WHEN matches_nu.location = 'CAM' THEN 'Cambodia' 
			WHEN matches_nu.location = 'CAY' THEN 'Cayman Islands' 
			WHEN matches_nu.location = 'CHI' THEN 'China' 
			WHEN matches_nu.location = 'CRC' THEN 'Costa Rica' 
			WHEN matches_nu.location = 'CRO' THEN 'Croatia' 
			WHEN matches_nu.location = 'DEN' THEN 'Denmark' 
			WHEN matches_nu.location = 'ESA' THEN 'El Salvador' 
			WHEN matches_nu.location = 'FIJ' THEN 'Fiji' 
			WHEN matches_nu.location = 'GRE' THEN 'Greece' 
			WHEN matches_nu.location = 'GUA' THEN 'Guadalupe' 
			WHEN matches_nu.location = 'GUD' THEN 'Gud' 
			WHEN matches_nu.location = 'HON' THEN 'Honduras' 
			WHEN matches_nu.location = 'INA' THEN 'Indonesia' 
			WHEN matches_nu.location = 'IRI' THEN 'Iran' 
			WHEN matches_nu.location = 'KSA' THEN 'Saudi Arabia' 
			WHEN matches_nu.location = 'KUW' THEN 'Kuwait' 
			WHEN matches_nu.location = 'LAT' THEN 'Latvia' 
			WHEN matches_nu.location = 'LBA' THEN 'Lybia' 
			WHEN matches_nu.location = 'Lesser Antilles' THEN matches_nu.location 
			WHEN matches_nu.location = 'MAS' THEN 'Malasya' 
			WHEN matches_nu.location = 'MRI' THEN 'Mauritius' 
			WHEN matches_nu.location = 'MRN' THEN 'Mrn' 
			WHEN matches_nu.location = 'NCA' THEN 'Nicaragua' 
			WHEN matches_nu.location = 'NED' THEN 'Netherlands' 
			WHEN matches_nu.location = 'NGR' THEN 'Nigeria' 
			WHEN matches_nu.location = 'NMI' THEN 'Nmi' 
			WHEN matches_nu.location = 'OMA' THEN 'Oman' 
			WHEN matches_nu.location = 'PAR' THEN 'Paraguay' 
			WHEN matches_nu.location = 'PHI' THEN 'Phillipines' 
			WHEN matches_nu.location = 'POR' THEN 'Portugal' 
			WHEN matches_nu.location = 'PUR' THEN 'Puerto rico' 
			WHEN matches_nu.location = 'RSA' THEN 'South Africa' 
			WHEN matches_nu.location = 'SCG' THEN 'Scg' 
			WHEN matches_nu.location = 'SIN' THEN 'Singapore' 
			WHEN matches_nu.location = 'SLO' THEN 'Slovenia' 
			WHEN matches_nu.location = 'SRI' THEN 'Sri Lanka' 
			WHEN matches_nu.location = 'SUD' THEN 'Sudan' 
			WHEN matches_nu.location = 'SUI' THEN 'Switzerland' 
			WHEN matches_nu.location = 'TCH' THEN 'Tch' 
			WHEN matches_nu.location = 'TOG' THEN 'Togo' 
			WHEN matches_nu.location = 'TPE' THEN 'Taiwan' 
			WHEN matches_nu.location = 'TRI' THEN 'Cal' 
			WHEN matches_nu.location = 'UAE' THEN 'United Arab Emirates' 
			WHEN matches_nu.location = 'URU' THEN 'Uruguay' 
			WHEN matches_nu.location = 'VIE' THEN 'Vietnam' 
			WHEN matches_nu.location = 'VIN' THEN 'Saint Vincent and the Grenadines' 
			WHEN matches_nu.location = 'YUG' THEN 'Yugoslavia' 
			WHEN matches_nu.location = 'ZAM' THEN 'Zambia' 
			WHEN matches_nu.location = 'ZIM' THEN 'Zimbabwe' 
			ELSE countries.name END AS nu_name
FROM schezflix.public.countries 
LEFT JOIN schezflix.public.matches_nu
	ON schezflix.public.countries.code = schezflix.public.matches_nu.location
ORDER BY ind) al
)
