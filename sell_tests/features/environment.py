from behave.fixture import use_fixture_by_tag

from sell_tests.driver_setup.driver_creator import DriverManager
from sell_tests.helpers.fixtures import FIXTURES


def before_feature(context, feature):
    DriverManager.create()
    for tag in feature.tags:
        if tag.startswith("fixture."):
            use_fixture_by_tag(tag, context, FIXTURES)


def after_feature(context, feature):
    DriverManager.quit()
