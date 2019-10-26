create or replace procedure rs(rel_pf in genome_tags.tag%type, rel_val in genome_scores.relevance%type)
as
cursor a is select * from genome_tags where tag = rel_pf;
cursor b(tagId number) is select * from genome_scores where relevance > rel_val;
cursor c(movieId1 number) is select * from movie inner join genome_scores on movieId = movieId1;
x genome_tags%rowtype;
y genome_scores%rowtype;
z movie%rowtype;

begin
	for x in a loop
		for y in b(x.tagId) loop
			for z in c(y.movieId) loop
			dbms_output.put_line(distinct(z.title));
			end loop;
		end loop;
	end loop;
end;
