"""Alembic environment configuration."""
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Import your models here
from app.models import User  # Example import

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Ensure the application package is on the Python path.
# This assumes your app package is in the parent directory.
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Set up your database configuration here
from app import db, create_app
app = create_app()
with app.app_context():
    target_metadata = db.metadata

# Add your model metadata to the Alembic configuration
config.set_main_option('sqlalchemy.url', str(app.config['SQLALCHEMY_DATABASE_URI']))
config.set_main_option('sqlalchemy.schema', 'your_schema_name')  # Replace with your actual schema name

# Other settings for database connections, etc.
# ...

# Exclude tables from the auto-generate process if needed
def include_object(object, name, type_, reflected, compare_to):
    return not object.info.get('exclude_from_auto_build', False)


# This function is used for database reflection
def run_migrations_offline():
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # Other settings as needed
        # ...
    )
    with context.begin_transaction():
        context.run_migrations()


# This function is used for migrations when online
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            include_object=include_object,
            # Other settings as needed
            # ...
        )

        with context.begin_transaction():
            context.run_migrations()


# Main entry point for Alembic migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
