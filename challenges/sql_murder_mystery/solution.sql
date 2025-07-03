SELECT * 
  FROM crime_scene_report
 where date = '20180115' AND type = 'murder'

date	type	description	city
20180115	murder	Life? Dont talk to me about life.	Albany
20180115	murder	Mama, I killed a man, put a gun against his head...	Reno
20180115	murder	Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".	SQL City



2witnesses:

- lives at the last house on "Northwestern Dr". 
SELECT * 
FROM person
join interview
on interview.person_id = person.id
where address_street_name = 'Northwestern Dr'
order by id
desc LIMIT 1

id	name	license_id	address_number	address_street_name	ssn	person_id	transcript
96595	Coretta Cubie	303645	3631	Northwestern Dr	378403829	96595	head in the lap of her sister, who was gently brushing away some dead

- named Annabel, lives somewhere on "Franklin Ave".	SQL City
SELECT * 
FROM person
join interview
on interview.person_id = person.id
where name Like '%Annabel%' AND address_street_name = 'Franklin Ave'

id	name	license_id	address_number	address_street_name	ssn	person_id	transcript
16371	Annabel Miller	490173	103	Franklin Ave	318771143	16371	I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.



the killer from my gym when I was working out last week on January the 9th.
SELECT * 
FROM get_fit_now_check_in
join get_fit_now_member
on get_fit_now_check_in.membership_id = get_fit_now_member.id
join person
on get_fit_now_member.person_id = person.id
where check_in_date Like '%0109'
order by check_in_date

SELECT get_fit_now_check_in.check_in_date, person.id, person.name, interview.transcript
FROM get_fit_now_check_in
join get_fit_now_member
on get_fit_now_check_in.membership_id = get_fit_now_member.id
join person
on get_fit_now_member.person_id = person.id
join interview
on person.id = interview.person_id
where check_in_date Like '20180109'
order by check_in_date

check_in_date	id	name	transcript
20180109	67318	Jeremy Bowers	I was hired by a woman with a lot of money. 
I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). 
She has red hair and she drives a Tesla Model S. 
I know that she attended the SQL Symphony Concert 3 times in December 2017.


SELECT *
from person
join drivers_license
on drivers_license.id = person.license_id
join facebook_event_checkin
on facebook_event_checkin.person_id = person.id
where height >= 65 and height <= 67 and hair_color = "red" and car_make = "Tesla" and facebook_event_checkin.date Like "201712%"
