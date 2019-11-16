import time
import cv2
minutes=0
hours=0
# while True:
#
#     prev=time.time()
#
#     cv2.waitKey(1000)
#     last=time.time()
#
#     seconds=last-prev

seconds=259267
def sec_to_year_days_hours_minutes_sec(seconds):
    print("sec = ",seconds)
    minutes = seconds / 60
    hours=minutes/60
    days = hours / 24
    years = int(days / 365.25)
    days=int(days%365.25)
    hours=int(hours%24)
    minutes=int(minutes%60)
    seconds=int(seconds%60)


    # hours=minutes//60


    print("y:",years,"d:",days,"h:",hours,"m:",minutes,"s:",seconds)