
# Little Lemon Restaurant

Desinged a simple resturant/booking app using Django.

## Run Locally

Clone the project

```bash
  git clone https://github.com/iamluckycheema/little_lemon.git
```

Go to the project directory

```bash
  cd my-project
```

Create Virtual enviourment
Make sure you have Pyhton and venv installed on you machine.
```bash
  python -m venv venv
```
for windows
```bash
  venv\Scripts\activate
  pip install django
```
move to the project 
```bash
  "cd ...\little_lemon\little_lemon"
```
run
```bash
  python manage.py makemigrations
  pyhton manage.py migrate
  pyhton manage.py runserver
```
for menu add your produts using the 'django admin panel'
```bash
  python manage.py createsuperuser
```
then run server and go to add enties in menu model.
```bash
  172.0.0.1:8000/admin
```
also reservations can be scene there too.

## Screenshots

![Home](https://github.com/iamluckycheema/little_lemon/blob/main/little_lemon/screenshots/home.png)
![About](https://github.com/iamluckycheema/little_lemon/blob/main/little_lemon/screenshots/about.png)
![Menu](https://github.com/iamluckycheema/little_lemon/blob/main/little_lemon/screenshots/menu.png)
![Reservation](https://github.com/iamluckycheema/little_lemon/blob/main/little_lemon/screenshots/reservation.png)
![Menu Item](https://github.com/iamluckycheema/little_lemon/blob/main/little_lemon/screenshots/menu_item.png)


## Features

- Booking online
- Menu & Menu details
- Home Page/Landing Page


## 🚀 About Me
I'm a full stack developer...

