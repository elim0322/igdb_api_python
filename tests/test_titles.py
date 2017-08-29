import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/titles/single_title.yml', filter_headers=['user-key'])
def test_single_title():
    result = igdb.titles(29)
    assert result != []

@vcr.use_cassette('tests/vcr_cassettes/titles/multiple_title.yml', filter_headers=['user-key'])
def test_multiple_title():
    result = igdb.titles({
        'ids':[29,14,22]
    })
    assert result != []
    assert result[0]['id'] == 29
    assert result[1]['id'] == 14
    assert result[2]['id'] == 22
