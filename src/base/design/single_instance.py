# coding: UTF-8

class Manager:

    __instance = None

    def __init__(self): pass

    @staticmethod
    def instance():
        if Manager.__instance:
            return Manager.__instance
        else:
            Manager.__instance = Manager()
            return Manager.__instance


def run():
    mgr1 = Manager.instance()
    mgr2 = Manager.instance()
    print(mgr1, mgr2)


if __name__ == "__main__":
    run()
