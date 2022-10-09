# REST-Service

This project implements a REST service for a DNS server using the Django Rest
Framework. I will provide a detailed explanation of how the code works along with the results shown on the website.

To run it, clone the repository to your local computer. Open command line and go to the directory with manage.py file. Run the command, python manage.py runserver. You'll be provided with a link to the server, follow the link and continue the steps below.

The URL http://127.0.0.1:8000/api takes us to our django application with the home page as shown below

![Screenshot 2022-10-09 013741](https://user-images.githubusercontent.com/61738363/194726863-1d5253be-5a08-4fcb-a0a3-a30e5420022f.jpg)

# Updating the record
Follow the url pattern http://127.0.0.1:8000/baseCreate to update the DNS record,
which takes domain and IP address as a request body and saves it in a database. The saveD domain names and IP addresses are as shown below.

![Screenshot 2022-10-09 014625](https://user-images.githubusercontent.com/61738363/194726999-ccc88f3f-6802-4d0b-a726-053308f652b6.jpg)
![Screenshot 2022-10-09 014826](https://user-images.githubusercontent.com/61738363/194727002-7367e2ff-30a5-4214-b6a2-788c8c13748c.jpg)

# IP Lookup
Follow the url pattern http://127.0.0.1:8000/baseLookup to search for the IP address given the domain name. The search result based on the IP address is shown below.

![Screenshot 2022-10-09 014931](https://user-images.githubusercontent.com/61738363/194727099-214607bf-660a-4fc9-acbb-9042f2c370fd.jpg)
![Screenshot 2022-10-09 015006](https://user-images.githubusercontent.com/61738363/194727109-94d07cf8-d188-4bac-8d47-14d547e197ea.jpg)

The API works fine with no errors!
