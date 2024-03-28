path := $(shell pwd)/app

run:
	PYTHONPATH=$(path) uvicorn main:app --reload --host 0.0.0.0 --port 8000