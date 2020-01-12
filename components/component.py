from sqlalchemy.ext.declarative import declarative_base


Component = declarative_base()


def get_table_name_to_class_mapping():
    return {
        c.__tablename__: c for c in Component.__subclasses__()
    }


def component_repr(obj):
    """Return a dictionary-style string of the component."""
    return '{0}{1}'.format(
        str(obj.__class__.__name__),
        str({k: v for k, v in obj.__dict__.items() if k != '_sa_instance_state'})
    )
