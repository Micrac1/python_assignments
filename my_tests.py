import inspect

def print_test_results() -> None:
    if test.fail_count == 0:
        print(f"All {test.pass_count} tests passed! Good job!")
    else:
        print(f"All tests finished. {test.pass_count} passed, {test.fail_count} failed.")

def test(value: bool) -> None:
    if (not hasattr(test, 'fail_count')):
        test.fail_count = 0
    if (not hasattr(test, 'pass_count')):
        test.pass_count = 0

    failed = False

    if value:
        test.pass_count += 1
    else:
        test.fail_count += 1
        failed = True
    print(f"[{'Error' if failed else '   Ok'}] ", end='')
    print(' '.join(inspect.stack()[1].code_context).lstrip(), end='')
