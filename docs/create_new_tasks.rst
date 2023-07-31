Create new tasks
================


Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample tasks list
^^^^^^^^^^^^^^^^^

.. code-block:: console

    User = get_user_model()

    ToDoList.objects.create(
        title = "Test Todo 1",
        owner = User.objects.first(),
        # owner = User.objects.get(username="mary"),
    )
    ToDoItem.objects.create(
        title = "Todo Item #1",
        description="Todo Item description",
        # due_date="" # default=one_week_hence
        todo_list = ToDoList.objects.get(title="Test Todo 1"),
    )

    ToDoList.objects.create(
        title = "Learn Python,
        owner = User.objects.first(),
        owner = User.objects.get(username="mary"),
    )
    ToDoList.objects.create(
        title = "Learn Django",
        owner = User.objects.first(),
        owner = User.objects.get(username="john"),
    )
    ToDoList.objects.create(
        title = "Learn to play guitar",
        owner = User.objects.first(),
        owner = User.objects.get(username="susan"),
    )


    ToDoList.objects.create(
        title = "My Shopping List",
        owner = User.objects.first(),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #1",
        description="Loaf of wheat bread",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #2",
        description="Gallon of milk",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #3",
        description="A dozen eggs",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #4",
        description="three tomatoes",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #5",
        description="One pound of coffee",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #6",
        description="Cat food",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #7",
        description="toilet paper",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #8",
        description="head of lettuce",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #9",
        description="Bag of string cheese",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )
    ToDoItem.objects.create(
        title = "Shopping List Item #10",
        description="Jar of peanut butter",
        todo_list = ToDoList.objects.get(title="My Shopping List"),
    )

    ToDoList.objects.create(
        title = "Grocery List",
        owner = User.objects.first(),
    )
    ToDoItem.objects.create(
        title = "Loaf of wheat bread",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "Gallon of milk",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "A dozen eggs",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "three tomatoes",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "One pound of coffee",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "Cat food",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "toilet paper",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "head of lettuce",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "Bag of string cheese",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
    ToDoItem.objects.create(
        title = "Jar of peanut butter",
        description="",
        todo_list = ToDoList.objects.get(title="Grocery List"),
    )
