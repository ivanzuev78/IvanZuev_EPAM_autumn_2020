from HomeWork_4.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_stdout(capsys):
    my_precious_logger("May the Force be with you")
    captured = capsys.readouterr()
    assert captured.out == "May the Force be with you"
    assert captured.err == ""


def test_my_precious_logger_stderr(capsys):
    my_precious_logger("error: Force not found")
    captured = capsys.readouterr()
    assert captured.err == "error: Force not found"
    assert captured.out == ""


def test_my_precious_logger_empty_input(capsys):
    my_precious_logger("")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
