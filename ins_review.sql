create or replace procedure ins_review(user_id rating.userId%type,movie_title movie.title%type,rati rating.score%type)
as 
cursor c is select movieId from movie where lower(movie.title)=lower(movie_title); 
movie_id movie.movieId%type;	
begin
for bb in c loop
movie_id:=bb.movieId;
exit;
end loop;
insert into rating
values(user_id,movie_id,rati);
end;
/



execute ins_review();
	
