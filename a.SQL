[
    SchemaField('repo_name', 'STRING', 'NULLABLE', None, (), None),
    SchemaField('language', 'RECORD', 'REPEATED', None, (
        SchemaField('name', 'STRING', 'NULLABLE', None, (), None), 
        SchemaField('bytes', 'INTEGER', 'NULLABLE', None, (), None))
    , None)
]