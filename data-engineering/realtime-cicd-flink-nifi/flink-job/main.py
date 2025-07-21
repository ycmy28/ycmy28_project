from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Example: from list (simulate clickstream input)
    input_data = env.from_collection(
        collection=[("user1", "click"), ("user2", "scroll")],
        type_info=Types.TUPLE([Types.STRING(), Types.STRING()])
    )

    result = input_data.map(lambda x: (x[0], x[1].upper()), output_type=Types.TUPLE([Types.STRING(), Types.STRING()]))

    result.print()
    env.execute("local_pyflink_job")

if __name__ == '__main__':
    main()
