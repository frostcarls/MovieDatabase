  create or replace procedure rs(rel_pf in genome_tags.tag%type, rel_val in genome_scores.relevance%type)
  as
  cursor b(tagId1 number) is select * from genome_scores where relevance > rel_val and tagId1 = genome_scores.tagId;
  cursor c(movieId1 number) is select * from movie where movie.movieId = movieId1;
  t movie.title%type;
  x genome_tags.tagId%type;
  y genome_scores%rowtype;
  z movie%rowtype;
  begin
  t:='asdf';
  select tagId into x from genome_tags where tag = rel_pf;
  for y in b(x) loop
  for z in c(y.movieId) loop
if t != z.title then
  t:=z.title;
  dbms_output.put_line('Movie Name : '||z.title);
end if;
  end loop;
  end loop;
  end;
/
