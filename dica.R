export HADOOP_CONF_DIR='/etc/hadoop/conf'
bin/sparkR --packages com.databricks:spark-avro_2.11:3.0.0

spark1.6.1-
========================================
sparkR.stop()
Sys.setenv(HADOOP_CONF_DIR='/etc/hadoop/conf')
sc <- sparkR.init(sparkHome = "/home/admnet/spark-1.6.1-bin-hadoop2.6", sparkPackages="com.databricks:spark-csv_2.11:1.4.0")
sqlContext <- sparkRSQL.init(sc)
df <- read.df(sqlContext, '/tmp/DATA_USAIR/1988.csv', "com.databricks.spark.csv", header="true")
df <- read.df(sqlContext, 'DATA/2007.csv', "com.databricks.spark.csv", header="true")
registerTempTable(df, "voos")
destinos <- sql(sqlContext, "SELECT distinct(Origin) from voos")
head(destinos)
=========================================
spark1.6.1-YARN
sparkR.stop()
Sys.setenv(HADOOP_CONF_DIR='/etc/hadoop/conf')
Sys.setenv(YARN_CONF_DIR='/etc/hadoop/conf')
library(SparkR, lib.loc = "/home/admnet/spark-1.6.1-bin-hadoop2.6/R/lib")
library(magrittr)
sc <- sparkR.init(sparkHome = "/home/admnet/spark-1.6.1-bin-hadoop2.6", sparkPackages="com.databricks:spark-csv_2.11:1.4.0")
sqlContext <- sparkRSQL.init(sc)

df <- read.df(sqlContext, 'DATA/2007.csv', "com.databricks.spark.csv", header="true")
df %>% head %>% print
sparkR.stop()





# sparkR.stop()
# sparkR.session(sparkPackages = "com.databricks:spark-avro_2.11:3.0.0")

df <- read.df("DATA/2007.csv","csv",header="true",inferSchema = "true", na.strings = "NA")
printSchema(df)
df
head(df)
contado <- head(summarize(groupBy(df, df$Dest), count = n(df$Dest)),500)

createOrReplaceTempView(df, "voos")

sql("SELECT count(*) from voos where Dest = 'JFK'")
jfk <- sql("SELECT count(*) from voos where Dest = 'JFK'")
jfk
head(jfk)
sfo <- sql("SELECT count(*) from voos where Dest = 'SFO'")
head(sfo)
airport <- sql("select Dest, count(*) from voos group by Dest")
head(airport)
airport <- sql("select Dest, count(*) from voos group by Dest order by Dest")
head(airport)

airport <- sql("select Dest, count(*) as cnt from voos group by Dest order by cnt desc")

bin/spark-submit --master yarn-client --driver-memory 1g --num-executors 3 --packages com.databricks:spark-avro_2.11:3.0.0 ../sparkr-submit_test2.0.R
bin/spark-submit --master yarn-client --driver-memory 1g --num-executors 3 --packages com.databricks:spark-avro_2.11:3.0.0 ../sparkr-submit_test2.0.R


/home/admnet/spark-2.0.0-bin-hadoop2.6/bin/load-spark-env.sh: linha 67: spark.executor.uri=hdfs://srv001.continuidade.net.br:8020/user/admnet/spark-2.0.0-bin-hadoop2.6.tgz: Arquivo ou diretório não encontrado
Using Spark's default log4j profile: org/apache/spark/log4j-defa

/home/admnet/spark-2.0.0-bin-hadoop2.6/bin/load-spark-env.sh: linha 67: spark.executor.uri=/user/admnet/spark-2.0.0-bin-hadoop2.6.tgz: Arquivo ou diretório não encontrado
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLeve

/home/admnet/spark-2.0.0-bin-hadoop2.6/bin/load-spark-env.sh: linha 67: spark.executor.uri=hdfs://srv001.continuidade.net.br:8020/user/admnet/spark-2.0.0-bin-hadoop2.6.tgz: Arquivo ou diretório não encontrado
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel).


 bin/spark-shell --master mesos://192.168.56.11:5050 --spark.executor.uri hdfs://srv001.continuidade.net.br:8020/user/admnet/ -c spark.mesos.executor.home=`pwd`

admnet@srvhost:~/spark-2.0.0-bin-hadoop2.6$ bin/spark-shell --master mesos://192.168.56.11:5050 -c spark.mesos.executor.home=`pwd`                              /home/admnet/spark-2.0.0-bin-hadoop2.6/bin/load-spark-env.sh: linha 68: export: `spark.executor.uri==hdfs://srv001.continuidade.net.br:8020/user/admnet/spark-2.0.0-bin-hadoop2.6.tgz': não é um identificador válido
Setting default log level to "WARN".


.168.56.11:5050 -c spark.mesos.executor.home=`pwd`
/home/admnet/spark-2.0.0-bin-hadoop2.6/bin/load-spark-env.sh: linha 68: export: `spark.executor.uri=hdfs://srv001.continuidade.net.br:8020/user/admnet/spark-2.0.0-bin-hadoop2.6.tgz': não é um identificador válido
Setting default log level to "WARN".
Sys.setenv(HADOOP_CONF_DIR='/etc/hadoop/conf')
library(magrittr)
sc <- sparkR.init(sparkHome = "/home/admnet/spark-1.6.1-bin-hadoop2.6", sparkPackages="com.databricks:spark-csv_2.11:1.4.0")
sqlContext <- sparkRSQL.init(sc)
df <- read.df(sqlContext, '/tmp/DATA_USAIR/1988.csv', "com.databricks.spark.csv", header="true")
registerTempTable(df, "voos")
destinos <- sql(sqlContext, "SELECT distinct(Origin) from voos")
head(destinos)
history(9)
head(df)
head(df,1000)


spark.debug.maxToStringFields



