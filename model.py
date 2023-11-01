import time
import psycopg2
from psycopg2 import DataError

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='banana',
            host='localhost',
            port=5432
        )

    def add_task_tab1(self, userid, title, description):
        c = self.conn.cursor()
        try:
            query = 'INSERT INTO public."USER" ("user_ID", username, email) VALUES (%s, %s, %s)'
            data = (userid, title, description)
            c.execute(query, data)
            self.conn.commit()
            print("Task added successfully!")
        except DataError as e:
            print(f"Error: {e}")

    def add_task_tab2(self, projectid, userid, title, description):
        c = self.conn.cursor()
        try:
            check_user_query = 'SELECT 1 FROM public."USER" WHERE "user_ID" = %s'
            c.execute(check_user_query, (userid,))
            user_exists = c.fetchone()
            if not user_exists:
                print("Error: The specified user_id does not exist.")
            else:
                query = 'INSERT INTO public."Projects" ("project_ID", "user_ID", projectname, "Date_of_publication") VALUES (%s, %s, %s, %s)'
                data = (projectid, userid, title, description)
                c.execute(query, data)
                self.conn.commit()
                print("Task added successfully!")
        except psycopg2.DataError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def add_task_tab3(self, commentid, projectid, userid, title, description):
        c = self.conn.cursor()
        try:
            check_user_query = 'SELECT 1 FROM public."USER" WHERE "user_ID" = %s'
            c.execute(check_user_query, (userid,))
            user_exists = c.fetchone()
            check_project_query = 'SELECT 1 FROM public."Projects" WHERE "project_ID" = %s'
            c.execute(check_project_query, (projectid,))
            project_exists = c.fetchone()
            if not user_exists:
                print("Error: The specified user_id does not exist.")
            elif not project_exists:
                print("Error: The specified project_id does not exist.")
            else:
                query = 'INSERT INTO public."Comments" ("comment_id", "user_id", "project_id", "text", "date_of_publication") VALUES (%s, %s, %s, %s, %s)'
                data = (commentid, userid, projectid, title, description)
                c.execute(query, data)
                self.conn.commit()
                print("Comment added successfully!")
        except psycopg2.DataError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


    def get_all_tasks_tab1(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."USER"')
        return c.fetchall()
    def get_all_tasks_tab2(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Projects"')
        return c.fetchall()
    def get_all_tasks_tab3(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM public."Comments"')
        return c.fetchall()

    def update_task_tab1(self, task_id, title, description):
        c = self.conn.cursor()
        c.execute('UPDATE public."USER" SET username=%s, email=%s WHERE "user_ID"=%s', (title, description, task_id))
        self.conn.commit()


    def update_task_tab2(self, task_id, title, description):
        c = self.conn.cursor()
        c.execute('UPDATE public."Projects" SET projectname=%s, "Date_of_publication"=%s WHERE "project_ID"=%s', (title, description, task_id))
        self.conn.commit()

    def update_task_tab3(self, task_id, title, description):
        c = self.conn.cursor()
        c.execute('UPDATE public."Comments" SET text=%s, Date_of_publication=%s WHERE comment_ID=%s', (title, description, task_id))
        self.conn.commit()

    def delete_task_tab1(self, task_id):
        c = self.conn.cursor()
        try:
            c.execute("""
                    WITH referenced_rows AS (
                        SELECT "user_id" FROM public."Comments" WHERE "user_id" = %s
                        UNION
                        SELECT "user_ID" FROM public."Projects" WHERE "user_ID" = %s
                    )
                    DELETE FROM public."USER" WHERE "user_ID" = %s
                    AND NOT EXISTS (SELECT 1 FROM referenced_rows);
                     """, (task_id, task_id, task_id))
            self.conn.commit()
            print("Deleted!" if c.rowcount > 0 else "The record could not be deleted")
        except Exception as e:
            self.conn.rollback()

    def delete_task_tab2(self, task_id):
        c = self.conn.cursor()
        try:
            c.execute("""
            WITH referenced_rows AS (
                SELECT DISTINCT "project_id" 
                FROM public."Comments" WHERE "project_id" = %s)
                DELETE FROM public."Projects" WHERE "project_ID" = %s
                AND NOT EXISTS (SELECT 1 FROM referenced_rows);
                    """, (task_id, task_id))
            self.conn.commit()
            print("Deleted!" if c.rowcount > 0 else "The record could not be deleted")
        except Exception as e:
            self.conn.rollback()

    def delete_task_tab3(self, task_id):
        c = self.conn.cursor()
        try:
            c.execute('DELETE FROM public."Comments" WHERE "comment_id"=%s', (task_id, ))
            self.conn.commit()
            print("Deleted!" if c.rowcount > 0 else "The record could not be deleted")
        except Exception as e:
            self.conn.rollback()

    def random_add_task_tab1(self, amount):
        c = self.conn.cursor()
        c.execute("""
        DO $$
        DECLARE
        max_user_id INT;
        BEGIN
        SELECT MAX("user_ID") INTO max_user_id FROM public."USER";
        INSERT INTO public."USER" ("user_ID", username, email)
        SELECT
        COALESCE(max_user_id, 0) + generate_series,
        chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int),
        chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || ('@outlook.com')
        FROM generate_series(1, %s);
        END $$;
        """, (amount, ))
        self.conn.commit()

    def random_add_task_tab2(self, amount):
        c = self.conn.cursor()
        c.execute("""
        DO $$
        DECLARE
        max_project_id INT;
        random_user_id INT;
        BEGIN
        SELECT MAX("project_ID") INTO max_project_id FROM public."Projects";    
        SELECT "user_ID" FROM public."USER" ORDER BY random() LIMIT 1 INTO random_user_id;    
        INSERT INTO public."Projects" ("project_ID", "user_ID", "Date_of_publication", "projectname")
        SELECT
        COALESCE(max_project_id, 0) + generate_series,
        random_user_id,
        current_date - (random() * interval '5 years'),
        chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int)
        FROM generate_series(1, %s);
        END $$;""", (amount, ))
        self.conn.commit()

    def random_add_task_tab3(self, amount):
        c = self.conn.cursor()
        c.execute("""
        DO $$
        DECLARE
        max_comment_id INT;
        random_user_id INT;
		random_project_id INT;
        BEGIN
        SELECT MAX("comment_id") INTO max_comment_id FROM public."Comments";    
        SELECT "user_ID" FROM public."USER" ORDER BY random() LIMIT 1 INTO random_user_id;
		SELECT "project_ID" FROM public."Projects" ORDER BY random() LIMIT 1 INTO random_project_id;
        INSERT INTO public."Comments" ("comment_id", "project_id", "user_id", "text" , "date_of_publication")
        SELECT
        COALESCE(max_comment_id, 0) + generate_series,
		random_project_id,
        random_user_id,
		chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
        current_date - (random() * interval '5 years')
        FROM generate_series(1, %s);
        END $$;""", (amount, ))
        self.conn.commit()

    def search_tab1(self, min_user_ID, max_user_ID, username, email):
        start_time = time.time()
        c = self.conn.cursor()
        c.execute("""
        SELECT *
        FROM public."USER"
        WHERE
            "user_ID" BETWEEN %s AND %s
            AND "username" LIKE %s
            AND "email" LIKE %s;
        """, (min_user_ID, max_user_ID, username, email))
        execution_time = (time.time() - start_time) * 1000
        print("Execution time: %.2f ms" % execution_time)
        print(c.fetchall())
    def search_tab2(self, min_project_ID, max_project_ID, min_user_ID, max_user_ID, projectname, start_date, end_date):
        start_time = time.time()
        c = self.conn.cursor()
        c.execute("""SELECT *
        FROM public."Projects"
        WHERE
        "project_ID" BETWEEN %s AND %s
        AND "user_ID" BETWEEN %s AND %s
        AND "projectname" LIKE %s
        AND "Date_of_publication" BETWEEN %s AND %s;""", (min_project_ID, max_project_ID, min_user_ID, max_user_ID, projectname, start_date, end_date))
        execution_time = (time.time() - start_time) * 1000
        print("Execution time: %.2f ms" % execution_time)
        print(c.fetchall())

    def search_tab3(self, min_comment_id, max_comment_id, min_project_ID, max_project_ID, min_user_ID, max_user_ID, text, start_date, end_date):
        start_time = time.time()
        c = self.conn.cursor()
        c.execute("""
        SELECT *
        FROM public."Comments"
        WHERE
        "comment_id" BETWEEN %s AND %s
        AND "project_id" BETWEEN %s AND %s
        AND "user_id" BETWEEN %s AND %s
        AND "text" LIKE %s
        AND "date_of_publication" BETWEEN %s AND %s;
        """, (min_comment_id, max_comment_id, min_project_ID, max_project_ID, min_user_ID, max_user_ID, text, start_date, end_date))
        execution_time = (time.time() - start_time) * 1000
        print("Execution time: %.2f ms" % execution_time)
        print(c.fetchall())