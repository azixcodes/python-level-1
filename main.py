command = "start"


match command:
    case "start":
        print("starting..")
    case "stop":
        print("stopping..")
    case "end":
        print("ending..")
    case _:
        print("unknow command")