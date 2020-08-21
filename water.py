import time
from plyer import notification

if __name__=="__main__":
    notification.notify(
    title="--Please Drink Water--",
    message="You have to intake 4 lts of water a day :)",
    #app_icon="C:\Users\unnati sharma\Desktop\python3\project\ico\water.ico",
    timeout=5
    )
    time.sleep(60)
