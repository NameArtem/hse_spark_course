import json
import importlib
import argparse
from pyspark.sql import SparkSession


def _parse_arguments():
    """ 
        spark-submit args
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    return parser.parse_args()


def main():

    args = _parse_arguments()

    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    spark = SparkSession.builder.appName(config.get("app_name")).getOrCreate()

    job_module = importlib.import_module(f"jobs.{args.job}")
    job_module.run_job(spark, config)


if __name__ == "__main__":
    main()