<img src="https://raw.githubusercontent.com/duronald/NetDiscover/main/staticNetDiscover/images/favicon.ico" alt="drawing" width="200"/>


# NetDiscover Production Version

**NetDiscover**, a network utility application, allows users to create and visualize their network through a topological map layout. NetDiscover is a user-friendly, affordable, low-maintenance network mapping tool that small companies and enterprises employ to monitor their networks. NetDiscover is geared toward assisting small businesses which are unable to monitor their networks effectively. NetDiscover provides a simple user interface where clients effectively and efficiently check the health of their network with local network topology construction, modification, and inspection. NetDiscover has an updated, modern user interface design.


## NetDiscover Live

NetDiscover is viewable and usable live here! 
[NetDiscover Live](https://team14netdiscover.ronalddu.me/)

## Creators

Team 14 [Internet Explorers]: Gavin Claire, Ronald Du, Carlos Dye, and Chad Saltzman 
Instructors: Devrin Lee and Dr. David Feil-Seifer  
External Advisors: Dr. Engin Arslan (High-Performance Computing Researcher) and Dr. Shamik Sengupta (Cybersecurity Center Executive Director)  
This project was created for CS 425 and CS 426 at the University of Nevada, Reno in Fall 2021 and Spring 2022.  
Feel free to contact any of us on LinkedIn for more infomation.  
This version of NetDiscover lacks certain functionality and the locally ran version should be ran for all functions.

[NetDiscover Local Version](https://github.com/Chad-Saltzman/Network_Topology_Mapper)
[NetDiscover Website](https://ronalddu.wixsite.com/netdiscover)


## Setup
>These setup directions are general guidelines and should generally be followed to setup a hosted publicly accessible version of NetDiscover.

1. Set up Ubuntu Server accessible from the internet with HTTPS certificates and a domain.
2. Ensure Apache is set up correctly. See example Apache configurations. [Removed for security reasons.] mod-wsgi should be installed.
3. Setup and create a python virtual enviorment inside of the NetDiscover Folder. 
4. Install all requirements after activating the virtual enviorment including django.
5. Configure settings.py in django manager to ensure that the allowed hosts match the domain, and ensure that the secret key is still secret.
6. Reboot apache and hope it works. 





# Locally Ran NetDiscover Notes
>Developer Notes: 
> - Make sure the virtual environment is running before executing commands.
>    - Run ". env/Scripts/activate" to start the virtual environment
>
>- While inside the Network_Topology_Mapper-django-interface folder
>- Run "python manage.py runserver" to run program
>- On web browser: http://127.0.0.1:8000/
