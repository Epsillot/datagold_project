from django.urls import reverse

def test_login_page_url():
    assert reverse('login') == '/login/'

def test_dashboard_url():
    assert reverse('index') == '/dashboard/'


def test_admin_url():
    assert reverse('admin:index') == '/admin/'

def test_collecte_api_url():
    assert reverse('collecte') == '/api/collecte/'

def test_logout_url():
    assert reverse('logout') == '/logout/'
