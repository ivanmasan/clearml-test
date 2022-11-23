from clearml import Task


def main():
    task = Task.current_task()

    config_file_yaml = task.connect_configuration(
        name="yaml file", configuration='./conf/config.yaml'
    )
    print(config_file_yaml)

    with open(config_file_yaml, 'r') as f:
        print(f.readlines())

    python_file = task.connect_configuration(
        name="py file", configuration='./conf/script.py'
    )
    print(python_file)

    with open(python_file, 'r') as f:
        print(f.readlines())

    from conf.script import p
    p()


if __name__ == "__main__":
    main()
