# data_insertion_wine.py
import pandas as pd
import psycopg2
from sklearn.datasets import load_wine


def get_data():
    wine = load_wine(as_frame=True)
    X, y = wine.data, wine.target
    df = pd.concat([X, y], axis="columns")
    
    rename_rule = {
        "alcohol": "alcohol",
        "malic_acid": "malic_acid",
        "ash": "ash",
        "alcalinity_of_ash": "alcalinity_of_ash",
        "magnesium": "magnesium",
        "total_phenols": "total_phenols",
        "flavanoids": "flavanoids",
        "nonflavanoid_phenols": "nonflavanoid_phenols",
        "proanthocyanins": "proanthocyanins",
        "color_intensity": "color_intensity",
        "hue": "hue",
        "od280/od315_of_diluted_wines": "od_of_diluted_wines",
        "proline": "proline"
    }
    df = df.rename(columns=rename_rule)
    return df


def insert_data(db_connect, data):
    insert_row_query = f"""
    INSERT INTO wine_data
        (timestamp, alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids,
         nonflavanoid_phenols, proanthocyanins, color_intensity, hue, od_of_diluted_wines, proline, target)
    VALUES (
            NOW(),
            {data.alcohol},
            {data.malic_acid},
            {data.ash},
            {data.alcalinity_of_ash},
            {data.magnesium},
            {data.total_phenols},
            {data.flavanoids},
            {data.nonflavanoid_phenols},
            {data.proanthocyanins},
            {data.color_intensity},
            {data.hue},
            {data.od_of_diluted_wines},
            {data.proline},
            {data.target}
    );"""
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()


if __name__ == "__main__":
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,
        database="mydatabase",
    )
    df = get_data()
    insert_data(db_connect, df.sample(1).squeeze())
