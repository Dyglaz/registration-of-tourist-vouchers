import pymysql
from data.auth_data import *


class Database:
    @staticmethod
    def get_connection() -> pymysql.Connection:
        try:
            connect = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                database=database,
                password=password,
                cursorclass=pymysql.cursors.DictCursor
            )
            return connect
        except Exception as ex:
            print(ex)

    def get_table(self, table: str) -> list[dict]:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                query = f"SELECT * FROM `{table}`"
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
        except Exception as ex:
            print(ex)
        finally:
            con.close()

    def insert_data(self, table: str, data: str, keys: str) -> str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                sql = f"INSERT INTO {table} {keys} VALUES {data}"
                cursor.execute(sql)
            con.commit()
            return "Successful insertion!"
        except Exception as ex:
            return f"Something went wrong! {ex}"
        finally:
            con.close()

    def delete_data(self, table: str, key: str, value: int) -> str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                sql = f"DELETE FROM {table} WHERE {key}={value}"
                cursor.execute(sql)
            con.commit()
            return "Successful delete!"
        except Exception as ex:
            return f"Something went wrong! {ex}"
        finally:
            con.close()

    def call_proc_get_employees_by_position(self, title: str) -> list or str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                cursor.execute(
                    f'CALL get_employees_by_position("{title}")'
                )
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)
            return f"Something went wrong! {ex}"
        finally:
            con.close()

    def call_proc_get_customer_service_information(self) -> list or str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                cursor.execute(
                    "CALL get_customer_service_information()"
                )
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)
            return f"Something went wrong! {ex}"
        finally:
            con.close()

    def call_proc_get_min_max_tour_prices(self) -> list or str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                cursor.execute(
                    "CALL get_min_max_tour_prices()"
                )
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)
            return f"Something went wrong! {ex}"
        finally:
            con.close()

    def call_func_get_the_average_cost_of_the_tour(self) -> list or str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                cursor.execute(
                    "SELECT get_the_average_cost_of_the_tour()"
                )
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)
            return f"Something went wrong! {ex}"
        finally:
            con.close()

    def call_func_get_tourist_vouchers_by_tour_name(self, tour_name: str) -> list or str:
        try:
            con = self.get_connection()
            with con.cursor() as cursor:
                cursor.execute(
                    f'SELECT get_tourist_vouchers_by_tour_name("{tour_name}")'
                )
                res = cursor.fetchall()
                return res
        except Exception as ex:
            print(ex)
            return f"Something went wrong! {ex}"
        finally:
            con.close()
