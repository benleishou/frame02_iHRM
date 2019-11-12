"""
    测试员工模块的增删改查实现

"""
# 1.导包
import logging
import unittest
import requests

# 2.创建测试类
import app
from api.EmpAPI import EmpCRUD


class Test_Emp(unittest.TestCase):
    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 4.资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5.测试函数 1：增
    # 直接执行该测试函数失败，为什么？
    # 原因：1.先执行登录操作  2.还需要提交银行卡（token）
    def test_add(self):

        logging.info("新增员工信息")

        # 1.请求业务
        response = self.emp_obj.add(self.session,
                                    username="宇宙大老爷",
                                    mobile="13438888843")
        # 2.断言业务
        print("员工新增响应结果：", response.json())
        # 员工新增响应结果： {'success': True, 'code': 10000, 'message': '操作成功！',
        # 'data': {'id': '1193817909516128256'}}
        # 提取 id
        id = response.json().get("data").get("id")
        app.USER_ID = id
        print("新增员工的ID：", id)

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 5.测试函数 2：改
    def test_updata(self):

        logging.warning("修改员工信息")

        # 1.请求业务
        response = self.emp_obj.updata(self.session, app.USER_ID, "陈翔六个蛋")
        print("修改后的员工信息：", response.json())
        # 2.断言业务

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 5.测试函数 3：查
    def test_get(self):

        logging.info("查看员工信息")

        # 1.请求业务
        response = self.emp_obj.get(self.session, app.USER_ID)
        print("查看到的员工信息：", response.json())
        # 2.断言业务

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 5.测试函数 4：删
    def test_delete(self):

        logging.warning("删除员工信息")

        # 1.请求业务
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print("删除成功后的数据：", response.json())
        # 2.断言业务

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

