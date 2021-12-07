# Redi-url

## Description 
This tool forces to redirect some domains for a given url. If you give like this input https://google.com , the tool will append the payloads and try to check whether the URL is redirected or not?

## Installation


```
git clone https://github.com/kavisurya/Redi-url
cd Redi-url
pip install requests
pip install time
python3 url_redirect_check.py

```

## Usage - 1

If you're going to add some vulnerable parameters, you can give yes

For example:

your URL like: https://www.google.com/pages/
yes --> keyword usage for append the vulnerable parameters. https://www.google.com/pages/?vulnparams=payloads or like https://www.google.com/pages?page=https://bing.com


```
python3 url_redirect_check.py

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


    
Do you wanna add param ??? like url='payload' RECOMMENDED (yes/no): yes
Enter Your URL (Ex: https://google.com/profileview) : https://www.guvi.in/courses
Enter your Time Delay (Default value is 0) : 0
Please wait...Whether the URL is vulnerable or not. If The URL is vulnerable its appear on the OUTPUT.TXT file

```
## Usage - 2

if you don't want to add vulnerable parameters, you should give no.

For example:

your URL like: https://www.google.com/payloads
no --> keyword usage for it won't append the vulnerable parameters. https://www.google.com/pages/payloads or like https://www.google.com/payloads

```
python3 url_redirect_check.py

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


    
Do you wanna add param ??? like url='payload' RECOMMENDED (yes/no): no
Enter Your URL (Ex: https://google.com/profileview) : https://www.guvi.in/
Enter your Time Delay (Default value is 0) : 0
Please wait...Whether the URL is vulnerable or not. If The URL is vulnerable its appear on the OUTPUT.TXT file

```


## Output

The output will be stored in the output file. Also, it will print the vulnerable URL with the payload.
