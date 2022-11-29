from clearml import Task


def main():
    task = Task.current_task()
    if task is None:
        task = Task.init(
            project_name="AIhub/Instance",
            task_name="Test run 4"
        )

    config_file_yaml = task.connect_configuration(
        name="config", configuration='./conf/config.yaml'
    )
    print(config_file_yaml)

    with open(config_file_yaml, 'r') as f:
        print(f.readlines())

    python_file = task.connect_configuration(
        name="augmentations", configuration='./conf/augmentation.py', description=""
    )
    print(python_file)

    with open(python_file, 'r') as f:
        print(f.readlines())

    task.upload_artifact(
        name='output',
        artifact_object='./R22.pkl'
    )

    o = task.connect(
        mutable={'test_a': True, 'test_b': False},
        name='bool'
    )
    print(o)

    task.close()


if __name__ == "__main__":
    main()
