# 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time 

n=int(input("Enter the  number :"))
for i in range (1,5):
    time.sleep(n)
    print(n)