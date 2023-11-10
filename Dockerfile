FROM chennavarri/ubuntu_opencv_python

WORKDIR /app
COPY server.py /app/

RUN apt-get install -y openssl

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install flask

ENV PYTHONPATH=/app