;;; Compiled snippets and support files for `org-mode'
;;; Snippet definitions:
;;;
(yas-define-snippets 'org-mode
                     '(("python_session" "#+BEGIN_SRC python :results raw :session $1\n$2\n#+END_SRC" "python_session" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/python_session" nil nil)
                       ("pysession" "#+BEGIN_SRC python :results raw :session $0\n$1\n#+END_SRC" "python seassio" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/python seassio" nil nil)
                       ("m" "\\begin{equation}\n$1\n\\end{equation}" "math" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/math" nil nil)
                       ("inlmath" "\\$\\\\ $1\\$" "inlinemath" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/inlinemath" nil nil)))


;;; Do not edit! File generated at Fri Jan  7 18:50:57 2022
