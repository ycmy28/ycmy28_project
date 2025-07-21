from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
env.from_collection(
    collection=["hello", "world"]
).print()
env.execute("Simple PyFlink Job")
