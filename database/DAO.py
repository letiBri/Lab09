from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select ID, IATA_CODE, AIRPORT
                    from airports a """

        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(x):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.ORIGIN_AIRPORT_ID as a, f.DESTINATION_AIRPORT_ID as b, avg(f.DISTANCE) as c 
                from flights f 
                group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID 
                having avg(f.DISTANCE) > %s """

        cursor.execute(query, (x, ))

        for row in cursor:
            result.append([row["a"], row["b"], row["c"]])

        cursor.close()
        conn.close()
        return result
