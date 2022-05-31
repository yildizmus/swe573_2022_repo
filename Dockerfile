FROM python:3.11.0b1-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /code

COPY Pipfile Pipfile.lock ./

#RUN pip install psycopg2-binary
#RUN pip install gunicorn
RUN pip install jmespath
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --skip-lock --system --dev

EXPOSE 8000
COPY . .
CMD ["gunicorn", "--chdir", "swe573_2022_repo", "--bind", ":8000", "colearning.wsgi:application", "--reload"] 	

