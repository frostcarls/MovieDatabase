import cx_Oracle

conn = cx_Oracle.connect('sys/sys_password@127.0.0.1/orcl')

print(conn.version)