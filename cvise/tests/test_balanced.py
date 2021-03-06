import os
import tempfile
import unittest

from cvise.passes.abstract import PassResult
from cvise.passes.balanced import BalancedPass


class BalancedParensTestCase(unittest.TestCase):
    def setUp(self):
        self.pass_ = BalancedPass('parens')

    def test_parens_no_match(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This is a simple test!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a simple test!\n')

    def test_parens_simple(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This is a (simple) test!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a  test!\n')

    def test_parens_nested_outer(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This !\n')

    def test_parens_nested_inner(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        # Transform failed
        state = self.pass_.advance(tmp_file.name, state)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This (is a  test)!\n')


class BalancedParensOnlyTestCase(unittest.TestCase):
    def setUp(self):
        self.pass_ = BalancedPass('parens-only')

    def test_parens_no_match(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This is a simple test!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a simple test!\n')

    def test_parens_simple(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This is a (simple) test!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a simple test!\n')

    def test_parens_nested_outer(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a (simple) test!\n')

    def test_parens_nested_inner(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        # Transform failed
        state = self.pass_.advance(tmp_file.name, state)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This (is a simple test)!\n')

    def test_parens_nested_both(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)
        state = self.pass_.advance_on_success(tmp_file.name, state)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a simple test!\n')

    def test_parens_nested_all(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('(This) (is a (((more)) complex) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (result, state) = self.pass_.transform(tmp_file.name, state, None)

        iteration = 0

        while result == PassResult.OK and iteration < 7:
            state = self.pass_.advance_on_success(tmp_file.name, state)
            (result, state) = self.pass_.transform(tmp_file.name, state, None)
            iteration += 1

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(iteration, 5)
        self.assertEqual(variant, 'This is a more complex test!\n')

    def test_parens_nested_no_success(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('(This) (is a (((more)) complex) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (result, state) = self.pass_.transform(tmp_file.name, state, None)

        iteration = 0

        while result == PassResult.OK and iteration < 7:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                tmp_file.write('(This) (is a (((more)) complex) test)!\n')

            state = self.pass_.advance(tmp_file.name, state)
            (result, state) = self.pass_.transform(tmp_file.name, state, None)
            iteration += 1

        os.unlink(tmp_file.name)

        self.assertEqual(iteration, 5)


class BalancedParensInsideTestCase(unittest.TestCase):
    def setUp(self):
        self.pass_ = BalancedPass('parens-inside')

    def test_parens_no_match(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This is a simple test!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a simple test!\n')

    def test_parens_simple(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This is a (simple) test!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This is a () test!\n')

    def test_parens_nested_outer(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This ()!\n')

    def test_parens_nested_inner(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        # Transform failed
        state = self.pass_.advance(tmp_file.name, state)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This (is a () test)!\n')

    def test_parens_nested_both(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('This (is a (simple) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)
        state = self.pass_.advance_on_success(tmp_file.name, state)
        (_, state) = self.pass_.transform(tmp_file.name, state, None)

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(variant, 'This ()!\n')

    def test_parens_nested_all(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('(This) (is a (((more)) complex) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (result, state) = self.pass_.transform(tmp_file.name, state, None)

        iteration = 0

        while result == PassResult.OK and iteration < 4:
            state = self.pass_.advance_on_success(tmp_file.name, state)
            (result, state) = self.pass_.transform(tmp_file.name, state, None)
            iteration += 1

        with open(tmp_file.name) as variant_file:
            variant = variant_file.read()

        os.unlink(tmp_file.name)

        self.assertEqual(iteration, 2)
        self.assertEqual(variant, '() ()!\n')

    def test_parens_nested_no_success(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
            tmp_file.write('(This) (is a (((more)) complex) test)!\n')

        state = self.pass_.new(tmp_file.name)
        (result, state) = self.pass_.transform(tmp_file.name, state, None)

        iteration = 0

        while result == PassResult.OK and iteration < 7:
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
                tmp_file.write('(This) (is a (((more)) complex) test)!\n')

            state = self.pass_.advance(tmp_file.name, state)
            (result, state) = self.pass_.transform(tmp_file.name, state, None)
            iteration += 1

        os.unlink(tmp_file.name)

        self.assertEqual(iteration, 5)
