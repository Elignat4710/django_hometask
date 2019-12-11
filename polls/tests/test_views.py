from django.test import TestCase
from django.urls import reverse
from polls.models import (
    Company, Manager, Work
    )


class CompanyListViewTest(TestCase):
    def setUp(self):
        Company.objects.create(
            name='company_1'
        )

    def test_company_list(self):
        response = self.client.get(reverse('companies_list'))
        self.assertTrue(response.context['companies'])


class ManagerListViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        Manager.objects.create(
            name='manager_1',
            com_name=self.company
        )

    def test_manager_list(self):
        response = self.client.get(reverse(
            'manager_list',
            kwargs={'pk': self.company.id}))
        self.assertTrue(response.context['managers'])


class CompanyDetailViewtest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
    
    def test_company_detail(self):
        response = self.client.get(reverse(
            'company_details',
            kwargs={'pk': self.company.id}))
        self.assertEqual(response.status_code, 200)


class WorkCreateViewTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name='company_1'
        )
        self.work = Work.objects.create(
            name='work',
            com_name=self.company
        )

    def test_work_create(self):
        work_dict = {
            'name': 'work_1',
            'com_name': self.company
        }
        response = self.client.post('work_create', work_dict, kwargs={'pk': self.company.id})
        print(response.status_code)
        work = Work.objects.all()
        # print(work)
        self.assertEqual(work.name, 'work')
