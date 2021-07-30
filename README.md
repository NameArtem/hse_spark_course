# Magnit Spark course

## Cодержание
- [Как работают и где живут большие данные](#t1)
- [Погружение среду Spark. Spark RDD / Spark SQL](#t2)
- [Spark ML / Spark TimeSeries](#t4)
- [Advanced ML & проверка результатов качества моделей](#t5)
- [Spark Ecosystem (AirFlow, H2O AutoML)](#t7)
- [Spark в архитектуре проекта / Spark CI/CD](#t8)



## Инфраструктура курса

- [Локальный кластре на Docker](https://github.com/NameArtem/hadoop-spark-standalone-docker)
- [DataBricks Community](/tutorials/databricks_tutorial)

## План курса

|№|Тема занятия| Статус| Дата | Ссылка|
|:---:|:---:|:---:|:---:|:---:|
|1| Как работают и где живут большие данные |Готово |25.06.2021||
|2.1| Погружение среду Spark. Spark RDD / Spark SQL | Готово |02.07.2021||
|2.2| Spark DF, UDF. Особенности работы с данными. 5 Слов о формате | Готово |||
|3.1| Spark ML  |Готово |||
|3.2| Spark Рекомендашки |Перенесено |||
|4| Advanced ML & проверка результатов качества моделей | |||
|5| Spark Ecosystem (AirFlow, H2O AutoML) | |||
|6| Spark в архитектуре проекта / Spark CI/CD | |||



## 1 Как работают и где живут большие данные
<a name='t1'></a>

**Рассмотрели:**

- [Презентация](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/pres/p1.pdf) по обзору "Проблем больших данных"
- [MrJob](https://github.com/NameArtem/hse_spark_course/tree/mgnt_tech/classwork/d1/3_MRJob_tutorial) библиотеку и сравнили её [Hadoop job](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/classwork/d1/MapReduce%20%D1%81%20python(mrjob).ipynb)

**Задание на самостоятельную работу:**

- [Исследовать и построить социальные связи по email Хиллари Клинтон](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/classwork/d1/3_MRJob_tutorial/3_3_emails/3_3.ipynb)

</br>

## 2.1 Погружение среду Spark. Spark RDD / Spark SQL
<a name='t2'></a>

**Рассмотрели:**

- [Знакомство](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/pres/p2.pdf) с Spark RDD и Spark SQL(DataFrame)
- [Распределение ресурсов Spark](https://github.com/NameArtem/hse_spark_course/tree/mgnt_tech/classwork/d2)

**Задание на самостоятельную работу:**

- [Выбрать набор данных для выполнения практических работ](https://cseweb.ucsd.edu/~jmcauley/datasets.html#)
- Сделать EDA выбранных данных:
  - https://habr.com/ru/post/353050/
  - https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce
  - https://www.analyticsvidhya.com/blog/2020/08/exploratory-data-analysiseda-from-scratch-in-python/

</br>

## 2.2 Spark DF

**Задание на самостоятельную работу:**

- на основе [файла-исследование EDА](https://github.com/NameArtem/hse_spark_course/tree/mgnt_tech/works/eda_t1) сделать EDA, но на PySpark (там сейчас в Pandas, нужно повторить на Spark)
- обратите внимание на повторяющийся код, сделайте из него функции.
- предложите варианты визуализации из PySpark



## 3.1 Spark ML
<a name='t4'></a>

**Рассмотрели:**

- [Spark ML Regression](https://github.com/NameArtem/hse_spark_course/tree/mgnt_tech/classwork/d4)


## 3.2 Advanced ML Рекомендашки

<a name='t5'></a>

**Задание на самостоятельную работу:**

- В [файле](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/classwork/d5_home/Recom_ALS.ipynb) заполнить пропуски и реализовать рекомендации алгоритмом ALS

## Spark Ecosystem (AirFlow, H2O AutoML)

<a name='t7'></a>


## Spark в архитектуре проекта / Spark CI/CD

<a name='t8'></a>

</br>

## Spark Data Quality проект

Проект базируется на том, что [DQ процесс входит в KPI сотрудников работающих с данными](https://www.datafold.com/blog/the-state-of-data-quality-in-2021/)

**Библиотека для проекта**

- PySpark [PyDeeQu](https://pypi.org/project/pydeequ/)
- Python [greatexpectations](https://greatexpectations.io/)

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

- Изучите библиотеку и попробуйте сделать:0
  - поиск аномалий в данных [пример поиска аномалий](https://www.reg.ru/blog/ishchem-anomalii-s-python-chast-1/)
  - профилирование в данных [про профилирование](https://www.machinelearningmastery.ru/automated-data-profiling-99523e51048e/) и [ещё немного](https://habr.com/ru/post/441538/) + [это](https://www.dvbi.ru/articles/reading/data-profiling-is-necessary-step-towards-building-DWH)



<br>
