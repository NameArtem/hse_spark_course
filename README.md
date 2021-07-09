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
|2.2| Spark DF, UDF. Особенности работы с данными. 5 Слов о формате | Перенесено |||
|3| Spark ML / Spark TimeSeries | |||
|4| Advanced ML & проверка результатов качества моделей | |||
|5| Spark Ecosystem (AirFlow, H2O AutoML) | |||
|6| Spark в архитектуре проекта / Spark CI/CD | |||



## Как работают и где живут большие данные
<a name='t1'></a>

**Рассмотрели:**

- [Презентация](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/pres/p1.pdf) по обзору "Проблем больших данных"
- [MrJob](https://github.com/NameArtem/hse_spark_course/tree/mgnt_tech/classwork/d1/3_MRJob_tutorial) библиотеку и сравнили её [Hadoop job](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/classwork/d1/MapReduce%20%D1%81%20python(mrjob).ipynb)

**Задание на самостоятельную работу:**

- [Исследовать и построить социальные связи по email Хиллари Клинтон](https://github.com/NameArtem/hse_spark_course/blob/mgnt_tech/classwork/d1/3_MRJob_tutorial/3_3_emails/3_3.ipynb)

</br>

## Погружение среду Spark. Spark RDD / Spark SQL
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

## Spark DF

**Задание на самостоятельную работу:**

- на основе [файла-исследование EDА](https://github.com/NameArtem/hse_spark_course/tree/mgnt_tech/works/eda_t1) сделать EDA, но на PySpark (там сейчас в Pandas, нужно повторить на Spark)
- обратите внимание на повторяющийся код, сделайте из него функции.
- предложите варианты визуализации из PySpark



## Spark ML / Spark TimeSeries
<a name='t4'></a>




## Advanced ML & проверка результатов качества моделей
<a name='t5'></a>



## Spark Ecosystem (AirFlow, H2O AutoML)

<a name='t7'></a>


## Spark в архитектуре проекта / Spark CI/CD

<a name='t8'></a>

</br>

## Spark Data Quality Проект
