#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
# coding:utf8
# lucy 2017-5-10
import requests
import json
import yaml
from collections import defaultdict


class Zabbix(object):
    def __init__(self):
        self.header = {'Content-Type': 'application/json-rpc'}
        # self.zabbix_config = yaml.load(open('zabbix_target.yaml'))
        # self.api_url = self.zabbix_config['api_url']
        # self.username = self.zabbix_config['user']
        # self.passwd = self.zabbix_config['passwd']
        # self.hostid_result_mapping = {}
        # self.info_chosen = {
        #     '/nginx': {
        #         'name': self.zabbix_config['item']['name'].keys()
        #     },
        #     '/php': {
        #         'key_': self.zabbix_config['item']['key_'].keys(),
        #     }
        # }
        # self.para_dic = {
        #     'host.get': {
        #         'output': ['hostid', 'host', 'name'],
        #         'filter': {
        #             'name': self.zabbix_config['hosts']
        #         }
        #     },
        # }

        def auth():
            '''
            Return Auth_token
            '''
            data = json.dumps({
                'jsonrpc': '2.0',
                'method': 'user.login',
                # 'params': {'user': self.username, 'password': self.passwd},
                'id': 1,
            })
            result_dic = requests.post(self.api_url, data=data, headers=self.header).content
            try:
                result_dic = json.loads(result_dic)
            except ValueError as e:
                print
                e, result_dic
                exit()
            return result_dic['result']

        # self.auth = auth()

    def item_get(self, want):
        if not self.hostid_result_mapping:
            self.getHost()
        if want not in self.info_chosen:
            print
            'Error! check what you want!'

        param = {
            'jsonrpc': '2.0',
            'method': 'item.get',
            'params': {
                'output': 'extend',
                'filter': {
                    'hostid': self.hostid_result_mapping.keys(),
                }
            },
            'auth': self.auth,
            'id': 1,
        }
        # 根据指令, 筛选需要的key
        filter_key, filter_list = self.info_chosen[want].items()[0]
        param['params']['filter'].update({filter_key: filter_list})
        data = json.dumps(param)
        result_dic = json.loads(requests.post(self.api_url, data=data, headers=self.header).content)
        # key 或者 name
        for item_name_or_key in self.info_chosen[want]:
            for item_info in result_dic['result']:
                self.hostid_result_mapping[item_info['hostid']]['items'][item_info['itemid']] = {
                    'info_name': item_info[item_name_or_key]  # 根据 key_ 或者 name字段, 取出名字
                }

            # 因为 item_name_or_key 只有一个, 要么name, 要么key_, 所以可以直接返回
            return self.his_get(item_name_or_key)

    def his_get(self, want):
        format_dict = defaultdict(dict)
        for hostid in self.hostid_result_mapping:
            for item_dicts_id in self.hostid_result_mapping[hostid]['items']:
                data = json.dumps({
                    'jsonrpc': '2.0',
                    'method': 'history.get',
                    'params': {
                        "limit": 1,
                        "sortorder": "DESC",
                        "sortfield": "clock",
                        'output': 'extend',
                        'itemids': item_dicts_id
                    },
                    'auth': self.auth,
                    'id': 1,
                })
                result_dic = json.loads(requests.post(self.api_url, data=data, headers=self.header).content)
                if result_dic['result']:
                    key_name = self.hostid_result_mapping[hostid]['items'][item_dicts_id]['info_name']
                    if key_name in self.zabbix_config['item'][want]:
                        format_dict[self.hostid_result_mapping[hostid]['name']].update({
                            # 名字转换
                            self.zabbix_config['item'][want][key_name]: result_dic['result'][0]['value']
                        })

        # 格式化打印
        message_list = []
        for host in format_dict:
            message = 'Host_name: %s\n' % host
            for item, value in format_dict[host].iteritems():
                message += '%s : %s\n' % (item, value)
            message_list.append(message)
        return '\n'.join(message_list)

    def getHost(self):
        data = json.dumps({
            'jsonrpc': '2.0',
            'method': 'host.get',
            'params': self.para_dic['host.get'],
            'auth': self.auth,
            'id': 1,
        })
        result_dic = json.loads(requests.post(self.api_url, data=data, headers=self.header).content)
        for item in result_dic['result']:
            self.hostid_result_mapping[item['hostid']] = {
                'name': item['name'],
                'items': {}
            }


if __name__ == '__main__':
    z = Zabbix()
    z.item_get('/nginx')