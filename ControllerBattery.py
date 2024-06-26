from XInput import *
from playsound import playsound
from win10toast import ToastNotifier
import time
toast = ToastNotifier()

events = get_events()
connected=get_connected()
if connected[0]==True:
    status="Connected"
else :
    status="Disconnected"

toast.show_toast("Controller Battery App","App is running in background. "+"\n"+"Device Connection  Status : "+ status,duration = 8,icon_path = r"C:\Users\Panos\Desktop\charge.ico",threaded = True)
time.sleep(5)
while 1:
    events = get_events()
    connected=get_connected()
    if connected[0]== True :  
        events = get_events()
        for event in events:
            print (event)
            BatteryInfo=get_battery_information(event.user_index)
            print (BatteryInfo)
            BatteryLevel=BatteryInfo[1]
        if BatteryLevel=="LOW" :
            playsound(r"PathToSound")
            toast.show_toast("Low Battery","Controller Battery is almost empty.",duration = 8,icon_path = r"PathToIcon",threaded = True)
            time.sleep(180)
            continue
    time.sleep(60)
