# -*- coding: utf-8 -*-
'''
Created on 2018年6月9日

@author: Administrator
'''

import json

data = {
    "count": "Int",
    "extras": "String or Json",
    "data": {
        "vm_list": [{
            "enable": 1,
            "vmid": "sample string"
        }],
        "enable": 1,
        "name": "sample string",
        "description": "sample string",
        "type": "hour",
        "schema": {
            "backup_clear": 1,
            "timeout_cancel": 1,
            "site": "6a0a707c-45ef-4758-b533-e55adddba8ce",
            "trigger": "sample string",
            "duration": 0,
            "backup_keep": 0,
            "backup_storage": "xxxxxxxxxxxxxx"
        }
    },
    "dbgmsg": "String",
    "success": "1",
}

def from_json_to_str():
    s = json.dumps(data)
    print(type(s))
    print(s)


def from_str_to_json():
    s = json.dumps(data)
    j = json.loads(s)
    print(type(j))
    print(j) 
    
if __name__ == '__main__':
    from_json_to_str()
    from_str_to_json()
    