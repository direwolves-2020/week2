import local
import child.childmod as ch

def check_imports():
    print(ch.add(1,2))

    print(local.sqrt(16))

if __name__ == "__main__":
    check_imports()