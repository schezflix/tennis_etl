DELETE FROM public.matches_nu
WHERE round = '0';

DELETE FROM public.matches_nu
WHERE currency NOT IN ('$', '£','€','A$');