# 🕵️‍♂️ 6. Website Status Checker

# Goal: Take a list of URLs and check which websites are online or offline.
# Concepts: requests, loops, exception handling
# Example:
# Input list:

# https://google.com  
# https://somerandomwebsite123.com


# Output:
# ✅ google.com is Online
# ❌ somerandomwebsite123.com is Offline

import requests
urls_list = []
endinput = 0
while endinput != 2:
    userURLs = input("Please enter the URLs:\nexample https://google.com\nhttps://somerandomwebsite123.com\n>>")#collecting url
    urls_list.append(userURLs)#Storing url(s) in a list
    data_valid = False#data validation
    while data_valid == False:
        endinput = input("Do you want to enter more URLS?\n1.yes\n2.no\n")
        try:#in the try block
            endinput = int(endinput)#converting to the integers
            if (endinput < 1 or endinput > 2):#checking if the input is out of the range f options
                print("enter a valid option.")#display error message
            else:
                data_valid = True#break out of the inner loop
        except:
            print("Alphabets are not allowed.")#error message if the conversion to integer fails

for url in urls_list:
    R = requests.get(url)#sending the resquest to the URL
    if(R.status_code == 200):#if status code is 200(which is the OK response)
        print(f"{url} is Online✅")#Run this if response is OK
    elif(R.status_code == 403):
        print(f"{url} is Forbidden❌")#Run this if URL is forbidden
    else:
        print(f"{url} is Offline❌")#Run this if URL is Offline



