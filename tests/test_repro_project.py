#!/usr/bin/env python

"""Tests for `repro_project` package."""

import pytest

from repro_project.repro_project import count_gc


@pytest.fixture
def seq():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return 'acgttc'
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_count_gc(seq):
    """Sample pytest test function with the pytest fixture as an argument."""
    assert count_gc(seq) == 0.5

    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
