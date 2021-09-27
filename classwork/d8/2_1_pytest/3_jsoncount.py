from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark import HiveContext


def do_json_counts(df, target_name):
    """ тестирование условия, если target_name есть в Df"""

    return df.filter(df.name == target_name).count()


if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.exit("Usage: json file}")
    
    sc = SparkContext(appName="PythonJsonCount")
    hc = HiveContext.getOrCreate(sc)
    df = hc.read.json(sys.argv[1], 1)
    
    print("Name found %d times" % do_json_counts(df, 'vikas'))
    

