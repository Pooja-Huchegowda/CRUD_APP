import pytest
from django.urls import reverse, resolve
from products.views import product_list, product_create, product_update, product_delete

# Test if the URLs resolve to the correct views
@pytest.mark.parametrize('url, view, kwargs', [
    ('product_list', product_list, {}),
    ('product_create', product_create, {}),
    ('product_update', product_update, {'pk': 1}),
    ('product_delete', product_delete, {'pk': 1}),
])
def test_url_resolves_to_correct_view(url, view, kwargs):
    # Use reverse() to get the URL from the name, and provide necessary arguments
    url_resolved = reverse(url, kwargs=kwargs)

    # Use resolve() to get the view associated with the URL
    resolved_view = resolve(url_resolved)

    # Check if the resolved view matches the expected view
    assert resolved_view.view_name == url
    assert resolved_view.func == view
