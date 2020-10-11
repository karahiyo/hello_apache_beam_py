# hello_apache_beam_py

Hello [Apache Beam](https://beam.apache.org/) using Python.

## Setup

```
$ python3 -m venv venv

# 仮想環境をactivate
# fishの場合
$ source ./venv/bin/activate.fish

# Apach Beam SDK等pythonパッケージのinstall
$ pip install google-cloud-storage
$ pip install apache-beam[gcp]
```

## Run examples

### ParDo with a simple DoFn

```
$ python src/examples/pardo/main.py
🍓Strawberry
🥕Carrot
🍆Eggplant
🍅Tomato
🥔Potato
```

### WordCount

```
$ cd src/examples/wordcount
# ローカル実行
$ python main.py --input=./input.txt --output=./output.txt
# GCS上のデータを対象に実行
$ python main.py \
  --input gs://dataflow-samples/shakespeare/kinglear.txt \
  --output=./output.txt
```

### Pipeline Test

```
$ cd src/examples/count_length
# ローカル実行
$ python main.py --input=./input.txt --output=./output.txt
```

#### Test

```
$ pip install nose
$ nosetests .
```

