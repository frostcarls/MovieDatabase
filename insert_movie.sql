create or replace procedure ins_movie(movie_title in movie.title%type,movie_genre1 in movie.genre%type,movie_genre2 in movie.genre%type,movie_genre3 in movie.genre%type)
is   
movie_id number;
ch varchar(1):='y';
ch2 varchar(1):='y';
i number:=0;
begin
select max(movieId) into movie_id from movie;
movie_id:=movie_id+1;
insert into movie 	
values(movie_id,movie_title,movie_genre1);
insert into movie 	
values(movie_id,movie_title,movie_genre2);
insert into movie 	
values(movie_id,movie_title,movie_genre3);
delete movie
where genre='NULL';
end;
/