import os
import click
import flask_migrate
from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

import models
from seeds import data


@click.command()
@with_appcontext
def init_db():
    create_db()
    flask_migrate.upgrade()
    load_seed_data(data)


def create_db():
    data_base = os.environ['DB_CONNECTION_STRING']
    # funcion para crear base de datos 
    if not database_exists(data_base):
        create_database(data_base)

    create_engine(data_base, encoding="latin1", echo=True)


# aqui se cargan los datos de seed_data y se insertan en la tabla
def load_seed_data(data):
    for table, rows in data.items():
        print(rows)
        ModelClass = getattr(models, table)

        for row in rows:
            new_row = ModelClass(**row)
            models.db.session.merge(new_row)

    models.db.session.commit()