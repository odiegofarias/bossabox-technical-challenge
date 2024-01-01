from django.test import TestCase
from django.urls import reverse, resolve
from tool import views
from tool.models import Tool, Tag


class ToolHomeViewTest(TestCase):
    def test_se_tools_url_retorna_200(self):
        url = reverse('get_tools')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_se_tools_esta_usando_view_correta(self):
        view = resolve(reverse('get_tools'))


        self.assertEqual(view.func, views.get_tools)

    def test_retorna_tool_corretamente_na_solicitacao_get(self):
        url = reverse('get_tools')

        Tag.objects.create(name='Django')

        test_tool = Tool.objects.create(
            title='test',
            link='https://github.com',
            description='test descrição',
        )

        tags = Tag.objects.all()
        test_tool.tags.set(tags)

        test_tool.save()

        response = self.client.get(url)

        self.assertEqual(response.json(), [
            {
                'id': 1,
                'title': 'test',
                'link': 'https://github.com',
                'description': 'test descrição',
                'tags': ['Django']
            }
            ]
        )