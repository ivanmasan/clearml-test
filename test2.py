from clearml import Task


def main():
    task = Task.current_task()
    print(task)
    if task is None:
        print("Here")
        task = Task.init(
            project_name="Testing",
            task_name="Test run 9"
        )
    print("Here")

    task.close()


if __name__ == "__main__":
    main()
