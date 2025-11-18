def show_args(title, *args, **kwargs):
    print(f"{title} args '{args}' kwargs '{kwargs}'")

show_args("nothing")
show_args("one unnamed argument", 1)
show_args("one named argument", second=2)
show_args("one for each", 3, fourth=4)
