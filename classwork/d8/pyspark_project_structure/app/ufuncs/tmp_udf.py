from parse import parse
from pyspark.sql.functions import udf
import pyspark.sql.types.* 


#########################################
# Place for functions
#########################################

def _some_udf(params):
    """
        You can write your own functions
    """
    return "Return result"



#########################################
# Place
#########################################

some_udf = udf(_some_udf, StringType())