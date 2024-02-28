FROM dyler2/khayal:slim-buster

RUN git clone https://github.com/dyler2/khayal.git /root/khayal

WORKDIR /root/khayal

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/khayal/bin:$PATH"

CMD ["python3","-m","khayal"]
