# table_creator_wine.py
import psycopg2

def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS wine_data (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP,
        alcohol FLOAT,
        malic_acid FLOAT,
        ash FLOAT,
        alcalinity_of_ash FLOAT,
        magnesium FLOAT,
        total_phenols FLOAT,
        flavanoids FLOAT,
        nonflavanoid_phenols FLOAT,
        proanthocyanins FLOAT,
        color_intensity FLOAT,
        hue FLOAT,
        od_of_diluted_wines FLOAT,
        proline FLOAT,
        target INT
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,
        database="mydatabase",
    )
    create_table(db_connect)
