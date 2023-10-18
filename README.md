# Flask sample application
A simple web application created using Python Flask in a purely server rendered manner. See `Makefile` for usage commands.


## Setup
Before the project can be setup, please ensure the following tools are installed on the system
- `make` - For running common project-related commands
- `nodejs` / `npm` - For installing front-end dependencies
- `venv` - For creating python virutal environments

Once the above tools have been setup on your system, run the following commands.

```bash
# create a new virutual environment
$ python -m venv .venv

# activate the environment
$ . .venv/bin/activate

# install project dependencies
$ make install-deps
```


## Running migrations 

```bash
# ensure the database is initialized
$ make db-init

# run the migrations
$ make db-migrate -m <migration-name>
```

**Note**: Migrations can also be run through ```flask shell```

```bash
# open the application shell
$ make shell

>>> from app import db
>>> db.create_all()
```