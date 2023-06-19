def test_package():
    """
    Check to see if the package even loads at all. I.e. Can we import it and get data from __init__?
    """
    import furrycrossroadspy
    assert furrycrossroadspy.__version__
    assert furrycrossroadspy.__author__



