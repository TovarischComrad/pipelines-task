from pipelines.tasks import *
import pytest
import os
import sqlite3

connect = 'database.db'
table_name = 'table_for_tests'
test_data = 'tests/test_data.csv'
result = 'tests/test_output'


def test_load():
    task = LoadFile(table_name, test_data)
    task.run()
    cursor = sqlite3.connect(connect).cursor()
    cursor.execute("SELECT COUNT(*) FROM " + table_name)
    assert cursor.fetchone()[0] == 2
    cursor.close()
    clean()


def test_export():
    LoadFile(table_name, test_data).run()
    CopyToFile(table_name, result).run()
    if os.path.isfile(result + '.csv'):
        with open(result + '.csv', 'r') as check_file:
            reader = csv.reader(check_file)
            assert len(list(reader)) - 1 == 2
        clean()
    else:
        pytest.fail("File not found")


def clean():
    RunSQL('DROP TABLE ' + table_name, connect).run()
    if os.path.isfile(result + '.csv'):
        os.remove(result + '.csv')
        os.remove(connect)
