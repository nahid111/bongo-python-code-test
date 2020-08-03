import io
import unittest
from unittest.mock import patch
import solution_1
import solution_2
import solution_3


class TestSolutions(unittest.TestCase):

    # =====================================================================================
    #                       Testing solution to the question 1
    # =====================================================================================
    def test_solution_1(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        expected_output = 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n'

        with patch('sys.stdout', new=io.StringIO()) as captured_std:
            solution_1.print_depth(a)
            self.assertEqual(captured_std.getvalue(), expected_output)

        with patch('sys.stdout', new=io.StringIO()) as captured_std:
            solution_1.print_depth([1, 2, 'foobar'])
            self.assertEqual(captured_std.getvalue(), '')

    # =====================================================================================
    #                       Testing solution to the question 2
    # =====================================================================================
    def test_solution_2(self):
        person_a = solution_2.Person("User", "1", None)
        person_b = solution_2.Person("User", "2", person_a)
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b
                }
            }
        }
        expected_output = 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser: 3\nfirst_name: 4\nlast_name: 4\nfather: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\n'

        with patch('sys.stdout', new=io.StringIO()) as captured_std:
            solution_2.print_depth(a)
            self.assertEqual(captured_std.getvalue(), expected_output)

        with patch('sys.stdout', new=io.StringIO()) as captured_std:
            solution_2.print_depth([1, 2, 'foobar'])
            self.assertEqual(captured_std.getvalue(), '')

    # =====================================================================================
    #                       Testing solution to the question 3
    # =====================================================================================
    def test_solution_3(self):
        # Create the Tree nodes
        n1 = solution_3.Node(1)
        n2 = solution_3.Node(2)
        n3 = solution_3.Node(3)
        n4 = solution_3.Node(4)
        n5 = solution_3.Node(5)
        n6 = solution_3.Node(6)
        n7 = solution_3.Node(7)
        n8 = solution_3.Node(8)
        n9 = solution_3.Node(9)
        # connect the nodes
        n2.parent = n1
        n3.parent = n1
        n4.parent = n2
        n5.parent = n2
        n6.parent = n3
        n7.parent = n3
        n8.parent = n4
        n9.parent = n4

        self.assertEqual(solution_3.lca(n6, n7), 3)
        self.assertEqual(solution_3.lca(n3, n7), 3)
        self.assertEqual(solution_3.lca(n2, n8), 2)
        self.assertEqual(solution_3.lca(n4, n5), 2)
        self.assertEqual(solution_3.lca(n7, n8), 1)
        self.assertEqual(solution_3.lca(n4, n6), 1)
        self.assertEqual(solution_3.lca(n4, n3), 1)
        self.assertEqual(solution_3.lca(n4, n1), 1)
        self.assertEqual(solution_3.lca(404, n1), None)


if __name__ == '__main__':
    unittest.main()
