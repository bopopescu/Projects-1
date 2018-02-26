# -*- coding: utf-8 -*-

tg_key = "444285376:AAFgmYTILr-EW8uk3VIgjr1scQKtEmNNgZM"  # telegram bot api key

zbx_tg_prefix = "zbxtg"  # variable for separating text from script info
zbx_tg_tmp_dir = "/tmp/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False

zbx_server = "http://192.168.192.109/zabbix"  # zabbix server full url
zbx_api_user = "admin"
zbx_api_pass = "zabbix"
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore

proxy_to_zbx = None
proxy_to_tg = None

#proxy_to_zbx = "proxy.local:3128"
#proxy_to_tg = "proxy.local:3128"

emoji_map = {
    "ok": "✅",
    "problem": "❗",
    "info": "ℹ️",
    "warning": "⚠️",
    "disaster": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}