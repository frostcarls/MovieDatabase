create or replace procedure pprint
as 
	a number;
begin
	select count(*) into a from tt;
	dbms_output.put_line(a);
end;
/

set serveroutput on;
execute pprint;
