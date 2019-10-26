create table genome_scores(
movieId number,
tagId number,
relevance number(*,3));

create table genome_tags(
tagId number,
tag varchar(20));

create table link(
movieId number primary key,
imdbId number,
tmdbId number);

create table movie(
movieId number,
title varchar(30),
genre varchar(30));

create table rating(
userId number,
movieId number,
score number(*,2));


create table tag(
movieId number,
tag varchar(20),
timestamp varchar(25));

