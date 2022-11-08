## Questionnare System
## Setup Project

Clone the project using following command
```
git clone https://github.com/khunshan97/arbisoft_task2
```

Create Virtual Environment
```
python -m venv venv
```

Activate Environment
```
source venv/bin/activate
```

Install Required Dependencies

```
pip install -r requirements.txt
```

Run following command to migrate django models to database
```
python manage.py makemigrations
python manage.py migrate
```

Run following commands to populate questions from json file to database
```
python manage.py runscript load_questionnare
```

Run following command to run server
```
python manage.py runserver
```