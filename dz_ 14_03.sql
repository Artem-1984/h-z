-- 1. Подсчитать количество групп, в которые вступил каждый пользователь.(кол-во груп у каждого пользователя) 
-- 	Вывести имя фамилию телефон и кол-во группю
SELECT firstname,lastname,users.phone,
count(users_communities.user_id)
FROM users
JOIN users_communities on users.id = users_communities.user_id 
JOIN communities on users_communities.community_id = communities.id
group by user_id
order by users_communities.user_id;


-- 2. Подсчитать количество пользователей в 
-- каждом сообществе и вывесли название сообщества.
SELECT  communities.name,count(user_id)
FROM users_communities
join communities on users_communities.community_id = communities.id 
group by community_id;


-- 3. Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, 
-- 	который больше всех общался с выбранным пользователем (написал ему сообщений).
from messages
where to_user_id in (select to_user_id
					from messages
                    where from_user_id = 2)
group by to_user_id
order by 'кол-во сообщений' desc
limit 1;


-- *4. Подсчитать общее количество лайков, которые получили пользователи младше 18 лет..
SELECT count(*) as "лайки пользователям младше 18 лет"
from likes
inner join media
on likes.media_id = media_id
inner join profiles
on media.user_id = profiles.user_id
where datediff(now(), birthday) < 18 * 365; 


-- *5. Определить кто больше поставил лайков (всего): мужчины или женщины.
SELECT count(profiles.gender) as 'count', profiles.gender
from likes
inner join media
on likes.media_id = media_id
inner join profiles
on media.user_id = profiles.user_id
group by profiles.gender ;