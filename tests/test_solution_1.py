import sys
sys.path.insert(1, '../src')

from solution_1 import print_depth


class TestSolution_1:

            def test_dict_depth_of_3_with_5_items(self, capsys):
                    
                test_data={'key1':1,'key2':{'key3':1,'key4':{'key5':4}}}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                        "key1 1\n"
                        "key2 1\n"
                        "key3 2\n"
                        "key4 2\n"
                        "key5 3\n"
                        )
                
                assert captured.err == ""

            def test_dict_depth_of_3_with_7_items(self, capsys):
                    
                test_data={'key1':{'key2':2,'key3':3},'key4':4,'key5':{'key6':{'key7':7}}}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                        "key1 1\n"
                        "key2 2\n"
                        "key3 2\n"
                        "key4 1\n"
                        "key5 1\n"
                        "key6 2\n"
                        "key7 3\n"
                        )
                assert captured.err == ""

            def test_dict_depth_of_4_with_4_items(self, capsys):
                    
                test_data={'key1':{'key2':{'key3':{'key4':4}}}}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                        "key1 1\n"
                        "key2 2\n"
                        "key3 3\n"
                        "key4 4\n"
                        )
                assert captured.err == ""

            def test_dict_depth_of_1_with_3_items(self, capsys):
                    
                test_data={'key1':1,'key2':2,'key3':3}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                        "key1 1\n"
                        "key2 1\n"
                        "key3 1\n"
                        )
                assert captured.err == ""

            def test_dict_depth_of_3_with_3_items(self, capsys):
                    
                test_data={'key1':{'key2':{'key3':3}}}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                        "key1 1\n"
                        "key2 2\n"
                        "key3 3\n"
                        )
                assert captured.err == ""

            def test_dict_depth_of_0_with_0_item(self, capsys):
                    
                test_data = {}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == ""
                assert captured.err == ""

