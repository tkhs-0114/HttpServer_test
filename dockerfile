FROM python:3.10
WORKDIR /usr/src
RUN pip install flask==2.3.2
COPY ./main.py /usr/src/main.py
CMD python main.py