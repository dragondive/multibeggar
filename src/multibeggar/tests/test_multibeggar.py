import pytest
from multibeggar import Multibeggar


def test_multibeggar():
    # This is a temporary test for the helloworld setup.
    # It can be removed after the setup is completed.
    value = 0.1
    instance = Multibeggar(complexity_tuning_factor=value)
    assert instance.complexity_tuning_factor == pytest.approx(value)
