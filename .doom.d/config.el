;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Place your private configuration here! Remember, you do not need to run 'doom
;; sync' after modifying this file!

;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets.
(setq user-full-name "cryoss"
      user-mail-address "n.billing@billtec.de")

(prefer-coding-system 'utf-8)
;; Doom exposes five (optional) variables for controlling fonts in Doom. Here
;; are the three important ones:
        ;;
;; + `doom-font'
;; + `doom-variable-pitch-font'
;; + `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;;
;; They all accept either a font-spec, font string ("Input Mono-12"), or xlfd
;; font string. You generally only need these two:
;; (setq doom-font (font-spec :family "monospace" :size 12 :weight 'semi-light)
;;       doom-variable-pitch-font (font-spec :family "sans" :size 13))

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)
;;(setq-default cursor-type 'hbar)
(setq evil-normal-state-cursor '(box "dark cyan" )
      evil-insert-state-cursor '(bar "medium sea green")
      evil-visual-state-cursor '(hollow "orange"))
 (blink-cursor-mode 0)
;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(after! org
(setq org-directory "~/dev/org/")
(setq org-agenda-files '("~/dev/org/agenda.org"))
(setq org-log-done 'note))
(setq browse-url-browser-function 'browse-url-generic
        browse-url-generic-program "qutebrowser")
;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type 'relative)


;; Here are some additional functions/macros that could help you configure Doom:
;;
;; - `load!' for loading external *.el files relative to this one
;; - `use-package!' for configuring packages
;; - `after!' for running code after a package has loaded
;; - `add-load-path!' for adding directories to the `load-path', relative to
;;   this file. Emacs searches the `load-path' when you load packages with
;;   `require' or `use-package'.
;; - `map!' for binding new keys
;;
;; To get information about any of these functions/macros, move the cursor over
;; the highlighted symbol at press 'K' (non-evil users must press 'C-c c k').
;; This will open documentation for it, including demos of how they are used.
;;
;; You can also try 'gd' (or 'C-c c d') to jump to their definition and see how
;; they are implemented.
(map! :leader
      (:prefix ("b". "buffer")
       :desc "List bookmarks" "L" #'list-bookmarks
       :desc "Save current bookmarks to bookmark file" "w" #'bookmark-save))
(xterm-mouse-mode 1)

(setq doom-font (font-spec :family "Source Code Pro" :size 20)
      doom-variable-pitch-font (font-spec :family "Ubuntu" :size 20)
      doom-big-font (font-spec :family "Source Code Pro" :size 25))
(after! doom-themes
  (setq doom-themes-enable-bold t
        doom-themes-enable-italic t))
(custom-set-faces!
  '(font-lock-comment-face :slant italic)
  '(font-lock-keyword-face :slant italic))


(setq undo-limit 80000000
      auto-save-default t)
(setenv "DICTIONARY" "de_DE")
;; Set $DICPATH to "$HOME/Library/Spelling" for hunspell.
(setenv
  "DICPATH"
  "/usr/share/hunspell")
;; Tell ispell-mode to use hunspell.
(setq
  ispell-program-name
  "hunspell")
(require 'ispell)
(setq ispell-personal-dictionary "~/org/.hunspell")
(add-to-list 'ispell-local-dictionary-alist '("deutsch-hunspell"
                                              "[[:alpha:]]"
                                              "[^[:alpha:]]"
                                              "[']"
                                              t
                                              ("-d" "de_DE"); Dictionary file name
                                              nil
                                              iso-8859-1))
(add-to-list 'ispell-local-dictionary-alist '("english-hunspell"
                                              "[[:alpha:]]"
                                              "[^[:alpha:]]"
                                              "[']"
                                              t
                                              ("-d" "en_US")
                                              nil
                                              iso-8859-1))

(setq selection-coding-system 'utf-8)
(require 'bibtex)
(setq bibtex-completion-bibliography '("~/dev/org/Bachelorarbeit/ba.bib" "~/dev/org/IuG/IuG.bib")
	bibtex-completion-library-path '("~/dev/org/bib/documents")
	bibtex-completion-notes-path "~/dev/org/bib/notes/"
	bibtex-completion-notes-template-multiple-files "* ${author-or-editor}, ${title}, ${journal}, (${year}) :${=type=}: \n\nSee [[cite:&${=key=}]]\n"
	bibtex-completion-additional-search-fields '(keywords)
	bibtex-completion-display-formats
	'((article       . "${=has-pdf=:1}${=has-note=:1} ${year:4} ${author:36} ${title:*} ${journal:40}")
	  (inbook        . "${=has-pdf=:1}${=has-note=:1} ${year:4} ${author:36} ${title:*} Chapter ${chapter:32}")
	  (incollection  . "${=has-pdf=:1}${=has-note=:1} ${year:4} ${author:36} ${title:*} ${booktitle:40}")
	  (inproceedings . "${=has-pdf=:1}${=has-note=:1} ${year:4} ${author:36} ${title:*} ${booktitle:40}")
	  (t             . "${=has-pdf=:1}${=has-note=:1} ${year:4} ${author:36} ${title:*}"))
	bibtex-completion-pdf-open-function
	(lambda (fpath)
	  (call-process "open" nil 0 nil fpath)))


(map! :leader
      (:prefix-map ("m" . "insert")
       (:prefix ("l" . "insert")
        :desc "New journal entry" "C" #'org-ref-cite-insert-helm
        )))


(setq bibtex-autokey-year-length 4
	bibtex-autokey-name-year-separator "-"
	bibtex-autokey-year-title-separator "-"
	bibtex-autokey-titleword-separator "-"
	bibtex-autokey-titlewords 2
	bibtex-autokey-titlewords-stretch 1
	bibtex-autokey-titleword-length 5
	org-ref-bibtex-hydra-key-binding (kbd "H-b"))

(define-key bibtex-mode-map (kbd "H-b") 'org-ref-bibtex-hydra/body)

(require 'org-ref-helm)
(setq org-ref-insert-link-function 'org-ref-insert-link-hydra/body
      org-ref-insert-cite-function 'org-ref-cite-insert-helm
      org-ref-insert-label-function 'org-ref-insert-label-link
      org-ref-insert-ref-function 'org-ref-insert-ref-link
      org-ref-cite-onclick-function (lambda (_) (org-ref-citation-hydra/body)))


;; (require 'org-ref-ivy)

;; (setq org-ref-insert-link-function 'org-ref-insert-link-hydra/body
;;       org-ref-insert-cite-function 'org-ref-cite-insert-ivy
;;       org-ref-insert-label-function 'org-ref-insert-label-link
;;       org-ref-insert-ref-function 'org-ref-insert-ref-link
;;       org-ref-cite-onclick-function (lambda (_) (org-ref-citation-hydra/body)))

(setq org-cite-csl-styles-dir "~/dev/org/bib/Zotero/styles")
;; (setq org-latex-pdf-process (list "latexmk -shell-escape -bibtex -f -pdf %f"))

(setq org-latex-pdf-process
      '("latexmk -gg -lualatex %f"
        ))



(require 'auto-virtualenv)
(add-hook 'python-mode-hook 'auto-virtualenv-set-virtualenv)
(setq org-src-fontify-natively t)
;; (setq org-format-latex-options (plist-put org-format-latex-options :scale 5.0))
(setq org-latex-pdf-process
  '("lualatex -shell-escape -interaction nonstopmode %f"
    "lualatex -shell-escape -interaction nonstopmode %f"))



(map! :leader
        (:prefix ("d" . "application")
       :desc "export to pdf"
      "e p" #'org-export-dispatch))
