install:
	pip install -r requirements.txt

format:	
	find . -type f -name "*.py" -exec black {} \;
	find . -type f -name "*.ipynb" -exec nbqa black {} \;


lint:
	find . -type f -name "*.py" -exec ruff check {} \;
	find . -type f -name "*.ipynb" -exec nbqa ruff {} \;

test:
	# python -m pytest -vv --cov=codes/project_codes codes/test_codes/*.py
	# python -m pytest --nbval codes/project_codes/*.ipynb 

all : install test format lint 