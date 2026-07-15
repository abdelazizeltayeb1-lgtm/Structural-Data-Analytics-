import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sensor_records = [
    ("S1", "2025-04-28 10:00", 35.2, 12.1, 0.002),
    ("S2", "2025-04-28 10:00", 36.5, 14.0, 0.003),
    ("S1", "2025-04-28 11:00", 36.1, 12.5, 0.0021),
    ("S3", "2025-04-28 10:00", 34.0, 11.8, 0.0025),
    ("S2", "2025-04-28 11:00", 37.2, 14.3, 0.0031),
    ("S1", "2025-04-28 12:00", 37.0, 13.0, 0.0022),
]

# numpy array
my_data = np.array(sensor_records, dtype=[('id','U5'),('time','U20'),('temp','f4'),('stress','f4'),('disp','f4')])

sensors = np.unique(my_data['id'])

print("numpy part")
for x in sensors:
    one_sensor = my_data[my_data['id'] == x]
    avg_stress = np.mean(one_sensor['stress'])
    print(x, "avg stress:", avg_stress)

# find highest per sensor
high_one = ""
high_num = 0
for x in sensors:
    one_sensor = my_data[my_data['id'] == x]
    avg_s = np.mean(one_sensor['stress'])
    if avg_s > high_num:
        high_num = avg_s
        high_one = x
print("highest stress sensor:", high_one)

# temps above 36
hot_readings = my_data[my_data['temp'] > 36]
print("readings above 36:", len(hot_readings))

print("\npandas part")

# dataframe
df = pd.DataFrame(sensor_records, columns=['id','time','temp','stress','displacement'])
df['time'] = pd.to_datetime(df['time'])

# averages per sensor
avg_table = df.groupby('id')[['temp','stress','displacement']].mean()
print(avg_table)

# hottest
temp_avg = df.groupby('id')['temp'].mean()
hottest_one = temp_avg.idxmax()
print("hottest sensor:", hottest_one)

# visualize temp over time
plt.figure()
for sid in df['id'].unique():
    small = df[df['id'] == sid]
    plt.plot(small['time'], small['temp'], marker='o', label=sid)

plt.title("temperature over time")
plt.xlabel("time")
plt.ylabel("temp (C)")
plt.legend()
plt.grid(True)
plt.show()

# visualize stress vs displacement
plt.figure()
plt.scatter(df['stress'], df['displacement'])
plt.title("stress vs displacement")
plt.xlabel("stress")
plt.ylabel("displacement")
plt.show()