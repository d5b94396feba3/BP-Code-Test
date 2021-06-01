import sys
sys.path.insert(1, '../src')
import pytest
from solution_3 import lca, Node

class TestSolution_3:
            
            @pytest.fixture
            def tree(self):
                tree = Node(1) 
                tree.left_node = Node(2) 
                tree.right_node = Node(3) 
                tree.left_node.left_node = Node(4) 
                tree.left_node.right_node = Node(5)
                tree.left_node.left_node.left_node=Node(8)
                tree.left_node.left_node.right_node=Node(9)
                tree.right_node.left_node = Node(6) 
                tree.right_node.right_node = Node(7) 
                return tree

            def test_node_3_and_node_7(self, capsys,tree):
                
                print(lca(tree, 3,7).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "3\n"
                assert captured.err == ""

            def test_node_3_and_node_3(self, capsys,tree):
                
                print(lca(tree, 3,3).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "3\n"
                assert captured.err == ""
            
            
            def test_node_8_and_node_9(self, capsys,tree):

                print(lca(tree, 8,9).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "4\n"
                assert captured.err == ""

            def test_node_4_and_node_6(self, capsys,tree):

                print(lca(tree, 4,6).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "1\n"
                assert captured.err == ""

            def test_node_2_and_node_9(self, capsys,tree):

                print(lca(tree, 2,9).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "2\n"
                assert captured.err == ""
     
            def test_node_7_and_node_7(self, capsys,tree):

                print(lca(tree, 7,7).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "7\n"
                assert captured.err == ""

            def test_node_6_and_node_7(self, capsys,tree):

                print(lca(tree, 6,7).value)
                
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == "3\n"
                assert captured.err == ""
   




