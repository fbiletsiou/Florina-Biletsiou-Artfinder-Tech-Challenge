from src.run import main, display_results


def test_display_results_with_float_score(capsys):
    # Display results with float score
    display_results([('file1.txt', 75.0), ('file2.txt', 50.5)])

    # Capturing printed output
    captured = capsys.readouterr().out

    # Verifying output
    assert "file1.txt : 75%" in captured
    assert "file2.txt : 50.5%" in captured


def test_display_results_with_integer_score(capsys):
    # Display results with integer score
    display_results([('file1.txt', 100), ('file2.txt', 0)])

    # Capturing printed output
    captured = capsys.readouterr().out

    # Verifying output
    assert "file1.txt : 100%" in captured
    assert "file2.txt : 0%" in captured
