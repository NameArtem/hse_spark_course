import pytest

from . import wordcount

# фиксация fixture для всех тестов pyspark
pytestmark = pytest.mark.usefixtures("spark_context")



def test_do_word_counts(spark_context):
    """ тестирование функции подсчета слов
    Args:
        spark_context: test fixture SparkContext
        hive_context: test fixture HiveContext
    """
    
    # ?
    test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]

    input_rdd = spark_context.parallelize(test_input, 1)
    
    # ?
    results = wordcount.do_word_counts(input_rdd)
    
    expected_results = {'hello':2, 'spark':3, 'again':1}  
    assert results == expected_results

