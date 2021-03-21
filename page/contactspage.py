from homework.page.addcontactspage import AddcontactsPage
from homework.page.base_page import BasePage


class ContactsPage(BasePage):
    def goto_addcontacts(self):
        self.steps('../page/contactspage.yaml')
        return AddcontactsPage(self.driver)
