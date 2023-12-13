import os
import pandas as pd
import calendar
import datetime as dt
import requests

URL = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime={start}&endtime={end}&minmagnitude=2.0&orderby=time"

for yr in range(2000, 2019):
    for m in range(1, 13):
        if os.path.isfile('{yr}_{m}.csv'.format(yr=yr, m=m)):
            continue
        _, ed = calendar.monthrange(yr, m)
        start = dt.datetime(yr, m, 1)
        end = dt.datetime(yr, m, ed, 23, 59, 59)
        with open('{yr}_{m}.csv'.format(yr=yr, m=m), 'w', encoding='utf-8') as f:
            f.write(requests.get(URL.format(start=start, end=end), verify=False).content.decode('utf-8'))

dfs = []
for i in range(2000, 2019):
    for m in range(1, 13):
        filename = f'D:/workspace_python/exemplo_holoviz/examples/data/csv/{i}_{m}.csv'

        if not os.path.isfile(filename):
            continue
        
        print(f'Filename: {filename}')
        df = pd.read_csv(filename, dtype={'nst': 'float64'})
        dfs.append(df)
df = pd.concat(dfs, sort=True)
df.to_parquet('D:/workspace_python/exemplo_holoviz/examples/data/earthquakes.parq', 'fastparquet')

# Reprojected, cleaned and gzip (not snappy)


# import numpy as np
# import pandas as pd
# from holoviews.util.transform import lon_lat_to_easting_northing

# df = pd.read_parquet('../data/earthquakes.parq')
# #df.time = df.time.astype('datetime64[ns]')

# cleaned_df = df.copy()
# cleaned_df['mag'] = df.mag.where(df.mag > 0)
# cleaned_df = cleaned_df.reset_index()

# x, y = lon_lat_to_easting_northing(cleaned_df.longitude, cleaned_df.latitude)
# cleaned_projected = cleaned_df.join([pd.DataFrame({'easting': x}), pd.DataFrame({'northing': y})])

# cleaned_projected.to_parquet('../data/earthquakes-projected.parq', 'fastparquet', compression='gzip', file_scheme='simple')
