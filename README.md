# Pulsevote: An online academic voting system

An undergraduate collaborative project.

## Getting started

1. Clone this project:

```
git clone https://github.com/lawrencemontaril/pulsevote.git
```

2. Go to the project directory:

```
cd pulsevote
```

3. Set up a python virtual environment:

```
python -m venv env
```

4. Activate the environment:

```
.\env\Scripts\activate.bat
```

5. Install dependencies:

```
python -m pip install -r requirements.txt
```

6. Install TailwindCSS and its dependencies (requires Node.js):

```
python manage.py tailwind install
```

7. Apply the migrations:

```
python manage.py migrate
```

8. Run the server:

```
python manage.py runserver
```

9. And on a separate terminal instance, run a watcher for TailwindCSS:

```
python manage.py tailwind start
```
