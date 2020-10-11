import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam import pvalue


class FilterMeanLengthFn(beam.DoFn):
    """平均以上の文字数を持つ文字列をフィルタリングする."""

    def __init__(self):
        pass

    # mean_word_length は副入力
    def process(self, element, mean_word_length):
        if len(element) >= mean_word_length:
            yield element


def run():
    p = beam.Pipeline(options=PipelineOptions())

    inputs = ['good morning.', 'good afternoon.', 'good evening.']

    # 副入力
    mean_word_length = (p
                        | 'CreateWordLength' >> beam.Create([len(s) for s in inputs])
                        | 'ComputeMeanWordLength' >> beam.CombineGlobally(beam.combiners.MeanCombineFn()))

    # 主入力
    output = (p
              | 'CreateWord' >> beam.Create(inputs)
              | 'FilterMeanLength' >> beam.ParDo(FilterMeanLengthFn(), pvalue.AsSingleton(mean_word_length))  # ParDo の第２引数に副入力を挿入する
              | 'WriteToText' >> beam.io.WriteToText('出力先のパス'))

    p.run().wait_until_finish()


if __name__ == '__main__':
    run()

