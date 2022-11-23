from clearml import Task


def main():
    task = Task.current_task()

    config_file_yaml = task.connect_configuration(
        name="yaml file", configuration='/conf/config.yaml'
    )

    print(config_file_yaml)


if __name__ == "__main__":
    main()
