import requests
import time
# Declaring variables
param_array = ["view","out","url","next","redirect","cgi-bin/redirect.cgi","login","logout","page"]
# file systems
payloads = open("url_payloads.txt","r")
payloads1 = open("url_payloads.txt","r")
output = open("output_url_redirect.txt","a")
# status code variables
statuscode_200 = "200"
statuscode_300 = "300"
statuscode_400 = "400"
statuscode_500 = "500"

count = 0
read_payload_split = payloads.read().split("\n")

# Count the umber of lines
for i in read_payload_split:
    count = count + 1
# print(count)

print(
    """
                                               _____                        
                                      /    /                        
 __  __   ___                        /    /                         
|  |/  `.'   `.                     /    /                          
|   .-.  .-.   '.-,.--. .-,.--.    /    /            .-''` ''-.     
|  |  |  |  |  ||  .-. ||  .-. |  /    /  __       .'          '.   
|  |  |  |  |  || |  | || |  | | /    /  |  |     /              `  
|  |  |  |  |  || |  | || |  | |/    '   |  |    '                ' 
|  |  |  |  |  || |  '- | |  '-/    '----|  |---.|         .-.    | 
|__|  |__|  |__|| |     | |   /          |  |   |.        |   |   . 
                | |     | |   '----------|  |---' .       '._.'  /  
                |_|     |_|              |  |      '._         .'   
                                        /____\        '-....-'`     


    """
)


check = input("Do you wanna add param ??? like url='payload' RECOMMENDED (yes/no): ")

if "yes" == check:
    url = input("Enter Your URL (Ex: https://google.com/profileview) : ")
    user_time = input("Enter your Time Delay (Default value is 0) : ")
    print("Please wait...Whether the URL is vulnerable or not. If The URL is vulnerable its appear on the OUTPUT.TXT file")
    for p in param_array:
        # print(url+"?"+p+"="+"paloads")
        inloop = 0
        for x in range(count):
            time.sleep(int(user_time))
            # print(payloads1.readline()
            try:
                req = requests.get(url +"?"+p+"="+payloads1.readline())
                print(inloop,"=>",req.status_code)
                # print("S.no", str(x), url +"?"+p+"="+payloads1.readline()+ " \t  --->   " + str(req.status_code))
            except KeyboardInterrupt:
                print("Good bye....")
                break
            except requests.exceptions.RequestException:
                print("Connection refused")
            except Exception as e:
                print(e)
                break

            finally:
                inloop = inloop + 1
                if count == inloop:
                    print("bye Meet soon")
                    payloads1.seek(0)
                    continue
                if str(req.status_code)[0:1] == statuscode_300[0:1]:
                    print("300 SERIES FOUND !!!\n [+] Vulnerable URL Found", url +"?"+p+"="+payloads1.readline())
                    output.write(url +"?"+p+"="+payloads1.readline())

                else:
                    pass

elif "no" == check:
    url = input("Enter Your URL (Ex: https://google.com/) : ")
    user_time = input("Enter your Time Delay (Default value is 0) : ")
    inloop = 0
    for x in range(count):
        time.sleep(int(user_time))
        # print(payloads1.readline()
        try:
            req = requests.get(url + payloads1.readline())
            print("S.no", str(x), url + payloads1.readline() + " \t --->  " + str(req.status_code))
        except KeyboardInterrupt:
            print("Good bye....")
            break
        except requests.exceptions.RequestException:
            print("Connection refused")
        except Exception as e:
            print(e)
            break

        finally:
            inloop = inloop + 1
            if count == inloop:
                print("bye")
                break
            if str(req.status_code)[0:1] == statuscode_300[0:1]:
                print("300 SERIES FOUND !!!\n [+] Vulnerable URL Found", url + payloads1.readline())
                output.write(url + payloads1.readline())

            else:
                pass

else:
    print("please check your option and try again ")
    exit()



