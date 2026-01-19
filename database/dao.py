from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_anno():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
                SELECT DISTINCT s_datetime as data
                FROM sighting
                WHERE '1910-01-01 00:00:00' <= s_datetime
                and s_datetime <= '2014-12-31 23:59:59'
                ORDER BY s_datetime ASC
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row['data'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_forma():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
                SELECT DISTINCT shape as forma
                FROM sighting
                ORDER BY shape ASC
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row['forma'])

        cursor.close()
        conn.close()
        return result