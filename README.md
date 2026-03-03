# Python Starter Project Skeleton based on DDD Clean Architecture
Starter python project based on DDD clean code architecture

## Struktur Project (DDD Style)
```
app/
 ├── domain/
 │    ├── entities/
 │    │     └── user.py
 │    ├── repositories/
 │    │     └── user_repository.py
 │    └── services/
 │          └── user_domain_service.py
 │
 ├── application/
 │    └── usecases/
 │          ├── create_user.py
 │          └── get_user.py
 │
 ├── infrastructure/
 │    ├── config/
 │    │     ├── base.py
 │    │     ├── development.py
 │    │     ├── production.py
 │    │     ├── loader.py
 │    │     ├── factory.py
 │    │     └── schema.py
 │    ├── database.py
 │    └── repositories/
 │          └── user_repository_impl.py
 ├── core/
 │    ├── logger.py
 │    ├── metrics.py
 │    └── middleware.py
 │
 ├── interfaces/
 │    └── http/
 │          ├── schemas.py
 │          └── user_controller.py
 │
 ├── config/
 │    ├── base.yaml
 │    ├── development.yaml
 │    └── production.yaml
 │
 ├── .env
 └── main.py

tests/
 ├── domain/
 ├── application/
 ├── infrastructure/
 └── interfaces/

```

## Install Requirements
```
$ pip install pydantic-settings PyYAML
$ pip install pytest

# Install Editable
$ pip install -e .

# Tests
$ pytest path/to/file.py::function_name
```
