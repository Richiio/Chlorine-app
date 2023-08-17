from django.conf import settings

import time
from datetime import datetime as dt
import pandas as pd
from influxdb_client import InfluxDBClient, Point

DATA_DIR = "sensor_app/UCRArchive_2018/ChlorineConcentration/"


def load_data(filename):
    df = pd.read_csv(DATA_DIR + filename, sep='\t', header=None)
    df.drop(0, axis=1, inplace=True)
    return df


def write_to_influxdb(data):
    url = f"http://{settings.INFLUXDB_HOST}:{settings.INFLUXDB_PORT}"

    with InfluxDBClient(url=url, token=settings.INFLUXDB_TOKEN, org=settings.INFLUXDB_ORGANISATION) as _client:
        with _client.write_api() as _write_client:
            _write_client.write(settings.INFLUXDB_BUCKET, settings.INFLUXDB_ORGANISATION,
                                [Point("chlorine_concentration").tag("reading", "average").\
                                field("concentration", data["average_concentration"]).time(dt.utcnow()),
                                 Point("chlorine_concentration").tag("reading", "minimum"). \
                                field("concentration", data["min_concentration"]).time(dt.utcnow()),
                                 Point("chlorine_concentration").tag("reading", "maximum"). \
                                field("concentration", data["max_concentration"]).time(dt.utcnow())])


def write_data():
    cc_df = load_data("ChlorineConcentration_TRAIN.tsv")
    for row_index in range(cc_df.shape[0]):
        row_data = {
            "average_concentration": cc_df.iloc[row_index, :].mean(),
            "min_concentration": cc_df.iloc[row_index, :].min(),
            "max_concentration": cc_df.iloc[row_index, :].max(),
        }
        # write to DB.
        write_to_influxdb(row_data)
        time.sleep(1)

        if row_index % 50 == 0:
            print(f"[{dt.utcnow():%Y-%m-%d %H:%M:%S%z}] Datapoint {row_index} saved.")
