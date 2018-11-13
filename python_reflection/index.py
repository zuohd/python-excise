# import common

def run():
    inp = input("input calling function name:")
    module_name, fuc_name = inp.split('/')
    module = __import__(module_name)
    if hasattr(module, fuc_name):
        func = getattr(module, fuc_name)
        func()
    else:
        print('404')


if __name__ == '__main__':
    run()
