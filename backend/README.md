python -m uvicorn main:app --reload

docker build -t my-fastapi-app .
docker run -p 8080:80 my-fastapi-app