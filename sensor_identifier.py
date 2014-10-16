#!/usr/bin/python

import os

# please add the permissions related to sensors
sensor_permission_dict = dict()

def reverse(apk_loc):
    # please implement
    pass

def get_permission(apk_loc):
    # use aapt to do implement
    pass

def search_for_generic_sensor(source_dir):
    # find the term "android/hardware/SensorManager;->getDefaultSensor", or "android/hardware/SensorEvenetListener"
    # generic sensor is related to SensorEvent
    pass

def search_for_specific_sensor(source_dir):
    # two rules:
    # 1. if we see "android/hardware/SensorManager;->getDefaultSensor", search for the const assigned to the variable in the same method. This sensor type and its mappings to const values can be found on developer's webpage
    # 2. if we see "android/hardware/SensorManager;->registerListener", also search for the const assigned to the variable for listener in the same method. We can map it to the sensor type.

def search_sensor(apk_loc):
    sensors = set()

    # 1. reverse the apk file
    (Manifest_path, reversed_dir) = reverse(apk_loc)

    # 2. check permission
    permissions = get_permission(apk_loc)

    for permission in permissions:
        if permission in sensor_permission_set():
            print "Sensor %s is detected"%sensor_permission_dict[permission]
            sensors.add(sensor_permission_dict[permission])
    
    # 3. check source code
    if search_for_generic_sensor(reversed_dir):
        sensors.add('Generic sensor')

    # 4. besides generic sensor
    sensors = sensor.union(search_for_specific_sensor(reversed_dir))
        
