# Flask sample application
A simple web application created using Python Flask in a purely server rendered manner. See `task.py` for usage commands.


## Setup
Before the project can be setup, please ensure the following tools are installed on the system
- `nodejs` / `npm` - For installing front-end dependencies
- `venv` - For creating python virutal environments

Once the above tools have been setup on your system, run the following commands.

```bash
# create a new virutual environment
$ python -m venv .venv

# activate the environment
$ . .venv/bin/activate

# install back-end dependencies (listed inside pyproject.toml file)
$ pip install .

# install front-end dependencies
$ npm i -D

# create the .env file
$ cp -v .env.example .env
```


## Generate app secret
A unique secret key is required by the application for security reasons. Generate
the key using the following command and the value inside `.env` file

```bash
$ invoke gensecret
```


## Running migrations 

```bash
# ensure the database is initialized
$ invoke dbinit

# run the migrations
$ invoke dbmigrate
```

**Note**: Migrations can also be run through ```flask shell```

```bash
# open the application shell
$ invoke shell

>>> from app import db
>>> db.create_all()
```