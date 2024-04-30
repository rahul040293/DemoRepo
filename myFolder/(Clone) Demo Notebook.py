# Databricks notebook source
print("hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "hello world"

# COMMAND ----------

# MAGIC %md
# MAGIC # Test Text
# MAGIC

# COMMAND ----------

# MAGIC %run ./secondNotebook
# MAGIC

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


