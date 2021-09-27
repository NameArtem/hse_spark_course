

import logging
import pytest

from pyspark import HiveContext
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def quiet_py4j():
    """ применение логгирования """
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)


@pytest.fixture(scope="session")
def spark_context(request):
    """ пример создание fixture (это функции, выполняемые pytest до (а иногда и после) фактических тестовых функций)
    
        создаем и тестируем сессию Spark
        
    Args:
        request: pytest.FixtureRequest object

    """
    conf = (SparkConf().setMaster("local[2]").setAppName("pytest-pyspark-local-testing"))
    sc = SparkContext(conf=conf)
    request.addfinalizer(lambda: sc.stop())

    quiet_py4j()
    return sc


@pytest.fixture(scope="session")
def hive_context(spark_context):
    """  Hive Context
    
    Args:
        spark_context: spark_context fixture

    Returns:
        HiveContext

    """
    return HiveContext(spark_context)


@pytest.fixture(scope="session")
def streaming_context(spark_context):
    return StreamingContext(spark_context, 1)
