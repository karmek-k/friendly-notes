# friendly-notes

## Installation

### With docker and docker-compose

Copy `.env.template` to `.env` and modify it
(you probably won't have to change DB_HOST from `db`):

```
cp .env.template .env
nano .env
```

Run docker-compose in detached mode:

```
docker-compose up -d
```

## Technologies used

- web framework: Django
- database: PostgreSQL
- reverse proxy: nginx
- containerization: Docker
