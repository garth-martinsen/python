This python3 program will create a 3x3 matrix of jpeg photos with a location label for each.
To use it, 
----------------------------
 Edit the grid.html file 

  change the Conference Title  eg: Leggo Expo July 17 2017 in Portland, Or

  edit the locations: eg: change Room 1 to Area 1 etc.

exit the grid.html edit session.
-------------------------------
copy 9 jpg imgs into the views directory and name them imgx.jpg where x= 1,2,...9
------------------------------
In a terminal 

Determine your server ip address by using: ifconfig | grep inet (result is like: 192.168.1.7)

Determine the absolute path to your project root. Navigate to the grid.html file and type pwd (result is like: /Users/garth/Programming/Python/ritzman )

Edit the server.py file and modify the following lines (approx lines 7,8) Note: the single quote marks are required. 

...             rootDir='yourPath'                
                ipAddress ='serverIpAddress'

Exit the server.py file  
----------------------------
Start the webserver by entering the following command in the rootDir.( where the server.py file is located)

                    python3 server.py 

On any connected device with a browser, enter http://serverIpAddress:8080/display 

You should see the conference Title,  9 imgs displayed with their captions.
