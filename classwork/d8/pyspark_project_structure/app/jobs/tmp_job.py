from pyspark.sql.functions import col, expr
from shared.udfs import get_movie_title_udf, get_movie_year_udf


def _first_step(spark, config):
    """ 
        Write code 
        what will be the first step 
        in the app
    """
    
    return (
        spark.read.format("csv")
             .option("header", "true")
             .load(f"{config.get('source_data_path')}/somefile")
    )


def _second_step(df):
    """ 
        Next step into your app 
    """
    return df
    

def _etc_step(config, df):
    """ 
        For example - save to parquet
    """
    
    df.write.mode("overwrite").parquet(f"{config.get('output_data_path')}/somefile"
    )


def run_job(spark, config):
    """ 
        Run job 
    """
    
    _etc_step(config, _second_step(_first_step(spark, config)))