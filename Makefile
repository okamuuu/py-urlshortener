all: mongod 

mongod:
	@touch data/
	@mongod --dbpath=data/

export:
	@mongoexport -d urlshortener -c urls > test/data/urls.json

import:
	@mongoimport -d urlshortener -c urls test/data/urls.json

clean:
	@echo 'db.dropDatabase()' | mongo urlshortener

test:
	@python tests/test-base62.py
	@python tests/test-db.py
