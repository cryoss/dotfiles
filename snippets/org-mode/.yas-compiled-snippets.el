;;; Compiled snippets and support files for `org-mode'
;;; Snippet definitions:
;;;
(yas-define-snippets 'org-mode
                     '(("src_python" "#+BEGIN_SRC python :results {output, pp}  :session $1 :tangle $2.py :comments org\n$3\n\n#+END_SRC" "src_python" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/src_python" nil nil)
                       ("src_ipy" "#+BEGIN_SRC python :results {output, pp}  :session $1 :tangle $2.py :comments org\n$3\n\n#+END_SRC\n" "src_ipython" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/src_ipython" nil nil)
                       ("src_emacslisp" "#+begin_src emacs-lisp :exports both :tangle $1 :comments org\n\n#+end_src" "src_emacslisp" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/src_emacslisp" nil nil)
                       ("m" "\\begin{equation}\n$1\n\\end{equation}" "math" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/math" nil nil)
                       ("inlmath" "\\$\\\\ $1\\$" "inlinemath" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/inlinemath" nil nil)
                       ("CommentYP" "$\\colorbox{yellow}{$1} \\colorbox{pink}{$2}$" "commentYP" nil nil nil "/home/cryoss/.doom.d/snippets/org-mode/commentYP" nil nil)))


;;; Do not edit! File generated at Sat Oct 22 09:05:56 2022
