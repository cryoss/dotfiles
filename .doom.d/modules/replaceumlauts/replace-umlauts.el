;;; replaceumlauts/replace-umlauts.el -*- lexical-binding: t; -*-


;;; replace-umlauts.el
;;;
;;; Replace transcription for german umlauts (ae, oe, etc.); keep
;;; database of known words. (See below for a more comprehensive
;;; description)
;;;
;;; Copyright (C) 1995, 2016 Juergen Nickelsen <ni@w21.org>
;;;
;;; Hierhin kommt spaeter der uebliche Hinweis, dass dieses Programm
;;; im Rahmen der GPL weitergegeben werden darf. Das ist bei dieser
;;; Version noch nicht der Fall!

;;; Description:
;;;
;;; The command M-x replace-umlauts looks in the current text buffer
;;; for words containing ae, oe, ue, Ae, Oe, Ue, or ss. (These are
;;; common transcriptions for the german umlauts ä, ö, ü, Ä, Ö, Ü, and
;;; the "sharp s" ß.) In a separate buffer the you are presented a
;;; list of these words and their suggested replacements. The
;;; replacements can be marked for deletion with "d", meaning the word
;;; is not to be replaced, or edited with "e" (in the minibuffer).
;;; Look up occurences of the current word in your text with "s" (for
;;; "show"). When you continue with C-c C-c, the replacements not
;;; marked as deleted are applied to the text buffer. All replacements
;;; are stored persistently in a file and are "known" the next time.
;;; The words not to be replaced are stored in this file as well.
;;;
;;; replace-umlauts saves time compared to query-replace because each
;;; word must be looked at only once *ever*.
;;;
;;; If you notice that you made a mistake in editing a replacement or
;;; not deleting the replacement, delete the line containing this word
;;; from the database, which is by default kept in
;;; $HOME/.umlaut-replacements (see the user option
;;; `umlaut-replacements-file' below). Be sure to delete the
;;; *complete* line, since replace-umlauts will get confused if the
;;; file format is corrupted.
;;;
;;; By default replace-umlauts does not turn on a minor mode for
;;; typing german umlauts. You can set the variable
;;; `umlaut-umlaut-edit-minor-mode' to a function symbol for a minor
;;; mode to type these characters. This function is called with the
;;; single argument `1' to enable typing german umlauts in the
;;; minibuffer while editing replacements. If you set
;;; `umlaut-umlaut-edit-minor-mode' to t, `iso-accents-mode' will be
;;; used, which enables typing umlauts using e.g. the `"a' sequence for
;;; an ä. See the Emacs manual for details about iso-accents-mode
;;; (Chapter "European Display"). iso-accents-mode is not available
;;; with XEmacs.
;;;
;;; By default replace-umlauts uses german umlauts in ISO 8859-1
;;; encoding. If you use an other character set, change the value of
;;; the variable `umlaut-replacements-alist' appropriately.
;;;
;;; The names of all functions (except some functions that get inlined
;;; when compiled) and global variables defined in replace-umlauts.el
;;; contain the string "umlaut", so you can match them easily with
;;; `apropos'.

;;; Release Notes:
;;;
;;; $Revision: 1.1 $
;;; First beta release. This version is known to work with GNU Emacs
;;; 19.28 and XEmacs 19.13. I appreciate all hints how to make it run
;;; faster.

;;; User options

(defvar umlaut-umlaut-edit-minor-mode nil
  "*If non-nil, a minor mode for writing ISO characters.
Precisely, nil or t or a function symbol that will be called with the
single argument 1 when writing german umlauts or similar characters
might be necessary. If nil, don't set a minor mode; if t, use
iso-accents-mode.")

(defvar umlaut-replacements-file "~/.umlaut-replacements"
  "*File to save known replacements for umlaut words to.
The file contains pairs. The car is the word to replace, the cdr the
replacement. Probably you don't need to change this variable.")

;;; Internal variables. Do not change unless you know what you are
;;; doing.

(defconst umlaut-replacements-alist
  '(("ae" . "ä")
    ("oe" . "ö")
    ("ue" . "ü")
    ("Ae" . "Ä")
    ("Oe" . "Ö")
    ("Ue" . "Ü")
    ("ss" . "ß")
    ("EUR" . "¤")))

(defconst umlaut-search-regexp ""
  "Regular expression to search umlauts.
Actually this is built from umlaut-replacements-alist.")

(defconst umlaut-save-file-comment
  ";;; This file has been created by replace-umlauts. It contains pairs
;;; of words and replacements.
" "Comment to appear on top of umlaut-replacements-file.")

(defconst replace-umlauts-copyright
  "replace-umlauts.el is Copyright (C) 1995, 2016
Juergen Nickelsen <ni@w21.org>")

;; must be defined here to be inlined
(defsubst umlaut-message-and-eval (string form)
  "Output STRING in the echo area and eval FORM."
  (message string)
  (sit-for 0)
  (eval form))

;;; This is the function to be called by the user:

(defun replace-umlauts (&optional buffer)
  "Replace all umlaut transcriptions in BUFFER
as defined in `umlaut-replacements-alist'.
For all unknown words ask the user. Save known words persistently.
Output messages regularly to entertain the user while running."
  (interactive)
  (umlaut-modify-umlaut-syntax)
  (save-excursion
    (save-window-excursion
      (setq buffer (or buffer (current-buffer)))
      (setq umlaut-search-regexp
            (umlaut-build-search-regexp umlaut-replacements-alist))
      (let (wordlist knownlist replacelist dolist)
        (umlaut-message-and-eval
         "Grab words from buffer..."
         '(setq wordlist (umlaut-grab-all-words buffer)))
        (umlaut-message-and-eval
         "Read known replacements..."
         '(setq knownlist (umlaut-read-known-replacements
                           umlaut-replacements-file)))
        (umlaut-message-and-eval
         "Merge known replacements..."
         '(setq replacelist (umlaut-merge-known-replacements knownlist
                                                             wordlist)))
        (umlaut-message-and-eval
         "Edit replacements..."
         '(setq dolist (umlaut-edit-unknown-replacements replacelist)))
        (if dolist
            (progn
              (umlaut-message-and-eval "Replace words..."
                                       '(umlaut-replace-words dolist buffer))
              (umlaut-message-and-eval "Save replacements..."
                                       '(umlaut-save-known-replacements
                                         dolist))
              (umlaut-message-and-eval "Delete markers..."
                                       '(umlaut-delete-markers dolist))
              (message "Done"))
          (ding)
          (message "Aborted"))))))

(defconst umlaut-save-file-comment
  ";;; This file has been created by replace-umlauts. It contains pairs
;;; of words and replacements.
" "Comment to appear on top of umlaut-replacements-file.")

(defun umlaut-modify-umlaut-syntax ()
  "Use ISO umlaut characters with word constituent syntax.
This is necessary for `umlaut-grab-word-at-point' to work correctly."
  (let ((alist umlaut-replacements-alist))
    (while alist
      ;; we assume that the replacements are single characters
      (modify-syntax-entry (string-to-char (cdar alist)) "w")
      (setq alist (cdr alist)))))

;;; In this code a data structure called `wlist' is used a lot. A
;;; wlist is a list of `entries' of the form
;;;
;;;   (word replacement . positionlist)
;;;
;;; where word is a string (usually a word from the text), replacement
;;; a string to replace word, and positionlist is a proper list of
;;; pairs of markers which point to the occurences of word in the text
;;; (beginning and end of the word).
;;;
;;; A wlist is usually sorted alphabetically. Each word occurs only
;;; once in a wlist.
;;;
;;; The positionlist may be empty, i.e. nil. If a replacement is not a
;;; string, but nil, we do not know how to replace the word and must
;;; query the user. This is done by umlaut-edit-unknown-replacements.

;;; For better readability of the code, define some inline functions
;;; to access components of wlists and wlist entries. (Not all of
;;; these are actually used.)

(defsubst wlist-first-entry (wlist)
  "Return the first entry of WLIST."
  (car wlist))

(defsubst wlist-other-entries (wlist)
  "Return the rest of WLIST's entries."
  (cdr wlist))

(defsubst wlist-first-word (wlist)
  "Return the first word in WLIST, as a string."
  (car (car wlist)))

(defsubst wlist-first-repl (wlist)
  "Return the replacement of the first word in WLIST.
This may be a string or nil."
  (car (cdr (car wlist))))

(defsubst wlist-first-poslist (wlist)
  "Return the position list of the first word in WLIST."
  (cdr (cdr (car wlist))))

(defsubst wlist-first-position (wlist)
  "Return the first position of the first word in WLIST."
  (car (cdr (cdr (car wlist)))))

(defsubst wlist-entry-word (entry)
  "Return the word of a wlist ENTRY."
  (car entry))

(defsubst wlist-entry-repl (entry)
  "Return the replacement of a wlist ENTRY."
  (car (cdr entry)))

(defsubst wlist-entry-positions (entry)
  "Return the position list of a wlist ENTRY."
  (cdr (cdr entry)))

(defsubst wlist-entry-first-pos (entry)
  "Return the first position of a wlist ENTRY."
  (car (cdr (cdr entry))))

(defsubst wlist-entry-other-pos (entry)
  "Return the rest of the positions of a wlist ENTRY."
  (cdr (cdr (cdr entry))))

(defsubst wlist-entry-first-beg (entry)
  "Return the first beginning position of a wlist ENTRY."
  (car (car (cdr (cdr entry)))))

(defsubst wlist-entry-first-end (entry)
  "Return the first end position of a wlist ENTRY."
  (cdr (car (cdr (cdr entry)))))

(defsubst wlist-pos-first-beg (positionlist)
  "Return the first beginning of a POSITIONLIST."
  (car (car positionlist)))

(defsubst wlist-pos-first-end (positionlist)
  "Return the first end of a POSITIONLIST."
  (cdr (car positionlist)))

(defsubst wlist-build-entry (word replacement positionlist)
  "Return a wlist entry built from WORD, REPLACEMENT, and POSITIONLIST."
  (cons word (cons replacement positionlist)))

(defun umlaut-build-search-regexp (alist)
  "Return a regular expression to search for the cars of ALIST.
ALIST may be empty, but must be a list of pairs of which at least
the car is a string."
  (let ((re ""))
    (while (cdr alist)
      (setq re (concat re (caar alist) "\\|"))
      (setq alist (cdr alist)))
    (if alist (setq re (concat re (caar alist))))
    re))

(defun umlaut-grab-all-words (&optional buffer)
  "Return a wlist of all words in potentially containing umlaut transcriptions.
Words are searched in BUFFER (optional, defaults to current buffer)."
  (save-excursion
    (set-buffer (or buffer (current-buffer)))
    (goto-char (point-min))
    (let ((case-fold-search nil)
          (wlist ())
          (bound (point-max)))
      (while (re-search-forward umlaut-search-regexp bound t)
        (setq wlist (cons (umlaut-grab-word-at-point) wlist)))
      (umlaut-sort-wlist wlist))))

(defun umlaut-grab-word-at-point ()
  "Return the word at point as a wlist entry.
Move point to the end of the word."
  (let (word begin end)
    (forward-word -1)
    (setq begin (point-marker))
    (forward-word 1)
    (setq end (point-marker))
    (setq word (buffer-substring begin end))
    (wlist-build-entry word nil (list (cons begin end)))))

(defun umlaut-sort-wlist (wlist)
  "Sort WLIST alphabetically.
The begin and end marker lists of each word must be sorted. Entries of
equal words are combined, their marker lists are merged."
  ;; First sort with `sort', then merge entries.
  (let ((presorted (sort wlist
                         '(lambda (e1 e2)
                            (not (string-lessp (wlist-entry-word e1)
                                               (wlist-entry-word e2))))))
        (sorted nil))
    ;; `presorted' is in reverse order; `sorted' is then consed
    ;; together alphabetically.
    (while (wlist-other-entries presorted)
      (let* ((rest (wlist-other-entries presorted))
             (e1 (wlist-first-entry presorted))
             (e2 (wlist-first-entry rest)))
        (if (string-equal (wlist-entry-word e1)
                          (wlist-entry-word e2))
            ;; Combine entries of equal words.
            (let ((new
                   (wlist-build-entry (wlist-entry-word e1)
                                      nil
                                      (nconc (wlist-entry-positions e1)
                                             (wlist-entry-positions e2)))))
              (setq presorted (cons new (wlist-other-entries rest))))
          ;; First two entries are different words; keep second
          (setq sorted (cons e1 sorted))
          (setq presorted rest))))
    (if presorted (cons (wlist-first-entry presorted) sorted))))


(defun umlaut-read-known-replacements (file)
  "Return a list of known umlaut replacements, read from FILE.
For a description of the file format, see the documentation of the
variable `umlaut-replacements-file'."
  (let ((buffer (find-file-noselect (expand-file-name file)))
        (previous-word "")
        (sorted-p t)
        knownlist)
    (save-excursion
      (set-buffer buffer)
      (bury-buffer buffer)
      (goto-char (point-min))
      (condition-case ignore-me
          (while t
            (let* ((pair (read buffer))
                   (word (car pair)))
              ;; The file may be unsorted.
              (if (not (string-lessp previous-word word))
                  (setq sorted-p nil))
              (setq knownlist (cons pair knownlist))))
        (end-of-file nil))
      (if (not sorted-p)
          (sort knownlist '(lambda (e1 e2)
                             (string-lessp (car e1) (car e2))))
        (nreverse knownlist)))))

(defun umlaut-merge-known-replacements (knownlist wordlist)
  "Merge KNOWNLIST (a list of pairs) and WORDLIST (a wlist).
Both lists must be sorted alphabetically.
Return a wlist with the replacements taken from KNOWNLIST.
If the word is not in KNOWNLIST, its entry is unchanged.
If a word from KNOWNLIST is not in WORDLIST, create an entry with
empty position list."
  (let ((newlist ()))
    (while knownlist
      (if wordlist
          (let ((word  (wlist-first-word wordlist))
                (known (caar knownlist)))
            (if (string-lessp known word)
                ;; Word only in knownlist
                (progn
                  (setq newlist (cons (wlist-build-entry (caar knownlist)
                                                         (cdar knownlist)
                                                         nil)
                                      newlist))
                  (setq knownlist (cdr knownlist)))
              (if (string-equal known word)
                  ;; Word in both lists
                  (progn
                    (setq newlist (cons (wlist-build-entry
                                         (caar knownlist)
                                         (cdar knownlist)
                                         (wlist-first-poslist wordlist))
                                        newlist))
                    (setq knownlist (cdr knownlist))
                    (setq wordlist (wlist-other-entries wordlist)))
                ;; Word only in wordlist
                (setq newlist (cons (wlist-first-entry wordlist) newlist))
                (setq wordlist (wlist-other-entries wordlist)))))
        ;; wlist is empty, but knownlist not
        (setq newlist (cons (wlist-build-entry (caar knownlist)
                                               (cdar knownlist)
                                               nil)
                            newlist))
        (setq knownlist (cdr knownlist))))
    (while wordlist
      ;; knownlist is empty
      (setq newlist (cons (wlist-first-entry wordlist) newlist))
      (setq wordlist (wlist-other-entries wordlist)))
    ;; newlist has been consed together in reverse order
    (nreverse newlist)))

(defun umlaut-replace-words (wlist buffer)
  "Replace words from WLIST in BUFFER.
If the replacement is the same as the word, don't replace (for obvious
reasons)."
  (save-excursion
    (set-buffer buffer)
    (while wlist
      (let* ((repl (wlist-first-repl wlist))
             (positions (wlist-first-poslist wlist)))
        (if (not (string-equal repl (wlist-first-word wlist)))
            (while positions
              (let ((beg (wlist-pos-first-beg positions))
                    (end (wlist-pos-first-end positions))
                    (inhibit-quit t))
                (goto-char beg)
                (delete-region beg end)
                (insert repl))
              (setq positions (cdr positions)))))
      (setq wlist (wlist-other-entries wlist)))))

(defun umlaut-save-known-replacements (wlist)
  "Save known words from WLIST in umlaut-replacements-file."
  (let ((buffer (find-file-noselect (expand-file-name
                                     umlaut-replacements-file))))
    (save-excursion
      (set-buffer buffer)
      (erase-buffer)
      (insert umlaut-save-file-comment)
      (insert ";;; saved at " (current-time-string) "\n\n")
      (while wlist
        (let ((inhibit-quit t)
              (repl (wlist-first-repl wlist)))
          (insert "(\"" (wlist-first-word wlist) "\"")
          (if repl
              (insert " . \"" repl "\""))
          (insert ")\n"))
        (setq wlist (wlist-other-entries wlist)))
      (save-buffer)
      (bury-buffer buffer))))

(defun umlaut-delete-markers (wlist)
  "Delete markers in WLIST, i.e. let them point to nil.
This is done to avoid slowing down editing due to lots of markers in
the text after calling replace-umlauts."
  (while wlist
    (let ((positions (wlist-first-poslist wlist)))
      (while positions
        (set-marker (wlist-pos-first-beg positions) nil)
        (set-marker (wlist-pos-first-end positions) nil)
        (setq positions (cdr positions))))
    (setq wlist (wlist-other-entries wlist))))

(defun umlaut-replace-in-word (word)
  "Return WORD with umlaut transcriptions replaced
according to `umlaut-replacements-alist'."
  (let ((case-fold-search nil)
        (alist umlaut-replacements-alist)
        end beg)
    (while alist
      (while (string-match (caar alist) word)
          (progn
            (setq word (concat (substring word 0 (match-beginning 0))
                               (cdar alist)
                               (substring word (match-end 0))))))
      (setq alist (cdr alist)))
    word))

(defun umlaut-minibuffer-setup-hook ()
  "Modify umlaut syntax;
if `umlaut-umlaut-edit-minor-mode' is non-nil, turn on a minor mode
for typing umlauts. To be used in minibuffer-setup-hook."
  (umlaut-modify-umlaut-syntax)
  (if umlaut-umlaut-edit-minor-mode
      (if (eq umlaut-umlaut-edit-minor-mode t)
          (iso-accents-mode 1)
        (funcall umlaut-umlaut-edit-minor-mode 1))))


(defun umlaut-edit-unknown-replacements (replacelist)
  "Edit REPLACELIST to get replacements for unknown words.
REPLACELIST is a wlist where replacement is nil if unknown and must be
supplied by the user. Uses `umlaut-replacements-mode'."
  (let ((repbuffer (get-buffer-create "*Umlaut-replace*"))
        (buffer-read-only nil))
    (bury-buffer repbuffer)
    (condition-case errvar
        (save-excursion
          (switch-to-buffer repbuffer)
          (erase-buffer)
          (umlaut-insert-unknown-replacements replacelist)
          (umlaut-replacements-mode replacelist)
          (goto-char (point-min))
          (let ((minibuffer-setup-hook
                 (if (boundp 'minibuffer-setup-hook)
                     (if (listp minibuffer-setup-hook)
                         (cons 'umlaut-minibuffer-setup-hook
                               minibuffer-setup-hook)
                       ;; must be a symbol then
                       (list 'umlaut-minibuffer-setup-hook
                             minibuffer-setup-hook))
                   '(umlaut-minibuffer-setup-hook))))
            (recursive-edit))
          (let ((new-replacements (umlaut-grab-new-replacements)))
            (kill-buffer repbuffer)
            (umlaut-merge-known-replacements new-replacements replacelist)))
      (quit                             ; recursive edit was aborted
       (message "Delete markers...")
       (sit-for 0)
       (kill-buffer repbuffer)
       (umlaut-delete-markers replacelist)
       ;; return nil to signal abort
       nil))))

(defconst umlaut-space-for-one-word 20
  "Length reserved for one word in replacement buffer.
A word may actually be longer; this value just controls column
alignment.")

(defun umlaut-insert-unknown-replacements (insertlist)
  "Insert unknown words and suggested replacements from INSERTLIST
in current buffer."
  (let ((formatstring (format "  %%-%ds "
                                  umlaut-space-for-one-word)))
    (while insertlist
      (if (not (wlist-first-repl insertlist))
          ;; replacement is unknown
          (let* ((word (wlist-first-word insertlist))
                 (repl (umlaut-replace-in-word word))
                 (inhibit-quit t))
            (insert (format formatstring word))
            (umlaut-insert-replacement repl)
            (insert "\n")))
      (setq insertlist (wlist-other-entries insertlist)))))

(defun umlaut-insert-replacement (repl)
  "Insert replacement at current line in replacements buffer."
  (beginning-of-line)
  (forward-char 2)
  (re-search-forward " +")
  (insert repl)
  (let ((beg (point)))
    (end-of-line)
    (delete-region beg (point))))

(defun umlaut-grab-new-replacements ()
  "Grab alist of replacements from the current buffer."
  (let ((newlist ())
        newlist-before-edited)
    (goto-char (point-min))
    (while (not (eobp))
      (setq newlist (cons (umlaut-grab-replacement-from-line)
                          newlist))
      (forward-line 1))
    (setq newlist-before-edited newlist)
    ;; insert all edited replacements as self-replacing pairs
    (goto-char (point-min))
    (while (re-search-forward "^E " (point-max) t)
      (setq newlist
            (let ((edited (cdr (umlaut-grab-replacement-from-line))))
              (cons (cons edited edited) newlist)))
      (forward-line 1))
    ;; If edited replacements have been included, we need to sort the list.
    (if (not (eq newlist newlist-before-edited))
        (sort newlist '(lambda (p1 p2)
                         (string-lessp (car p1) (car p2))))
      (nreverse newlist))))

(defun umlaut-mark-line (mark-character)
  "Mark line with MARK-CHARACTER (a one-character string),
probably \"D\", \"E\", or \" \".
We assume that a line is marked with a capital letter in column 1."
  (beginning-of-line)
  (if (looking-at "[A-Z ] ")
      (save-excursion
        (let ((buffer-read-only nil))
          (delete-char 1)
          (insert (string-to-char mark-character))))
    (error "No word on this line")))

(defun umlaut-grab-replacement-from-line ()
  "Grab a word/replacement pair from the current line.
Lines marked with D \(deleted\) denote words that are not to be
replaced. In this case the word is returned as a self-replacing pair."
  (beginning-of-line)
  (if (looking-at "[DE ] ")
      (let ((userepl (not (looking-at "D ")))
            beg1 end1 beg2)
        (save-excursion
          (forward-char 2)
          (setq beg1 (point))
          (setq end1 (1- (search-forward " ")))
          (let ((word (buffer-substring beg1 end1)))
            (cons word
                  (if userepl
                      (progn
                        (setq beg2 (1- (re-search-forward "[^ ]")))
                        (end-of-line)
                        (buffer-substring beg2 (point)))
                    word)))))
    (error "No word on this line")))

;;; Major mode for editing replacements follows.

(defvar umlaut-replacements-mode-map nil
  "Local map for umlaut-replacements-mode.")

(defvar umlaut-local-wordlist nil
  "Buffer-local variable for the current wordlist.
It is used to look up the occurences of words for umlaut-show-occurences.")

(defvar umlaut-last-show nil
  "Word last shown with umlaut-show-occurences.
If non-nil, this buffer-local variable is a pair
(<wlist-entry> . <position-list>), where <wlist-entry> is the entry of
the word last shown; <position-list> is a part of the list of its
positions. If non-nil, the car of this list is the next position to
show with `umlaut-show-occurences'.")

;; mode is not for regular editing
(put 'umlaut-replacements-mode 'mode-class 'special)

(defun umlaut-replacements-mode (wordlist)
  "\
Major mode for editing umlaut replacements in a buffer.

p - previous word     n - next word       s - show word's occurences in text
< - beginning         > - end
d - mark as deleted   u - remove mark     e - edit replacement
C-c C-c - exit and accept changes         a - abort edit
? - short help        h - long help

Runs `umlaut-replacements-mode-hook' after setup.

Key bindings:
\\{umlaut-replacements-mode-map}"
  (kill-all-local-variables)
  (setq mode-line-buffer-identification '("Replacements: %17b"))
  (setq major-mode 'umlaut-replacements-mode)
  (use-local-map umlaut-replacements-mode-map)
  (setq mode-name "Umlaut Edit")
  (setq buffer-read-only t)
  (make-local-variable 'umlaut-last-show)
  (setq umlaut-last-show nil)           ; pair: wlist entry and poslist
  (make-local-variable 'umlaut-local-wordlist)
  (setq umlaut-local-wordlist wordlist)
  (message
   (substitute-command-keys
    (concat "Type \\[umlaut-continue-with-replacing] to continue,"
            " \\[umlaut-edit-help] for help")))
  (run-hooks 'umlaut-replacements-mode-hook))

(if (not umlaut-replacements-mode-map)
    (progn
      (setq umlaut-replacements-mode-map (make-sparse-keymap))
      (define-key umlaut-replacements-mode-map "d" 'umlaut-mark-delete)
      (define-key umlaut-replacements-mode-map "u" 'umlaut-undelete)
      (define-key umlaut-replacements-mode-map "e" 'umlaut-edit-repl)
      (define-key umlaut-replacements-mode-map "n" 'umlaut-next-word)
      (define-key umlaut-replacements-mode-map "p" 'umlaut-previous-word)
      (define-key umlaut-replacements-mode-map " " 'umlaut-next-word)
      (define-key umlaut-replacements-mode-map "\177" 'umlaut-previous-word)
      (define-key umlaut-replacements-mode-map "<" 'beginning-of-buffer)
      (define-key umlaut-replacements-mode-map ">" 'end-of-buffer)
      (define-key umlaut-replacements-mode-map "h" 'describe-mode)
      (define-key umlaut-replacements-mode-map "\C-c\C-c"
        'umlaut-continue-with-replacing)
      (define-key umlaut-replacements-mode-map "a" 'umlaut-abort)
      (define-key umlaut-replacements-mode-map "q" 'umlaut-abort)
      (define-key umlaut-replacements-mode-map "?" 'umlaut-edit-help)
      (define-key umlaut-replacements-mode-map "s" 'umlaut-show-occurences)
      ))

(defun umlaut-show-occurences ()
  "Successively show occurences of current word in other window."
  (interactive)
  (save-excursion
    (let* ((window (selected-window))
           (word (car (umlaut-grab-replacement-from-line)))
           entry position)
      (if (or (not umlaut-last-show)
              (not (string-equal (wlist-entry-word (car umlaut-last-show))
                                 word)))
          ;; Last word shown was not this one.
          (let ((entry (umlaut-lookup-word word umlaut-local-wordlist)))
            (setq umlaut-last-show (cons entry
                                         (wlist-entry-positions entry)))))
      ;; Any positions left?
      (if (not (cdr umlaut-last-show))
          (or (setcdr umlaut-last-show
                      (wlist-entry-positions (car umlaut-last-show)))
              (error "Word not in text")))
      (setq position (wlist-pos-first-beg (cdr umlaut-last-show)))
      ;; Remove position from list.
      (setcdr umlaut-last-show (cdr (cdr umlaut-last-show)))
      (if (not (cdr umlaut-last-show))
          (message "Last occurence"))
      (pop-to-buffer (marker-buffer position))
      (goto-char position)
      (recenter 1)
      (select-window window))))

(defun umlaut-lookup-word (word wlist)
  "Return WORD's entry in WLIST."
  (while (and wlist
              (not (string-equal word (wlist-first-word wlist))))
    (setq wlist (cdr wlist)))
  (and wlist
       (wlist-first-entry wlist)))

(defun umlaut-mark-delete ()
  "Mark current word as deleted (no replace)."
  (interactive)
  (umlaut-mark-line "D")
  (forward-line 1))

(defun umlaut-undelete ()
  "Remove delete mark from current word."
  (interactive)
  (let ((buffer-read-only nil))
    (beginning-of-line)
    (if (looking-at "[ED ] ")
        (if (looking-at "D ")
            (progn
              (umlaut-mark-line " ")
              (forward-line 1))
          (message "Current word is not marked as deleted"))
      (message "No word on this line"))))

(defun umlaut-edit-repl ()
  "Edit replacement for current word."
  (interactive)
  (let* ((pair (umlaut-grab-replacement-from-line))
         (newrepl (read-string (format "New replacement for %s: "
                                       (car pair))
                               (cdr pair)))
         (buffer-read-only nil))
    (umlaut-insert-replacement newrepl)
    (umlaut-mark-line "E")
    (forward-line 1)))

(defun umlaut-next-word (arg)
  "Move down ARG words."
  (interactive "p")
  (forward-line arg))

(defun umlaut-previous-word (arg)
  "Move up ARG words."
  (interactive "p")
  (forward-line (- arg)))

(defun umlaut-continue-with-replacing (arg)
  "Exit replacements mode and replace words.
With C-u as prefix arg, don't ask for confirmation."
  (interactive "P")
  (if (or (equal arg '(4))
          (y-or-n-p "Replace all words? "))
      (exit-recursive-edit)))

(defun umlaut-abort ()
  "Abort replacements mode, discard changes, do not replace words."
  (interactive)
  (if (yes-or-no-p "Discard changes and abort without replacing? ")
      (abort-recursive-edit)))

(defun umlaut-edit-help ()
  "Give a short help message."
  (interactive)
  (message
   "d)el u)nmark e)dit s)how  C-c C-c: continue  a)bort   ?:help h:long help"))

(defun reverse-replace-umlauts (umlaut-alist)
  (save-excursion
    (let ((case-replace nil)
          (case-fold-search nil)
          (count 0))
      (while umlaut-alist
        (let ((from (caar umlaut-alist))
              (to (cdar umlaut-alist)))
          (goto-char (point-min))
          (while (search-forward from nil t)
            (incf count)
            (replace-match to nil t))
        (setq umlaut-alist (cdr umlaut-alist))))
      (message "replaced %d umlauts" count))))

(defun htmlify-umlauts ()
  (interactive)
  (reverse-replace-umlauts '(("ä" . "&auml;")
                             ("ö" . "&ouml;")
                             ("ü" . "&uuml;")
                             ("Ä" . "&Auml;")
                             ("Ö" . "&Ouml;")
                             ("Ü" . "&Uuml;")
                             ("ß" . "&szlig;")
                             ("¤" . "&euro;"))))

(defun transcribe-umlauts ()
  (interactive)
  (reverse-replace-umlauts '(("ä" . "ae")
                             ("ö" . "oe")
                             ("ü" . "ue")
                             ("Ä" . "Ae")
                             ("Ö" . "Oe")
                             ("Ü" . "Ue")
                             ("ß" . "ss")
                             ("¤" . "EUR"))))



;;; EOF
