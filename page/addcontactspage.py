from homework.page.addcontactspage2 import AddcontactsPage2
from homework.page.base_page import BasePage


class AddcontactsPage(BasePage):
    def goto_add_contacts(self):
        self.steps('../page/addcontactspage.yaml')
        return AddcontactsPage2(self.driver)
