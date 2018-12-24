import allure


class TestWang:
    def test_a(self):
        assert 1

    @allure.step("测试登陆的步骤")
    def test_b(self):
        print("\n11111")
        allure.attach("描述1","请输入用户名")
        print("\n22222")
        allure.attach("描述2","请输入密码")
        assert 0