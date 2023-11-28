import json
import time
from elasticsearch import Elasticsearch
from prometheus_client import start_http_server, Gauge
import logging
import logging.handlers
import pymysql
import datetime
import threading

log_set = {
    "filename": "./logs/es_delay.log",
    "maxBytes": 1024 * 1024 * 1024,
    "backupCount": 1
}

client = Elasticsearch("http://11.179.84.79:9200", basic_auth=("elastic", "OPC.test"))
db_conn = pymysql.connect(host="9.223.25.246", user="tcc_read", password="tcc_idc_read2021", database="tcc", charset="utf8")

db_list_conn = pymysql.connect(host="9.223.25.246", user="tcc_read", password="tcc_idc_read2021", database="tcc", charset="utf8")

db_agg_query_cost = Gauge('db_agg_query_cost', 'database aggregation query cost')

db_list_query_cost = Gauge('db_list_query_cost', 'database list query cost')

es_agg_query_cost = Gauge('es_agg_query_cost', 'elasticsearch aggregation query cost', ["idx"])

es_list_query_cost = Gauge('es_list_query_cost', 'elasticsearch list query cost', ["idx"])

sql = "SELECT count(*) FROM tcc.tcc_lead l LEFT JOIN tcc.tcc_customer c ON c.cid = l.cid and c.belongModule = l.belongModule \
WHERE l.belongModule = 7 AND c.belongModule = 7 AND c.status = 0 AND l.status IN (1,3) AND c.follower IN \
('LiuHongQian','MingYuan','ZhaoXiaoHong','LuHang','XiongXiaoJie','XuMiaoJie','HeRong','DingGan','ZhuXiangTao',\
'YaoMaoChao','LuoJiaLin','ZhuJiang','SuDeZhi','YiXiangPool','HeXueXing', 'AnChangPool') AND \
l.createTime >= %s AND l.createTime <= %s;"

list_sql = "SELECT * FROM tcc.tcc_lead l LEFT JOIN tcc.tcc_customer c ON c.cid = l.cid and c.belongModule = l.belongModule \
WHERE l.belongModule = 7 AND c.belongModule = 7 AND c.status = 0 AND l.status IN (1,3) AND c.follower IN \
('LiuHongQian','MingYuan','ZhaoXiaoHong','LuHang','XiongXiaoJie','XuMiaoJie','HeRong','DingGan','ZhuXiangTao',\
'YaoMaoChao','LuoJiaLin','ZhuJiang','SuDeZhi','HeXueXing') AND l.createTime >= %s AND \
l.createTime <= %s ORDER BY l.leadAssignTime DESC, leadId desc limit 0,10"

v1_query = {
    "bool": {
      "filter": [
        {
          "term": {
            "lead_belongModule": 7
          }
        },
        {
          "terms": {
            "lead_status": [
              1,
              3
            ]
          }
        },
        {
          "term": {
            "join_field": "lead_task"
          }
        },
        {
          "range": {
            "lead_createTime": {
              "gte": "",
              "lte": ""
            }
          }
        },
        {
          "has_parent": {
            "parent_type": "customer",
            "query": {
              "bool": {
                "filter": [
                  {
                    "term": {
                      "customer_status": 0
                    }
                  },
                  {
                    "terms": {
                      "customer_follower": [
                        "LiuHongQian",
                        "MingYuan",
                        "ZhaoXiaoHong",
                        "LuHang",
                        "XiongXiaoJie",
                        "XuMiaoJie",
                        "HeRong",
                        "DingGan",
                        "ZhuXiangTao",
                        "YaoMaoChao",
                        "LuoJiaLin",
                        "ZhuJiang",
                        "SuDeZhi",
                        "YiXiangPool",
                        "HeXueXing",
                        "AnChangPool"
                      ]
                    }
                  }
                ]
              }
            }
          }
        }
      ]
    }
  }

v1_list_query = {
    "bool": {
      "filter": [
        {
          "term": {
            "lead_belongModule": 7
          }
        },
        {
          "terms": {
            "lead_status": [
              1,
              3
            ]
          }
        },
        {
          "term": {
            "join_field": "lead_task"
          }
        },
        {
          "range": {
            "lead_createTime": {
              "gte": "",
              "lte": ""
            }
          }
        },
        {
          "has_parent": {
            "parent_type": "customer",
            "query": {
              "bool": {
                "filter": [
                  {
                    "term": {
                      "customer_status": 0
                    }
                  },
                  {
                    "terms": {
                      "customer_follower": [
                        "LiuHongQian",
                        "MingYuan",
                        "ZhaoXiaoHong",
                        "LuHang",
                        "XiongXiaoJie",
                        "XuMiaoJie",
                        "HeRong",
                        "DingGan",
                        "ZhuXiangTao",
                        "YaoMaoChao",
                        "LuoJiaLin",
                        "ZhuJiang",
                        "SuDeZhi",
                        "HeXueXing"
                      ]
                    }
                  }
                ]
              }
            }
          }
        }
      ]
    }
  }

v2_query = {
    "bool": {
      "filter": [
        {
          "term": {
            "lead_belongModule": 7
          }
        },
        {
          "terms": {
            "lead_status": [
              1,
              3
            ]
          }
        },
        {
          "term": {
            "join_field": "lead_task"
          }
        },
        {
          "range": {
            "lead_createTime": {
              "gte": "",
              "lte": ""
            }
          }
        },
        {
          "term": {
            "c_status": 0
          }
        },
        {
          "terms": {
            "c_follower": [
              "LiuHongQian",
              "MingYuan",
              "ZhaoXiaoHong",
              "LuHang",
              "XiongXiaoJie",
              "XuMiaoJie",
              "HeRong",
              "DingGan",
              "ZhuXiangTao",
              "YaoMaoChao",
              "LuoJiaLin",
              "ZhuJiang",
              "SuDeZhi",
              "YiXiangPool",
              "HeXueXing",
              "AnChangPool"
            ]
          }
        }
      ]
    }
}

v2_list_query = {
    "bool": {
      "filter": [
        {
          "term": {
            "lead_belongModule": 7
          }
        },
        {
          "terms": {
            "lead_status": [
              1,
              3
            ]
          }
        },
        {
          "term": {
            "join_field": "lead_task"
          }
        },
        {
          "range": {
            "lead_createTime": {
              "gte": "",
              "lte": ""
            }
          }
        },
        {
          "term": {
            "c_status": 0
          }
        },
        {
          "terms": {
            "c_follower": [
              "LiuHongQian",
              "MingYuan",
              "ZhaoXiaoHong",
              "LuHang",
              "XiongXiaoJie",
              "XuMiaoJie",
              "HeRong",
              "DingGan",
              "ZhuXiangTao",
              "YaoMaoChao",
              "LuoJiaLin",
              "ZhuJiang",
              "SuDeZhi",
              "HeXueXing"
            ]
          }
        }
      ]
    }
  }

sort = [
    {
      "lead_leadAssignTime": "desc"
    },
    {
      "lead_leadId": "desc"
    }
  ]

def build_v1_query(t1, t2):
    range = {
        "gte": t1,
        "lte": t2
    }
    v1_query["bool"]["filter"][3]["range"]["lead_createTime"] = range
    return v1_query

def build_v1_list_query(t1, t2):
    range = {
        "gte": t1,
        "lte": t2
    }
    v1_list_query["bool"]["filter"][3]["range"]["lead_createTime"] = range
    return v1_list_query

def build_v2_query(t1, t2):
    range = {
        "gte": t1,
        "lte": t2
    }
    v2_query["bool"]["filter"][3]["range"]["lead_createTime"] = range
    return v2_query

def build_v2_list_query(t1, t2):
    range = {
        "gte": t1,
        "lte": t2
    }
    v2_list_query["bool"]["filter"][3]["range"]["lead_createTime"] = range
    return v2_list_query

def get_milli_time():
    return int(time.time() * 1000)

def sniff_db_cost(t1, t2):
    with db_conn.cursor() as cursor:
        begin = get_milli_time()
        cursor.execute(sql, (t1, t2))
        result = cursor.fetchall()
        timecost = get_milli_time() - begin
        logging.info("db query result: %s, timecost: %d", result, timecost)
        db_agg_query_cost.set(timecost)

def sniff_db_list_cost(t1, t2):
    with db_list_conn.cursor() as cursor:
        begin = get_milli_time()
        cursor.execute(list_sql, (t1, t2))
        result = cursor.fetchall()
        timecost = get_milli_time() - begin
        logging.info("db list query result: %s, timecost: %d", result, timecost)
        db_list_query_cost.set(timecost)

def sniff_v1_cost(t1, t2):
    query = build_v1_query(t1, t2)
    begin = get_milli_time()
    result = client.count(index="idc_tcc_lead_idx", query=query)
    timecost = get_milli_time() - begin
    logging.info("es v1 query result: %s, timecost: %d", result, timecost)
    es_agg_query_cost.labels("v1").set(timecost)

def sniff_v1_list_cost(t1, t2):
    query = build_v1_list_query(t1, t2)
    begin = get_milli_time()
    result = client.search(index="idc_tcc_lead_idx", query=query, sort=sort, source=False, from_=0, size=10)
    timecost = get_milli_time() - begin
    logging.info("es v1 query result: %s, timecost: %d", result, timecost)
    es_list_query_cost.labels("v1").set(timecost)

def sniff_v2_cost(t1, t2):
    query = build_v2_query(t1, t2)
    begin = get_milli_time()
    result = client.count(index="idc_tcc_lead_idx", query=query)
    timecost = get_milli_time() - begin
    logging.info("es v2 query result: %s, timecost: %d", result, timecost)
    es_agg_query_cost.labels("v2").set(timecost)

def sniff_v2_list_cost(t1, t2):
    query = build_v2_list_query(t1, t2)
    begin = get_milli_time()
    result = client.search(index="idc_tcc_lead_idx", query=query, sort=sort, source=False, from_=0, size=10)
    timecost = get_milli_time() - begin
    logging.info("es v2 query result: %s, timecost: %d", result, timecost)
    es_list_query_cost.labels("v2").set(timecost)

def init_log():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    h = logging.handlers.RotatingFileHandler(**log_set)
    h.setFormatter(fmt)
    logger.addHandler(h)


if __name__ == "__main__":
    init_log()
    start_http_server(9600)
    while True:
        start_time = datetime.datetime.now()

        t1 = start_time - datetime.timedelta(days=30)
        t2 = start_time

        t1 = t1.strftime("%Y-%m-%d %H:%M:%S")
        t2 = t2.strftime("%Y-%m-%d %H:%M:%S")

        logging.info("sniff start, t1: %s, t2: %s", t1, t2)

        db_sniff = threading.Thread(target=sniff_db_cost, args=(t1, t2))
        v1_sniff = threading.Thread(target=sniff_v1_cost, args=(t1, t2))
        v2_sniff = threading.Thread(target=sniff_v2_cost, args=(t1, t2))

        db_list_sniff = threading.Thread(target=sniff_db_list_cost, args=(t1, t2))
        v1_list_sniff = threading.Thread(target=sniff_v1_list_cost, args=(t1, t2))
        v2_list_sniff = threading.Thread(target=sniff_v2_list_cost, args =(t1, t2))

        threads = [db_sniff, v1_sniff, v2_sniff, db_list_sniff, v1_list_sniff, v2_list_sniff]
        for t in threads:
            t.start()

        for t in threads:
            t.join()
        logging.info("sniff end")

        diff = datetime.datetime.now() - start_time
        n = 10 - diff.total_seconds()
        if n > 0:
            time.sleep(n)
