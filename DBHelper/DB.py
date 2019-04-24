from config import db_info
import psycopg2


class DBConnect:
    def __init__(self):
        self.conn = psycopg2.connect(db_info)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def read_all_ip_port(self):
        with self.conn.cursor() as c:
            c.execute('select * from basic_info where service is null')
            result = c.fetchall()
        return result

    def write_ip_port(self, ip_list):
        with self.conn.cursor() as c:
            c.executemany("""INSERT INTO basic_info(ip,port,task_id) VALUES (%(ip)s, %(port)s,%(task_id)s)""", ip_list)
            self.conn.commit()
        return True

    def insert_serviceandinfo(self, info_list):
        with self.conn.cursor() as c:
            c.execute("""UPDATE basic_info set service = %(service)s, system_info = %(sysinfo)s, details = %(details)s where task_id=%(task_id)s and port=%(port)s""",
                      info_list)
            self.conn.commit()
        return True


