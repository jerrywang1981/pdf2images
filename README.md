# pdf2images
convert pdf to pictures

### install poppler
```
conda install -c conda-forge poppler
```

### install pdf2image
```
pip install pdf2image
```

### to run in python
```python
python convert_pdf_to_image.py xxx yyy
```

### to build image
```
docker image build -t jerrywang1981/pdf2image:0.0.1 .
```

### or pull existing if you want to
```
docker pull jerrywang1981/pdf2image:0.0.1
```

### to convert pdf
* /xxx your pdf folder
* /yyy your output folder


```
docker run --rm -v /xxx:/input -v /yyy:/output -it jerrywang1981/pdf2image:0.0.1
```

## if you want to build executable
```
go build pdf2image.go
chmod +x pdf2image
```

