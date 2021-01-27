from psycopg2 import connect, DatabaseError



def pg_connect(params_dic):
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