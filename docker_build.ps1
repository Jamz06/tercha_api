docker build -t api_test .
docker run --name recapi1 -p 8081:80 api_test