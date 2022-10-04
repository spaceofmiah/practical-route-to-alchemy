# practical-route-to-alchemy
My learning journey to sqlalchemy

## Requirements

- Basic understanding of python
- Docker fundamentals

### Getting Started

To get started, ensure to have python and docker installed and do make sure to have clone this repository. Below is an outline on how to run the application in no given order ( _just make sure to have completed all the steps before [running the application](#running-the-aplication)_ )

- [environment setup ( docker and postgres )](#environment-setup--docker-and-postgres-)

- [creating application database](#creating-application-database)

- [application setup](#application-setup)

- [running the application](#running-the-application)


#### Environment setup ( docker and postgres )

SQLAlchemy is a database wrapper that helps to easily connect and interact with the database. To be able to connect to postgres database, we need to have one readily available. Docker comes to the rescue. Run the below commands on your terminal / command prompt

> **Note:**
>
> Do make sure to have docker installed before running the commands below
>

```shell
docker pull postgres:12-alpine
```

Above command will pull postgres image to your local machine. This can be used to spin up postgres instance at will.

```shell
docker run --env POSTGRES_USER=admin --env POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:12-alpine
```

Above command will run the postgres image which was just pulled with a couple of settings 

`--env POSTGRES_USER=admin` sets the base user for which we can access the default database `postgres` as `admin` and you guess rightly `--env POSTGRES_PASSWORD=password` sets the user's password. `-p 5432:5432` connects your local machine to the port where the postgres is running on ( port wouldn't be opened for connectivity if not done ).

To confirm that we've a postgres instance running within docker run the below command 

```shell
docker ps -a
```

Above command simply says, show me the running containers. You should see a container whose _IMAGE_ column holds value _postgres:12-alpine_ and _PORTS_ column hold values _0.0.0.0:5432->5432/tcp_. Now you'll have to pay attention to either of these column _NAME_ or _CONTAINER ID_ and take note of the values they've got as the below command will be needing either of them

```shell
docker exec -it (NAME value | CONTAINER_ID value ) bash
```

Above command gives access into the running database container within which we can proceed to creating the application database

#### Creating application database

Now that we've postgres instance up and have gain access into it, run the following command to create a database which we'll be working with.

> **Note:**
>
> Do make sure to have gained access into a running docker postgres:12-alpine container [how to](#environment-setup--docker-and-postgres-)
>

```shell
psql --username=admin --password
```

The above will bring up an interactive interface for you to enter the password which was given to the admin user during creation of a postgres instance. After entering the password (which is _password_ if you followed the [instructions](#environment-setup--docker-and-postgres-) from to the T), press your return key or enter button.

This should give you access into postgres environment where you can proceed to creating a postgres database.

```sql
CREATE DATABASE learnsqlalchemy;
CREATE USER learner WITH PASSWORD 'StrongPassword123';
GRANT ALL PRIVILEGES ON DATABASE learnsqlalchemy TO learner;
```

The above command would give us the database configuration

DATABASE_NAME = learnsqlalchemy

DATABASE_USER = learner

DATABASE_PASSWORD - StrongPassword123

> **Disclaimer:**
>
> This is just a learning process therefore, these values are not to be used in a real world application. Kindly ensure to use a stronger value for each setup. Something only you know
>

We're now ready to explore the application setup

#### Application setup

Aside to prefill [application database](#creating-application-database) values as environment variables, you'll also install the needed dependencies. 

**Prefill Application Database Values**

The root directory has a `config.ini.tpl` which is a template of how the required environment variables. Rename this file to `config.ini` and fill the values ( those with _xxxx_ ) accordingly. If you've followed the setup in this guide, your configuration should be

```ini
[database]
username=learnsqlalchemy
password=StrongPassword123
name=learnsqlalchemy
host=localhost
port=5432
```

**Install Application Dependencies**

Run the following command to create and activate a virtual environment 

```shell
python -m venv env
```

If you're on windows, use the first command and linux the second command to activate just created virtual environment

**first**

```shell
source env/Script/activate
```

**second**

```shell
source env/bin/activate
```

Now that virtual environment is created and activated, run the below command to install application dependencies

```shell
pip3 install -r requirements.txt
```

#### Running the application 

Run `python main.py` to run the application.

To confirm that the setup is successful you should have an "Hello World" output 

```bash
2022-10-03 17:16:31,150 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2022-10-03 17:16:31,150 INFO sqlalchemy.engine.Engine [raw sql] {}
2022-10-03 17:16:31,156 INFO sqlalchemy.engine.Engine select current_schema()
2022-10-03 17:16:31,156 INFO sqlalchemy.engine.Engine [raw sql] {}
2022-10-03 17:16:31,165 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2022-10-03 17:16:31,165 INFO sqlalchemy.engine.Engine [raw sql] {}
2022-10-03 17:16:31,173 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-10-03 17:16:31,173 INFO sqlalchemy.engine.Engine select 'Hello World'
2022-10-03 17:16:31,173 INFO sqlalchemy.engine.Engine [generated in 0.00092s] {}
[('Hello World',)]
2022-10-03 17:16:31,185 INFO sqlalchemy.engine.Engine ROLLBACK
```

#### Codebase Structure

> **Disclaimer:**
>
> The application setup is by no means an opinionated approach to setting up sqlalchemy (especially when learning). I'm using what i'm most comfortable with at the moment. 
>

> **Note:**
>
> If you're following along this setup, kindly ensure to follow to the T the setup in this repository (which cloning should have fixed) otherwise, you might have issues running the code
>

**`conf/`** : All application configurations, goes in here

**`db/`** : Houses all database related activities e.g _engine initializer, orm e.t.c_

**`src/`** : Application source code resides here

**`main.py`** : Application entrypoint

