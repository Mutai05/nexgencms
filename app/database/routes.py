from flask import render_template
from app import db
from app.database import database
from sqlalchemy import inspect, MetaData, text
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required

# Database details

@database.route('/')
@login_required
def db_details():
    # Reflect the database schema
    metadata = MetaData()
    metadata.reflect(bind=db.engine)
    
    # Exclude the 'alembic_version' table
    table_names = [name for name in metadata.tables.keys() if name != 'alembic_version']
    
    tables_data = {}
    for table_name in table_names:
        try:
            if table_name == 'logs':
                query = text(f"SELECT * FROM {table_name} ORDER BY id DESC")
            else:
                table = metadata.tables[table_name]
                query = table.select()
            
            result = db.session.execute(query).fetchall()
            tables_data[table_name] = [dict(row._asdict()) for row in result]
        except SQLAlchemyError as e:
            tables_data[table_name] = str(e)
    
    return render_template('db_details.html', tables_data=tables_data)
