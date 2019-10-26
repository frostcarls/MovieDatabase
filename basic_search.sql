create or replace procedure basic_search(name in movie.title%type)
as 
cursor a is select * from movie where title = name;
x movie%rowtype;
  c number:=0;
begin
    open a;
    fetch a into x;
    while(a%found) 
    loop
        dbms_output.put_line(x.title||'   '||x.genre);
	c:=1;
	exit;
        fetch a into x;
    end loop;
	if c = 0 then
		dbms_output.put_line('Movie Not found');
	end if;
end;
/
