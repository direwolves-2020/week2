import local
import child.childmod

def check_imports():
    print(child.childmod.add(1,2))

    print(local.square(16))

if __name__ == "__main__":
    check_imports()