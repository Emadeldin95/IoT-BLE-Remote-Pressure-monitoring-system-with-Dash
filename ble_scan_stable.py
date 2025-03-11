"""
Simple BLE forever-scan example, that prints all the detected
LE advertisement packets, and prints a colored diff of data on data changes.
"""
import sys
import string
import bluetooth._bluetooth as bluez


from bluetooth_utils import (toggle_device,
                             enable_le_scan, parse_le_advertising_events,
                             disable_le_scan, raw_packet_to_str)
import binascii
import struct
import pandas as pd
import time
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

csv_path='/home/mazen/PycharmProjects/BLE/sensors.csv'
dev_id = 0  # the bluetooth device is hci0
database_con='sqlite:////home/mazen/PycharmProjects/BLE/sensors_database.db'
now = datetime.now()
current_date = now.strftime("%Y-%m-%d %H:%M:%S")
try:
    #pd.read_sql_table('sensors_table',con=database_con)
    pd.read_csv(csv_path)
    sensors_data={'Date':[current_date],'Shaping':[0],'Upper Left':[0],'Upper Right':[0],'Down Left':[0],'Down Right':[0],
                       'Sector Left':[0],'Sector Right':[0],'Main':[0]}

    sensors_df=pd.DataFrame(sensors_data)
    sensors_df = sensors_df.astype({"Shaping": 'float64', "Upper Left": 'float64','Upper Right':'float64','Down Left':'float64',
                                  'Down Right':'float64','Sector Left':'float64','Sector Right':'float64','Main':'float64',
                                  'Date':'datetime64'})

    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
    sensors_df.to_csv(csv_path,index=False)


except:
    sensors_data={'Date':[current_date],'Shaping':[0],'Upper Left':[0],'Upper Right':[0],'Down Left':[0],'Down Right':[0],
                       'Sector Left':[0],'Sector Right':[0],'Main':[0]}

    sensors_df=pd.DataFrame(sensors_data)
    sensors_df = sensors_df.astype({"Shaping": 'float64', "Upper Left": 'float64','Upper Right':'float64','Down Left':'float64',
                                  'Down Right':'float64','Sector Left':'float64','Sector Right':'float64','Main':'float64',
                                  'Date':'datetime64'})

    #sensors_df.to_sql('sensors_table',con=database_con,index=False,if_exists='replace')
    sensors_df.to_csv(csv_path,index=False)


toggle_device(dev_id, True)

try:
    sock = bluez.hci_open_dev(dev_id)
    try:
        disable_le_scan(sock)
    except:
        pass
    
except:
    print("Cannot open bluetooth device %i" % dev_id)
    raise


enable_le_scan(sock, filter_duplicates=False)

time_elabsed=0
try:
    prev_data = None


    def le_advertise_packet_handler(mac, adv_type, data, rssi):

        global prev_data,time_elabsed
        start = time.time()
        data_str = raw_packet_to_str(data)
        data_wo_rssi = (mac, data_str)

        if (adv_type == 2):
            #print("BLE packet: %s %02x %s %d" % (mac, adv_type, data_str, rssi))
            IDval=data_str[30:36]
            print('ID',IDval)
            #print("ID = " + IDval)
            if (rssi == 0):
                print('pressing')
                pass
            else:
                print('no pressure input')
                pass

            rawTemp = data_str[44:52]
            #print("temprature raw data = " + rawPress)
            value = rawTemp
            # x = value[4:8] + value[0:4]
            # print(x)
            packed_data = binascii.unhexlify(value)
            s = struct.Struct('I')
            unpacked_data = s.unpack(packed_data)
            temprature= unpacked_data[0] / 100
            #print('temprature Unpacked Values (Celsius):', temprature)
            #print('pressure Unpacked Values :' + str(pressure) + ' C')

            # press = int(data_str[48:56], 16)
            # print(press/100000)
            rawPress = data_str[36:44]
            #print("pressure raw data = " + rawPress)
            value = rawPress
            # value = '26590000'
            # x = value[4:8] + value[0:4]
            # print(x)
            packed_data = binascii.unhexlify(value)
            s = struct.Struct('I')
            unpacked_data = s.unpack(packed_data)
            pressure = unpacked_data[0] / 100000
            #print('pressure Unpacked Values :' + str(pressure) + ' bar')
            #'Down Right':'10a053','Sector Left':'409d7c'
            sensors_ids={'Shaping':'10da84','Upper Left':'20d7c8','Upper Right':'40bd2e','Down Left':'309f77',
                         'Down Right':'10a053','Sector Left':'409d7c','Main':'4077cc','Sector Right':'3077ad'}

            # final = data_str[0:1] | data[1:2] << 8 | data_str[3:4] << 16 | data_str[5:6] << 24'''
       #209f3b
       #  209c7e
            if (IDval == sensors_ids['Shaping']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Shaping'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')

                print('Shaping Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif (IDval == sensors_ids['Upper Left']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Upper Left'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')

                print('Upper Left Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif(IDval == sensors_ids['Upper Right']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Upper Right'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')

                print('Upper Right Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif(IDval == sensors_ids['Down Left']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings = sensors_df.tail(1)
                    df_last_readings['Down Left'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0] = current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)

                except:
                    print('database busy')

                print('Down Left Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif (IDval == sensors_ids['Down Right']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Down Right'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')


                print('Down Right Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif (IDval == sensors_ids['Sector Left']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Sector Left'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')

                print('Sector Left Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif (IDval == sensors_ids['Sector Right']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Sector Right'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')

                print('Sector Right Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            elif (IDval == sensors_ids['Main']):
                try:
                    #sensors_df=pd.read_sql_table('sensors_table', con=database_con)
                    sensors_df=pd.read_csv(csv_path)
                    df_last_readings=sensors_df.tail(1)
                    df_last_readings['Main'].values[0]=round(pressure,3)
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
                    df_last_readings['Date'].values[0]=current_date
                    sensors_df=sensors_df.append(df_last_readings,ignore_index=True)
                    #sensors_df.to_sql('sensors_table', con=database_con, index=False, if_exists='replace')
                    sensors_df.to_csv(csv_path, index=False)
                except:
                    print('database busy')

                print('Main Pressure = '+str(round(pressure,3))+' bar')
                print('send data')
            end = time.time()
            func_time=end-start
            time_elabsed+=func_time
            #print('time_elabsed',  time_elabsed)
        '''if prev_data is not None:
            if data_wo_rssi != prev_data:
                # color differences with previous packet data
                sys.stdout.write(' ' * 35 + 'data_diff=')
                for c1, c2 in zip(data_str, prev_data[1]):
                    if c1 != c2:
                        sys.stdout.write('\033[0;33m' + c1 + '\033[m')
                    else:
                        sys.stdout.write(c1)
                sys.stdout.write('\n')

        prev_data = data_wo_rssi'''


    # Blocking call (the given handler will be called each time a new LE
    # advertisement packet is detected)
    if __name__ == "__main__":
        parse_le_advertising_events(sock,
                                    handler=le_advertise_packet_handler,
                                    debug=False)


except KeyboardInterrupt:
    disable_le_scan(sock)
    pass
