FROM chennavarri/ubuntu_opencv_python

WORKDIR /app
COPY . /app/

# RUN apt-get install -y openssl

# RUN pip install --upgrade pip
# RUN pip install requests
# RUN pip install flask

# COPY requirements.txt /app/
# RUN pip install -r requirements.txt

# ENV PYTHONPATH=/app