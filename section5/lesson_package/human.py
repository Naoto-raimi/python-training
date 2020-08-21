def sing():
    return "Sing!!"

def cry():
    return "Cry!!"

# importされると平文でprint("main")をかくと実行されてしまうので，
# mainで呼ばれた時だけ実行する
if __name__ == "__main__":
    print("main")
