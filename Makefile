create_dirs:
	mkdir -p data/exportable
	mkdir -p data/raw
	mkdir -p data/processed

setup: create_dirs
	@echo "Creating data structure and importing dependencies..."
	pip install -r requirements.txt

fetch:
	@echo "Fethching imported data from storage..."
	python src/data/fetch.py

gen_bin:
	@echo "Importing data from remote source and converting to be manualy exported to our storage"
	python src/data/gen_bin.py

install: setup fetch
	@echo 'Ready.'
