# coding: UTF-8

import ConfigParser


def config_tt():
    print(dir(ConfigParser.ConfigParser))
    print("=========")

    cfg = ConfigParser.ConfigParser()
    cfg.read("test.cfg")

    nodes = cfg.sections()
    print(nodes)

    for node in nodes:
        print(cfg.options(node))

    for node in cfg.sections():
        print("=== %s ===" % node)
        for opt in cfg.options(node):
            print(opt, cfg.get(node, opt))


def run():
    config_tt()


if __name__ == "__main__":
    run()
    

