""":mod:`cpg_islands.header` --- Helper module to print a nice-looking header
"""

def header(header_text, char='-'):
    """Print text from a header and a line of header characters below it.

    :param header_text: the text to print
    :type header_text: :class:`str`
    :param char: the header character
    :type char: :class:`str`
    :return: the formatted header
    :rtype: :class:`str`
    """
    return header_text + '\n' + len(header_text) * char
