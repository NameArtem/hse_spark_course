# Шаблон проекта PySpark App
> 

<br>

### Содержание
* [Install](#install)
* [Usage](#usage)
<br>

### Install

> **[?]** Как начать использовать данные проекта

<a name="instal"></a>
```bash
# Create your spark job

# run
bash Makefile
```

## Usage

> **[?]** 

<a name="usage"></a>

### Usage

```bash
spark-submit \
	--py-files jobs.zib, ufuncs.zip, libs.zip \
	--files conf.json \
	main.py --job tmp_job.py
```
