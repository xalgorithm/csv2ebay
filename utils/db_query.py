import pymysql
import utils.config as cf
cfg = cf.read_config()
con = pymysql.connect(cf.cfg.host, cf.cfg.username, cf.cfg.password, cf.cfg.db)