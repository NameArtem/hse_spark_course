import pytest

from . import jsoncount

# фиксация fixture для всех тестов pyspark
pytestmark = pytest.mark.usefixtures("spark_context", "hive_context")


def test_do_json_counts(spark_context, hive_context):
    """ проверска парсинга на одном событие
    Args:
        spark_context: test fixture SparkContext
        hive_context: test fixture HiveContext
    """

    test_input = [
        {'name': 'vikas'},
        {'name': 'vikas'},
        {'name': 'john'},
        {'name': 'jane'},
    ]

    input_rdd = spark_context.parallelize(test_input, 1)
    df = hive_context.jsonRDD(input_rdd)
    results = jsoncount.do_json_counts(df, 'vikas')

    expected_results = 2
    assert results == expected_results
