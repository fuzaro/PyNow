sparkR.stop()
sparkR.session(sparkPackages = "com.databricks:spark-avro_2.11:3.0.0")
df <- read.df("DATA/2007.csv","csv",header="true",inferSchema = "true", na.strings = "NA")
printSchema(df)
df
head(df)
contado <- head(summarize(groupBy(df, df$Dest), count = n(df$Dest)),500)
