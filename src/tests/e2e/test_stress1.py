import sys
import pytest
import os

# Ensure src is in the path
sys.path.insert(0, 'src')

from sunbears.dataframe import DataFrame

def test_stress1(tmp_path):
    """
    Stresses the DataFrame lifecycle:
    1. Initialization
    2. Insert (Valid & Invalid)
    3. Remove
    4. String Representation
    5. Persistence (Save & Load)
    """
    
    # ---------------------------------------------------------
    # 1. INITIALIZATION & INSERT
    # ---------------------------------------------------------
    df = DataFrame(
        column_names=["ID", "Name", "Score"], 
        column_types=[int, str, float], 
        rows=[]
    )
    
    # Insert valid rows
    df.insert((1, "Alice", 95.5))
    df.insert((2, "Bob", 80.0))
    df.insert((3, "Charlie", 60.5))
    
    # Verify internal state
    assert len(df.rows) == 3
    assert df.active == [True, True, True]

    # ---------------------------------------------------------
    # 2. INSERT STRESS (Error Handling)
    # ---------------------------------------------------------
    # Case A: Wrong number of columns (2 instead of 3)
    with pytest.raises(ValueError):
        df.insert((4, "Dave"))
        
    # Case B: Wrong types (str instead of int for ID)
    with pytest.raises(TypeError):
        df.insert(("five", "Eve", 100.0))

    # Case C: Wrong types (int instead of float for Score - strict check)
    # Note: Your implementation checks `type(val) != col_type`, so 100 != float
    with pytest.raises(TypeError):
        df.insert((5, "Frank", 100)) 

    # ---------------------------------------------------------
    # 3. REMOVE & __STR__
    # ---------------------------------------------------------
    # Remove the middle row (Bob)
    df.remove(1)
    
    assert df.active == [True, False, True]
    
    output_str = str(df)
    
    # Ensure "Bob" is NOT in the string output
    assert "Alice" in output_str
    assert "Bob" not in output_str
    assert "Charlie" in output_str
    
    # Ensure formatting borders exist
    assert "+-" in output_str
    assert "| " in output_str

    # ---------------------------------------------------------
    # 4. PERSISTENCE (Save)
    # ---------------------------------------------------------
    file_path = tmp_path / "lifecycle_dump.txt"
    df.persist_to_disk(str(file_path))
    
    assert file_path.exists()
    
    # ---------------------------------------------------------
    # 5. LOAD & VERIFY
    # ---------------------------------------------------------
    loaded_df = DataFrame()
    loaded_df.load_from_disk(str(file_path))
    
    # VERIFICATION
    # NOTE: In your current implementation, persist_to_disk writes ALL rows
    # (ignoring self.active) and load_from_disk inserts them as new (True).
    # So "Bob" will resurrect here.
    
    assert loaded_df.column_names == ["ID", "Name", "Score"]
    assert loaded_df.column_types == [int, str, float]
    
    # Check that we have 3 rows again (Bob is back)
    assert len(loaded_df.rows) == 3
    assert loaded_df.rows[1] == (2, "Bob", 80.0)
    
    # Ensure types were preserved during load
    assert isinstance(loaded_df.rows[0][0], int)
    assert isinstance(loaded_df.rows[0][1], str)
    assert isinstance(loaded_df.rows[0][2], float)

    print("\nLIFECYCLE TEST PASSED: Init -> Insert -> Errors -> Remove -> Str -> Save -> Load")
