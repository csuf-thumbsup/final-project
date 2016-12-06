parsing_table_1 = {
        'A': {
            'program': 'program B ; var C begin D end.',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'B': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'E F',
            'b': 'E F',
            'c': 'E F',
            '$': 'undef'
            },
        'F': {
            'program': 'undef',
            ';': 'Y',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'Y',
            ',': 'Y',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'Y',
            '=': 'Y',
            '+': 'Y',
            '-': 'Y',
            '*': 'Y',
            '/': 'Y',
            '0': 'Y',
            '1': 'Y',
            '2': 'Y',
            '3': 'Y',
            '4': 'Y',
            '5': 'Y',
            '6': 'Y',
            '7': 'Y',
            '8': 'Y',
            '9': 'Y',
            'a': 'Y',
            'b': 'Y',
            'c': 'Y',
            '$': 'undef'
            },
        'Y': {
            'program': 'undef',
            ';': 'lambda',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'lambda',
            ',': 'lambda',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'lambda',
            '=': 'lambda',
            '+': 'lambda',
            '-': 'lambda',
            '*': 'lambda',
            '/': 'lambda',
            '0': 'H Y',
            '1': 'H Y',
            '2': 'H Y',
            '3': 'H Y',
            '4': 'H Y',
            '5': 'H Y',
            '6': 'H Y',
            '7': 'H Y',
            '8': 'H Y',
            '9': 'H Y',
            'a': 'E Y',
            'b': 'E Y',
            'c': 'E Y',
            '$': 'undef'
            },
        'C': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'I : J ;',
            'b': 'I : J ;',
            'c': 'I : J ;',
            '$': 'undef'
            },
        'I': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'B T',
            'b': 'B T',
            'c': 'B T',
            '$': 'undef'
            },
        'T': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'lambda',
            ',': ', B T',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'J': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'integer',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'D': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'K U',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'K U',
            'b': 'K U',
            'c': 'K U',
            '$': 'undef'
            },
        'U': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'lambda',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'K U',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'K U',
            'b': 'K U',
            'c': 'K U',
            '$': 'undef'
            },
        'K': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'L',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'M',
            'b': 'M',
            'c': 'M',
            '$': 'undef'
            },
        'L': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'print ( B );',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'M': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'B = N ;',
            'b': 'B = N ;',
            'c': 'B = N ;',
            '$': 'undef'
            },
        'N': {
            'program': 'undef',
            ';': 'O V',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'O V',
            ')': 'O V',
            '=': 'undef',
            '+': 'O V',
            '-': 'O V',
            '*': 'O V',
            '/': 'O V',
            '0': 'O V',
            '1': 'O V',
            '2': 'O V',
            '3': 'O V',
            '4': 'O V',
            '5': 'O V',
            '6': 'O V',
            '7': 'O V',
            '8': 'O V',
            '9': 'O V',
            'a': 'O V',
            'b': 'O V',
            'c': 'O V',
            '$': 'undef'
            },
        'V': {
            'program': 'undef',
            ';': 'lambda',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'lambda',
            '=': 'undef',
            '+': '+ O V',
            '-': '- O V',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'O': {
            'program': 'undef',
            ';': 'P W',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'P W',
            ')': 'P W',
            '=': 'P W',
            '+': 'P W',
            '-': 'P W',
            '*': 'P W',
            '/': 'P W',
            '0': 'P W',
            '1': 'P W',
            '2': 'P W',
            '3': 'P W',
            '4': 'P W',
            '5': 'P W',
            '6': 'P W',
            '7': 'P W',
            '8': 'P W',
            '9': 'P W',
            'a': 'P W',
            'b': 'P W',
            'c': 'P W',
            '$': 'undef'
            },
        'W': {
            'program': 'undef',
            ';': 'lambda',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'lambda',
            '=': 'undef',
            '+': 'lambda',
            '-': 'lambda',
            '*': '* P W',
            '/': '/ P W',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'undef',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'P': {
            'program': 'undef',
            ';': 'Q',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': '( N )',
            ')': 'Q',
            '=': 'undef',
            '+': 'Q',
            '-': 'Q',
            '*': 'Q',
            '/': 'Q',
            '0': 'Q',
            '1': 'Q',
            '2': 'Q',
            '3': 'Q',
            '4': 'Q',
            '5': 'Q',
            '6': 'Q',
            '7': 'Q',
            '8': 'Q',
            '9': 'Q',
            'a': 'B',
            'b': 'B',
            'c': 'B',
            '$': 'undef'
            },
        'Q': {
            'program': 'undef',
            ';': 'R H S',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'R H S',
            '=': 'undef',
            '+': 'R H S',
            '-': 'R H S',
            '*': 'R H S',
            '/': 'R H S',
            '0': 'R H S',
            '1': 'R H S',
            '2': 'R H S',
            '3': 'R H S',
            '4': 'R H S',
            '5': 'R H S',
            '6': 'R H S',
            '7': 'R H S',
            '8': 'R H S',
            '9': 'R H S',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'R': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': '+',
            '-': '-',
            '*': 'undef',
            '/': 'undef',
            '0': 'lambda',
            '1': 'lambda',
            '2': 'lambda',
            '3': 'lambda',
            '4': 'lambda',
            '5': 'lambda',
            '6': 'lambda',
            '7': 'lambda',
            '8': 'lambda',
            '9': 'lambda',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'S': {
            'program': 'undef',
            ';': 'X',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'X',
            '=': 'undef',
            '+': 'X',
            '-': 'X',
            '*': 'X',
            '/': 'X',
            '0': 'X',
            '1': 'X',
            '2': 'X',
            '3': 'X',
            '4': 'X',
            '5': 'X',
            '6': 'X',
            '7': 'X',
            '8': 'X',
            '9': 'X',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'X': {
            'program': 'undef',
            ';': 'lambda',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'lambda',
            '=': 'undef',
            '+': 'lambda',
            '-': 'lambda',
            '*': 'lambda',
            '/': 'lambda',
            '0': 'H X',
            '1': 'H X',
            '2': 'H X',
            '3': 'H X',
            '4': 'H X',
            '5': 'H X',
            '6': 'H X',
            '7': 'H X',
            '8': 'H X',
            '9': 'H X',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'H': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': '0',
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            'a': 'undef',
            'b': 'undef',
            'c': 'undef',
            '$': 'undef'
            },
        'E': {
            'program': 'undef',
            ';': 'undef',
            'var': 'undef',
            'begin': 'undef',
            'end.': 'undef',
            ':': 'undef',
            ',': 'undef',
            'integer': 'undef',
            'print': 'undef',
            '(': 'undef',
            ')': 'undef',
            '=': 'undef',
            '+': 'undef',
            '-': 'undef',
            '*': 'undef',
            '/': 'undef',
            '0': 'undef',
            '1': 'undef',
            '2': 'undef',
            '3': 'undef',
            '4': 'undef',
            '5': 'undef',
            '6': 'undef',
            '7': 'undef',
            '8': 'undef',
            '9': 'a',
            'a': 'b',
            'b': 'c',
            'c': 'undef',
            '$': 'undef'
            }
        }