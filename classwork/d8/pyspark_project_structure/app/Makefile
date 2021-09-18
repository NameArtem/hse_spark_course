# there is an example for building your app

build:
	rm -rf ./dist && mkdir ./dist
	cp ./main.py ./dist
	cp ./config.json ./dist
	zip -r dist/jobs.zip jobs
	zip -r dist/shared.zip shared
	pip install -r requirements.txt -t ./dist/libs
	cd ./dist/libs && zip -r -D ../libs.zip .