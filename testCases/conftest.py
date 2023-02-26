from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


###################### Pytest HTML report ##################
# it is a hook for adding environment info into HTML report

def pytest_configure(config):
    config._metadata['Project Name'] = 'NopCommerceApp'
    config._metadata['Tester'] = 'Rajnandan'
    config._metadata['Module Name'] = 'Customer'


# it is Hook for deleting/modifying environment info into Html report

@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("Python home", None)
    metadata.pop('plugin', None)
