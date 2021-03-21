from homework.page.information_page import Information


class TestAddcontacts:

    def test_add_contacts(self):
        name = 'aaa17'
        phonenum = '18918290017'
        Information().start().goto_contacts().goto_addcontacts().goto_add_contacts().goto_add(name, phonenum)
