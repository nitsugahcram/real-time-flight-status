from psycopg2 import connect, DatabaseError


def postgresql_connect(params_dic: dict):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = connect(**params_dic)
        print("Connection successful")
    except (Exception, DatabaseError) as error:
        print("Check Params ", params_dic)
        print(error)
    return conn


def postgresql_fetch_data(conn: connect, select_query: str):
    """Fetch Data from postgress"""
    tupples = []
    try:
        cursor = conn.cursor()
        cursor.execute(select_query)
        tupples = cursor.fetchall()
        cursor.close()
    except (Exception, DatabaseError) as error:
        print("Error: %s" % error)
    return tupples
