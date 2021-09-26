# Create .env with MY_IP as a variable

>MY_IP=172.18.0.172 

# Create venv and install requirements

for win10
>python -m venv c:\my_path\venv
>.\venv\Scripts\activate
> pip install -r requirements.txt
(I didn't test it)

---

for ubuntu
cd to base project and run:

>python -m venv venv
>source venv/bin/activate
> pip install -r requirements.txt

# To run the project

1. cd to root base in this case managementAPP/

2. then run
>python3 manage.py runserver 9000

PS. I used 9000 with another intern since the default one was in use

# Database:

for this project I used sqlite to avoid configuration and all that pain.
I included the database with the project


# API:

localhost:9000/swagger/

localhost:9000/api/

