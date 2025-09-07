FROM python:3.12-alpine

#creating the workdir for container
WORKDIR /usr/local/app

# installing the depencies
COPY . .
COPY ./model_res/requirement.txt ./

#upgrading pip
# adding build-dependencies
RUN apk add --no-cache build-base
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 -r requirement.txt

EXPOSE 8501
#SETTING UP THE USER FOR NON-ROOT OPERATION and choosing the operation

RUN adduser -D app
USER app
ENTRYPOINT []

# running the app
CMD ["streamlit","run", "streamlit.py"]
