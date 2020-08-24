# -*- coding: utf-8 -*-
from __future__ import print_function
import ply.lex as lex

tokens = (
   'ID',
   'STRING',
   'INT',
   'FLOAT',
   'LPAREN',
   'RPAREN'
)

t_ignore  = ' \t'
t_ignore_comment= r'//.*'
t_ignore_comment_2 = r'/\*.*\*/'
t_ID  = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_STRING  = r'\".*?\"'
t_INT = r'\d+'
t_FLOAT = r'-?\d+(\.\d+)*'
t_LPAREN  = r'\{'
t_RPAREN  = r'\}'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)