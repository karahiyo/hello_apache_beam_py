import apache_beam as beam

# Create pipeline.
schema = ({'fields': [{'name': 'a', 'type': 'STRING', 'mode': 'REQUIRED'}]})

p = beam.Pipeline()

errors = (
        p | 'Data' >> beam.Create([1, 2])
        | 'CreateBrokenData' >>
        beam.Map(lambda src: {'a': src} if src == 2 else {'a': None})
        | 'WriteToBigQuery' >> beam.io.WriteToBigQuery(
            "<Your Project:Test.dummy_a_table",
            schema=schema,
            insert_retry_strategy='RETRY_ON_TRANSIENT_ERROR',
            create_disposition='CREATE_IF_NEEDED',
            write_disposition='WRITE_APPEND'))

result = (
        errors['FailedRows']
        | 'PrintErrors' >>
        beam.FlatMap(lambda err: print("Error Found {}".format(err))))
