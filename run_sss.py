"""
    测试套件：
        按照需求组合被执行的测试函数


    自动化测试执行顺序：
        增 --> 改 --> 查 --> 删

    补充说明：
        关于测试套件的组织，接口业务测试中，需要保证测试套件中接口的执行顺序：
            合法实现：suite.addTest(类名（方法名）) 逐一添加
            非法实现：suite.addTest(unittest.makeSuite(类名)) 虽然可以一次性添加多个测试数据，但是无法保证执行顺序

"""
# 1.导包
import unittest
# 2.实例化套件对象。组织被执行的测试函数
import app
from case.Test_iHRM_Emp import Test_Emp
from case.Test_iHRM_Login import Test_login
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_login("test_login_success"))  # 组织登陆成功的测试函数
suite.addTest(Test_Emp("test_add"))  # 组织员工新增的测试函数
suite.addTest(Test_Emp("test_updata")) # 组织员工修改的测试函数
suite.addTest(Test_Emp("test_get")) # 组织员工查询的测试函数
suite.addTest(Test_Emp("test_delete")) # 组织员工删除的测试函数

# 3.执行套件。生成测试报告


with open(app.PRO_PATH + "/report/report.html", "wb") as f:
    # 创建 HTMLTestRunner 对象
    runner = HTMLTestRunner(f, title="人力资源管理系统",description="测试了员工模块的增删改查相关接口")
    # 执行
    runner.run(suite)