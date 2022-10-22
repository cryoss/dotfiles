;;; Compiled snippets and support files for `python-mode'
;;; Snippet definitions:
;;;
(yas-define-snippets 'python-mode
                     '(("idn" "def __init__(self, $1, $2, $3, $4, $5):\n    \\\"\\\"\\\"$2\n    ${1:$(python-args-to-docstring-numpy)}\n    \\\"\\\"\\\"\n    $0\n\n    self.${1:$()} = ${1:$}\n    self.${2:$()} = ${2:$}\n    self.${3:$()} = ${3:$}\n    self.${4:$()} = ${4:$}\n    self.${5:$()} = ${5:$}\n    self.${6:$()} = ${6:$}" "init_docstring_numpy" nil
                        ("definitions")
                        nil "/home/cryoss/.doom.d/snippets/python-mode/init_docstring_real" nil nil)))


;;; Do not edit! File generated at Sat Oct 22 09:05:56 2022
