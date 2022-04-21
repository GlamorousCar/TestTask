FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/TestTask

#ENV VIRTUAL_ENV=/usr/src/TestTask
#RUN python3 -m venv $VIRTUAL_ENV
RUN pip3 install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
COPY ./requirements.txt usr/src/requirements.txt
#RUN pip install -r usr/src/requirements.txt


COPY . /usr/src/TestTask
RUN pip install -r usr/src/requirements.txt
#RUN pip install poetry
#RUN poetry build && /venv/bin/pip install dist/*.whl

EXPOSE 8000
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
