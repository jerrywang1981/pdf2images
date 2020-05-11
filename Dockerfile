FROM continuumio/anaconda3:latest
LABEL maintainer "wangjianjun@gmail.com"

RUN conda install -c conda-forge poppler

RUN mkdir -p /home/app

WORKDIR /home/app
COPY requirements.txt ./
COPY . .

RUN pip install -r requirements.txt

VOLUME [ "/input", "/output" ]

ENTRYPOINT ["python", "convert_pdf_to_image.py", "/input"]
CMD ["/output"]
