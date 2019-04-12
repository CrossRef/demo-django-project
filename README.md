# Django Demo Project

Quick demo project to show Django.

- Runs in Docker
- Hello World response
- Naive JSON response
- Django REST API based response.
- Swagger schema


First time, and if you change dependencies or Dockerfile:

    `docker-compose build`

To test:

    `docker-compose run dev /code/manage.py test`

To run development:

    `docker-compose run --service-ports dev`

Then visit

- <http://localhost:8000/>
- <http://localhost:8000/naive/numbers> - JSON response done naively.
- <http://localhost:8000/naive/numbers/28>
- <http://localhost:8000/numbers/> - API with properly defined entities.
- <http://localhost:8000/numbers/28/>
- <http://localhost:8000/docs/> - Auto generated Docs.
- <http://localhost:8000/metrics> - Prometheus metrics.
