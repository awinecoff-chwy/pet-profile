import os
import configparser

#use this if you are a dork running in Spyder
os.environ['DSECONFIG']='/Users/awinecoff/Documents/PythonScripts'

config = configparser.ConfigParser()

config.read(os.getenv("DSECONFIG") + "/db_config.ini")

config.sections()
topsecret = config["connection"]
aerospike = config["aerospike-host"]
redishost = config["redis-host"]
#snowflake_schema = config["snowflake-schema"]
#snowflake_conn = config["snowflake-connection"]

bidb = {
    "host": topsecret["host"],
    "port": topsecret["port"],
    "user": topsecret["user"],
    "password": topsecret["password"],
    "database": topsecret["database"],
    "unicode_error": topsecret["unicode_error"],
    "ssl": False,
}

aero = {"aero-host": aerospike["host"]}

redis = {"redis-host": redishost["host"]}

#sf_schema = {"snowflake-schema": snowflake_schema["dse_schema"]}

#snowflake_connection = {
#    "user": snowflake_conn["user"],
#    "password": snowflake_conn["password"],
#    "account": snowflake_conn["account"],
#}
