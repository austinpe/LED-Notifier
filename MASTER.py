# Master LED Notifier 
# v1.0
# By Austin Philipp-Edmonds

import os, time, serial

#Connects to Arduino
ser = serial.Serial('COM4', 9600)
time.sleep(5)
print "Connected to Arduino"

#Plugin Lists
#set the destination of plugin folder below
plugin_list = os.listdir("C:\\users\\austin\\desktop\\plugins")
plugin_list_len = len(plugin_list)
module_names = []

#Pulls all the plugins found
for plugin in plugin_list:
    if 'MASTER' in plugin:
        continue
    plugin = plugin.split('.')
    module_names.append(plugin[0])
    print str(plugin) + " was loaded"
    
plugins = []

#Pulls the functions from the plugins
for module_name in module_names:
    module = __import__(module_name)
    for function in dir(module):
        if '_refresh' in function:
            f = getattr(module, function)
            plugins.append(f)

#Loop that runs all the functions            
while True:
    for plugin_functions in plugins:
        result = plugin_functions()
        if result:
            print result
            ser.write(result)
    time.sleep(4)
    

    
