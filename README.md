WaterGo2016 - SoT Hackathon
===

## Data sources used:

 + [Access Freshwater Chemistry Data ("NRWQN")](https://teamwork.niwa.co.nz/pages/viewpage.action?pageId=38830500)

## Build

Initialize virtual environment

```
virtualenv venv
source ./venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Copy latest DB dump

```bash
cp `ls -1 dumps/* | head -1` flaskr.db
```

Run application

```bash
./run.py
```

## License

[MIT](https://github.com/herrjemand/WaterGo2016/blob/master/LICENSE.md) © WET Team