import sys
sys.path.insert(1, '../src')
import pytest
from solution_2 import print_depth, Person

class TestSolution_2:
            
            @pytest.fixture
            def person_a(self):
                person_a = Person('User', '1',None)
                return person_a.__dict__

            @pytest.fixture
            def person_b(self,person_a):
                person_b = Person('User', '2', person_a)
                return person_b.__dict__ 
            
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

            def test_dict_depth_of_5_with_nested_class_objects(self, capsys,person_b):
     
                test_data={'key1':1,'key2':{'key3':1,'key4':{'key5':4,'user': person_b}}}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                        "key1 1\n"
                        "key2 1\n"
                        "key3 2\n"
                        "key4 2\n"
                        "key5 3\n"
                        "user: 3\n"
                        "first_name: 4\n"
                        "last_name: 4\n"
                        "father: 4\n"
                        "first_name: 5\n"
                        "last_name: 5\n"
                        "father: 5\n"
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


            def test_dict_depth_of_3_with_class_object(self, capsys,person_a):
                    
                test_data={'key1':1,'key6':person_a,'key2':{'key3':1,'key4':{'key5':4,'user': 5}}}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (          
                    "key1 1\n"
                    "key6 1\n"
                    "first_name: 2\n"
                    "last_name: 2\n"
                    "father: 2\n"
                    "key2 1\n"
                    "key3 2\n"
                    "key4 2\n"
                    "key5 3\n"
                    "user: 3\n"
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


            def test_dict_depth_of_2_with_class_object(self, capsys, person_a):
                
                test_data = {'user':person_a}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == (
                    "user: 1\n"
                    "first_name: 2\n"
                    "last_name: 2\n"
                    "father: 2\n"
                    )
                assert captured.err == ""

            def test_dict_depth_of_0_with_0_item(self, capsys):
                    
                test_data = {}
                
                print_depth(test_data)
                sys.stderr.write("")
                captured=capsys.readouterr()
                assert captured.out == ""
                assert captured.err == ""

                        
                        
