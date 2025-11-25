import sys
import pytest

sys.path.insert(0, 'src')

from sunbears.dataframe import DataFrame

def test_persist_load_single_row_single_column(tmp_path):
    # Create a DataFrame
    original = DataFrame(["A"], [int], [(1,)])
    
    # Export the DataFrame
    file_path = tmp_path / "exported"
    original.persist_to_disk(file_path)

    # Import the DataFrame
    new_df = DataFrame()
    new_df.load_from_disk(file_path)

    # Original and the new DataFrame must be the same
    assert original.column_names == new_df.column_names
    assert original.column_types == new_df.column_types
    assert original.rows == new_df.rows

def test_persist_load_single_row_multiple_columns(tmp_path):
    # Create a DataFrame
    original = DataFrame(["A", "B", "C"], [int, float, str], [(1, 1.5, "A")])
    
    # Export the DataFrame
    file_path = tmp_path / "exported"
    original.persist_to_disk(file_path)

    # Import the DataFrame
    new_df = DataFrame()
    new_df.load_from_disk(file_path)

    print(original)

    print(new_df.column_names)
    print(new_df.column_types)
    print(new_df.rows)

    print(new_df)

    # Original and the new DataFrame must be the same
    assert original.column_names == new_df.column_names
    assert original.column_types == new_df.column_types
    assert original.rows == new_df.rows

def test_persist_load_multiple_rows_single_column(tmp_path):
    # Create a DataFrame
    original = DataFrame(["A"], [float], [
        (1.5,),
        (1.5,),
        (2.5,),
        (1.0,),
        (-1.0,)])
    
    # Export the DataFrame
    file_path = tmp_path / "exported"
    original.persist_to_disk(file_path)

    # Import the DataFrame
    new_df = DataFrame()
    new_df.load_from_disk(file_path)

    # Original and the new DataFrame must be the same
    assert original.column_names == new_df.column_names
    assert original.column_types == new_df.column_types
    assert original.rows == new_df.rows

def test_persist_load_multiple_rows_multiple_columns(tmp_path):
    # Create a DataFrame
    original = DataFrame(["A", "B", "C"], [int, float, str], [
        (1, 1.5, "A"),
        (2, 1.5, "B"),
        (3, 2.5, "C"),
        (4, 1.0, "B"),
        (5, -1.0, "A")])
    
    # Export the DataFrame
    file_path = tmp_path / "exported"
    original.persist_to_disk(file_path)

    # Import the DataFrame
    new_df = DataFrame()
    new_df.load_from_disk(file_path)

    # Original and the new DataFrame must be the same
    assert original.column_names == new_df.column_names
    assert original.column_types == new_df.column_types
    assert original.rows == new_df.rows

def test_persist_load_ensure_types(tmp_path):
    # Create a DataFrame
    original = DataFrame(["A", "B", "C"], [int, float, str], [
        (1, 1.5, "2"),
        (2, 1.5, "3"),
        (3, 2.5, "4"),
        (4, 1.0, "5"),
        (5, -1.0, "6")])
    
    # Export the DataFrame
    file_path = tmp_path / "exported"
    original.persist_to_disk(file_path)

    # Import the DataFrame
    new_df = DataFrame()
    new_df.load_from_disk(file_path)

    # Original and the new DataFrame must be the same
    assert original.column_names == new_df.column_names
    assert original.column_types == new_df.column_types
    assert original.rows == new_df.rows

def test_export_path_not_exist(tmp_path):
    with pytest.raises(FileNotFoundError):
        # Create a DataFrame
        original = DataFrame(["A", "B", "C"], [int, float, str], [
            (1, 1.5, "2"),
            (2, 1.5, "3"),
            (3, 2.5, "4"),
            (4, 1.0, "5"),
            (5, -1.0, "6")])
        
        # Export the DataFrame
        file_path = tmp_path / "my_directory" / "exported"
        original.persist_to_disk(file_path)

        # Import the DataFrame
        new_df = DataFrame()
        new_df.load_from_disk(file_path)

def test_import_path_not_exist(tmp_path):
    with pytest.raises(FileNotFoundError):
        # Create a DataFrame
        original = DataFrame(["A", "B", "C"], [int, float, str], [
            (1, 1.5, "2"),
            (2, 1.5, "3"),
            (3, 2.5, "4"),
            (4, 1.0, "5"),
            (5, -1.0, "6")])
        
        # Export the DataFrame
        file_path = tmp_path / "exported"
        original.persist_to_disk(file_path)

        # Import the DataFrame
        new_df = DataFrame()
        non_file_path = tmp_path / "my_directory" / "exported"
        new_df.load_from_disk(non_file_path)
