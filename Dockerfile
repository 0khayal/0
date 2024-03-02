FROM dyler2/main:slim-buster

WORKDIR /root/main

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3","-m","main"]
