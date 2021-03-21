from homework.page.base_page import BasePage


class AddcontactsPage2(BasePage):
    def goto_add(self, name, phonenum):
        self.params['name'] = name
        self.params['phonenum'] = phonenum
        self.steps('../page/addcontactspage2.yaml')
