# Jay Hussaini's Orbital Witness technical test

## Running the API

Before running for the first time install the dependencies:

`pip install -r requirements.txt`

install the server:

`pip install "uvicorn[standard]"`

Run `uvicorn main:app --reload` from the root folder to start the API.

The API can then be reached at `http://127.0.0.1:8000/`

## Running the tests

### Unit tests

`pip install pytest`

`python -m pytest unit_tests/`

### Integration tests

## API Specification

[SwaggerUI](http://127.0.0.1:8000/docs)

[ReDoc](http://127.0.0.1:8000/redoc)

## Notes

- `test_list_titles_second_page_empty` demonstrates that when paging beyond the limit of
    the result set an empty array will be returned. Instead, it might be desirable to check
    for this and return a warning.
- 