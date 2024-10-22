def convert_zero_datetime(value):
    if value == '0000-00-00 00:00:00':
        return None
    return value

def convert_dates(db_project):
    db_project.date_added = convert_zero_datetime(db_project.date_added)
    db_project.date_modified = convert_zero_datetime(db_project.date_modified)
    db_project.date_archived = convert_zero_datetime(db_project.date_archived)
    db_project.date_deleted = convert_zero_datetime(db_project.date_deleted)