This python program will create a 3x3 matrix of jpeg photos with a location label for each.
To use it, edit the grid.html file to change the Conference name  eg: Leggo Expo July 17 2017 in Portland, Oregon
If needed edit the locations: eg: change Room 1 to Area 1 etc.
exit the grid.html edit session.
copy 9 jpg imgs into the views directory and name them imgx.jpg where x= 1,2,...9
Determine your server ip address by using: ifconfig | grep inet perhaps: 192.168.1.7
Edit the server.py file and:
    modify the root parameter to point to your paths.(in a terminal navigate to your project and do a 'pwd" in the directory with grid.html and in the views dir.) 
...        return static_file('grid.html', root= '<yourPath>')
...        return static_file(img, root='<yourPath>/views')

    modify the following line to have your ip address:
                run(host='<yourIpAddress>',port=8080,debug=True)   
Start the webserver by entering python3 server.py in the project root directory ( where server.py exists).
On any connected device with a browser, enter http://<server ip address>:8080/display 
You should see the 9 imgs displayed with their locations.