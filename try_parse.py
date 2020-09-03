# parse function
def try_parse_int(input_value):
    def ignore_exception(IgnoreException=Exception, DefaultVal=None):

        def dec(function):
            def _dec(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except IgnoreException:
                    return DefaultVal
            return _dec
        return dec

    string_int = ignore_exception(ValueError)(int)

    return string_int(input_value)


def try_parse_float(input_value):
    def ignore_exception(IgnoreException=Exception, DefaultVal=None):

        def dec(function):
            def _dec(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except IgnoreException:
                    return DefaultVal
            return _dec
        return dec

    string_float = ignore_exception(ValueError)(float)

    return string_float(input_value)
