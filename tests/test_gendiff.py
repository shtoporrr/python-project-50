from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json():
    """Test generate_diff function with JSON files."""
    result = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    )
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert result == expected


def test_generate_diff_yaml():
    """Test generate_diff function with YAML files."""
    result = generate_diff(
        'tests/fixtures/file1.yml',
        'tests/fixtures/file2.yml'
    )
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert result == expected


def test_generate_diff_nested_json():
    """Test generate_diff function with nested JSON files."""
    result = generate_diff(
        'tests/fixtures/nested_file1.json',
        'tests/fixtures/nested_file2.json'
    )
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    assert result == expected


def test_generate_diff_nested_yaml():
    """Test generate_diff with nested YAML files."""
    file1_path = 'tests/fixtures/nested_file1.yml'
    file2_path = 'tests/fixtures/nested_file2.yml'
    
    result = generate_diff(file1_path, file2_path)
    
    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    
    assert result == expected


def test_generate_diff_plain_json():
    """Test generate_diff with plain format for JSON files."""
    file1_path = 'tests/fixtures/nested_file1.json'
    file2_path = 'tests/fixtures/nested_file2.json'
    
    result = generate_diff(file1_path, file2_path, 'plain')
    
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    
    assert result == expected


def test_generate_diff_plain_yaml():
    """Test generate_diff with plain format for YAML files."""
    file1_path = 'tests/fixtures/nested_file1.yml'
    file2_path = 'tests/fixtures/nested_file2.yml'
    
    result = generate_diff(file1_path, file2_path, 'plain')
    
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    
    assert result == expected


def test_generate_diff_json_format():
    """Test generate_diff with json format."""
    import json
    
    file1_path = 'tests/fixtures/nested_file1.json'
    file2_path = 'tests/fixtures/nested_file2.json'
    
    result = generate_diff(file1_path, file2_path, 'json')
    
    # Verify that result is valid JSON
    parsed_result = json.loads(result)
    assert isinstance(parsed_result, list)
    
    # Verify structure contains expected diff nodes
    assert len(parsed_result) > 0
    for node in parsed_result:
        assert 'key' in node
        assert 'type' in node
        assert node['type'] in [
            'added', 'removed', 'unchanged', 'changed', 'nested'
        ]