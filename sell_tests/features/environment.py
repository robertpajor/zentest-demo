from behave.fixture import use_fixture_by_tag

from sell_tests.configurations.driver_manager import DriverManager
from sell_tests.helpers.fixtures import FIXTURES


def before_feature(context, feature):
    DriverManager.create()
    for tag in feature.tags:
        if tag.startswith("fixture."):
            use_fixture_by_tag(tag, context, FIXTURES)


def after_feature(context, feature):
    # for tag in feature.tags:
    #     if tag.startswith("post."):
    #         use_fixture_by_tag(tag, context, POST_ACTIONS)
    DriverManager.quit()
