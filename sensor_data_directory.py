"""
DHT22 provides :

1. temp
2.humidity
#static/meta data
place
"""

sensor_data = \
{      #\ -----to avoid new line
    "temp" : 0,
    "humidity" : 0,
    "place" : "pune"
}
print(sensor_data)

sensor_data["temp"] = 27
sensor_data["humidity"] = 96
print(sensor_data)

#access values using get method
print(sensor_data.get('temp'))
print(sensor_data.get('pressure',"pressure sensor is not available"))
print(sensor_data)

#retrive the key
for sensors in sensor_data:
    print(sensors)

#retrive key and value also
for sensors in sensor_data:
    print("{} {}".format(sensors,sensor_data[sensors]))
