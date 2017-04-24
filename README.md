This python program will create a 3x3 matrix of jpeg photos with a location label for each.
To use it, edit the grid.html file to change the Conference  eg: Leggo Expo July 17 2017 in Portland, Or
If needed edit the locations: eg: change Room 1 to Area 1 etc.
exit the grid.html edit session.
copy 9 jpg imgs into the views directory and name them imgx.jpg where x= 1,2,...9
Determine your server ip address by using: ifconfig | grep inet perhaps: 192.168.1.7
Edit the server.py file and modify the following line to have your ip address:
                run(host='192.168.1.10',port=8080,debug=True)   
Start the webserver by entering python3 server.py.
On any connected device with a browser, enter http://<server ip address>:8080/display 
You should see the 9 imgs displayed with their locations.
