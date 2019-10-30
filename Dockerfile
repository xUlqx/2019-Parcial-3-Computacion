FROM python:3

RUN git clone https://github.com/xUlqx/2019-Parcial-3-Computacion.git

WORKDIR /2019-Parcial-3-Computacion.git

CMD [ "python3", "test_tateti.py" ]