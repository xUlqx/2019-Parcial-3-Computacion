FROM python:3

RUN git clone https://github.com/xUlqx/2019-Parcial-3-Computacion.git

WORKDIR /2019-Parcial-3-Computacion.git

RUN pip install parameterized

RUN pip install -r requirements.txt

RUN python3 test_tateti.py

CMD [ "python3", "test_tateti.py" ]

