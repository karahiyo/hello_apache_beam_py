import argparse
import logging

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class ComputeWordCount(beam.PTransform):

    def __init__(self):
        pass

    def expand(self, pcoll):
        return (pcoll
                | 'SplitWithHalfSpace' >> beam.Map(lambda element: element.split(' '))
                | 'ComputeArraySize' >> beam.Map(lambda element: len(element)))


def run(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='input.txt',
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        required=True,
        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)

    with beam.Pipeline(options=pipeline_options) as p:
        (
            p | 'Read' >> beam.io.ReadFromText(known_args.input)
            | 'ComputeWordCount' >> ComputeWordCount()
            | 'WriteToText' >> beam.io.WriteToText(known_args.output)
        )

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
