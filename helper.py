def convert_zero_datetime(value):
    if value == '0000-00-00 00:00:00':
        return None
    return value

def convert_dates(table_instance):
    # List of attributes to convert
    attributes_to_convert = [
        'date_added',
        'date_modified',
        'date_archived',
        'date_deleted',
        'date_started',
        'date_completed',

    ]
    for attr in attributes_to_convert:
        if hasattr(table_instance, attr):  # Check if the attribute exists
            value = getattr(table_instance, attr)  # Get the value of the attribute
            # Check the value before converting
            if value == '0000-00-00 00:00:00':
                setattr(table_instance, attr, None)  # Set to None for the specific placeholder
            else:
                setattr(table_instance, attr, convert_zero_datetime(value))
