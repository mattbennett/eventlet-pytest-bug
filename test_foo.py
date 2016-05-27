pytest_plugins = "pytester"


def test_bar(testdir):

    testdir.makepyfile(
        """
        def test_baz():
            import logging
            log = logging.getLogger()
            log.debug("hello")

            assert "foo" == "foo"
        """
    )
    result = testdir.runpytest()
    assert result.ret == 0
