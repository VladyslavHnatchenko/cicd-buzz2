import unittest
import pytest
from buzz import generator


def test_sample_single_word():
    li = ('foo', 'bar', 'foobar')
    word = generator.sample(li)
    assert word in li


def test_sample_multiple_words():
    li = ('foo', 'bar', 'foobar')
    words = generator.sample(li, 2)
    assert len(words) == 2
    assert words[0] in li
    assert words[1] in li
    assert words[0] is not words[1]


def test_generate_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
