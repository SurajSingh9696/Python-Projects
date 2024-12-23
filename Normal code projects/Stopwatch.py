import time


sec = int(input("Enter the no. of seconds: "));

for x in range(sec , 0 ,-1):
    second = int(x % 60);
    minute = int((x / 60) % 60);
    hour = int((x / 3600));
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1);


print("Times up!")