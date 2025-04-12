set up virtualenv

```bash
python3 -m venv env
source env/bin/activate
```

install requirements

```bash
pip install -r requirements.txt
```

migrate database

```bash
python manage.py migrate
```

run server

```bash
python manage.py runserver
```

## Screenshots

### Full page

![full page](screenshots/full_screenshot.png)

### Login page

![login page](screenshots/login.png)

### Register page

![register page](screenshots/register.png)

### After login

![after login](screenshots/after_login.png)

### Question detail with answers

![question detail](screenshots/question_detail_with_answers.png)

### Edit question

![edit question](screenshots/edit_question.png)

### Edit answer

![edit answer](screenshots/edit_answer.png)
