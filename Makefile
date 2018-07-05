venv:
	virtualenv -p python3 `basename .`
requirements:
	pip install -r requirements.txt
clean:
	rm -rf `cat .gitignore`
