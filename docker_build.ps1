docker build -t api_test .
docker run --name tercha_api -p 8081:80 api_test