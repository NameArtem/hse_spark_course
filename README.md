# hse_spark_course

## Cодержание
- [Введение в распределенные вычисления](#t1)
- [Apache Spark. RDD](#t2)
- [Apache Spark. DataFrame](#t3)
- [Знакомство со Scala](#t4)
- [Spark ML](#t5)
- [Spark Recommendations](#t6)
- [Spark Recom-Pandas_udf-Streaming](#t7)
- [Spark Production](#t8)
- [Финальный проект](#finpro)



## Инфраструктура курса

- [Локальный кластре на Docker](https://github.com/NameArtem/hadoop-spark-standalone-docker)
- [DataBricks Community](/tutorials/databricks_tutorial)

## План курса

|№|Тема занятия| Статус| Дата | Ссылка|
|:---:|:---:|:---:|:---:|:---:|
|1| Введение в распределенные вычисления |Готово |21.06.2021||
|2| Apache Spark (RDD) (+ FuncProg на Python) | Готово |||
|3| Spark SQL. Анализ больших данных | Готово |||
|4| Подробнее о модели вычислений Spark. Знакомство со Scala | |||
|5| Spark ML | |||
|6| Рекомендательные системы на Spark | |||
|7| Ещё о системах рекомендаций. О Spark UDF. Spark Structure Streaming (+ интеграция со Spark ML) | |||
|8| Модели в прод. Управленеи кластеровм  | |||



## Введение в распределенные вычисления
<a name='t1'></a>

Краткое соедержание:
- Что такое распределенные вычисления
- Как установить и работать со Spark | Hadoop
- Python MRJob библиотека (как вариант работы с распределенными вычислениями)


## Apache Spark. RDD
<a name='t2'></a>

Краткое соедержание:
- Функциональное программирование на Python (как способ минимизации сложности входа в Spark RDD)
- Знакомство с RDD (разбор примеров)
- Код на RDD

## Apache Spark. DataFrame
<a name='t3'></a>

Краткое соедержание:
- Переход от RDD к DataFrame
- Примеры и разбор Spark DF

## Знакомство со Scala
<a name='t4'></a>

Краткое соедержание:
- Минимум о Scala
- Spark DF на Scala


## Spark ML
<a name='t5'></a>



## Spark Recommendations
<a name='t6'></a>




## Spark Recom-Pandas_udf-Streaming

<a name='t7'></a>


## Spark Production

<a name='t8'></a>


## Финальный проект
<a name='finpro'></a>

## Data Quality

## Data Quality

Проект базируется на том, что [DQ процесс входит в KPI сотрудников работающих с данными](https://www.datafold.com/blog/the-state-of-data-quality-in-2021/)

**Библиотека для проекта**

- [PyDeeQu](https://pypi.org/project/pydeequ/)

**Данные для проекта** - самостоятельный выбор

### Первое задание по DQ

- Используя PyDeeQu проведите быстрый обзор ваших данных

```Python
from pydeequ.checks import *
from pydeequ.verification import *

# примерные данные
df = spark.sparkContext.parallelize([
    Row(a="foo", b=1, c=5),
    Row(a="bar", b=2, c=6),
    Row(a="baz", b=3, c=None)]).toDF()

# инициализация теста
check = Check(spark, CheckLevel.Error, "Integrity checks")

# rdd обзор / тест данных
checkResult = VerificationSuite(spark) \
    .onData(df) \
    .addCheck(
        check.hasSize(lambda x: x >= 3) \
        .hasMin("b", lambda x: x == 0) \
        .isComplete("c")  \
        .isUnique("a")  \
        .isContainedIn("a", ["foo", "bar", "baz"]) \
        .isNonNegative("b")) \
    .run()

# запуск верификации
checkResult_df = VerificationResult.checkResultsAsDataFrame(spark, checkResult)
checkResult_df.show()

# описание результата
if checkResult.status == "Success":
    print('Тесты пройдены')

else:
    print('Найдены ошибки:')

    for check_json in checkResult.checkResults:
        if check_json['constraint_status'] != "Success":
            print(f"\t{check_json['constraint']} причина: {check_json['constraint_message']}")
```

- Изучите библиотеку и попробуйте сделать:
  - поиск аномалий в данных (пример поиска аномалий)[https://www.reg.ru/blog/ishchem-anomalii-s-python-chast-1/]
  - профилирование в данных (про профилирование)[https://www.machinelearningmastery.ru/automated-data-profiling-99523e51048e/] и (ещё немного)[https://habr.com/ru/post/441538/] + (это)[https://www.dvbi.ru/articles/reading/data-profiling-is-necessary-step-towards-building-DWH]



<br>
