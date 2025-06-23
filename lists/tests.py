from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_renders_homepage_input_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form method="POST">')


    def test_render_input_form(self):
        response = self.client.get("/")
        self.assertContains(response, '<form method="POST">')
        self.assertContains(response, '<input name="item_text"')
        self.assertContains(response, '<input name="item_text'"")

    def test_can_save_a_POST_request(self):
        response = self.client.post("/", data={"item_text" : "A new list item"})
        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, "home.html")

