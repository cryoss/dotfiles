
;; Define username and email

(setq user-full-name "cryoss"
      user-mail-address "n.billing@billtec.de")

(prefer-coding-system 'utf-8)

(setq undo-limit 80000000
      auto-save-default t)

(setq doom-theme 'doom-one)
;;(setq-default cursor-type 'hbar)
(setq evil-normal-state-cursor '(box "dark cyan" )
      evil-insert-state-cursor '(bar "medium sea green")
      evil-visual-state-cursor '(hollow "orange"))
 (blink-cursor-mode 0)

;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type 'relative)

(setq doom-font (font-spec :family "Comic Mono" :size 30)
      doom-variable-pitch-font (font-spec :family "Ubuntu" :size 20)
      doom-big-font (font-spec :family "Comic Mono" :size 25))
(after! doom-themes
  (setq doom-themes-enable-bold t
        doom-themes-enable-italic t))
(custom-set-faces!
  '(font-lock-comment-face :slant italic)
  '(font-lock-keyword-face :slant italic))

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(after! org
(setq org-directory "~/dev/org/")
(setq org-agenda-files '("~/dev/org/ideas.org"))
(setq org-log-done 'note))
(setq browse-url-browser-function 'browse-url-generic
        browse-url-generic-program "qutebrowser")

(setq org-latex-pdf-process
      '("latexmk -gg -lualatex %f"
        ))


(setq org-src-fontify-natively t)
;; (setq org-format-latex-options (plist-put org-format-latex-options :scale 5.0))
(setq org-latex-pdf-process
  '("lualatex -shell-escape -interaction nonstopmode %f"
    "lualatex -shell-escape -interaction nonstopmode %f"))



(map! :leader
        (:prefix ("d" . "application")
       :desc "export to pdf"
      "e p" #'org-export-dispatch))
(when (daemonp)
  (exec-path-from-shell-initialize))(when (daemonp)
  (exec-path-from-shell-initialize))

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
                                              iso-88))

(use-package dired
  :ensure nil
  :commands (dired dired-jump)
  :bind (("C-x C-j" . dired-jump))
  :custom ((dired-listing-switches "-agho --group-directories-first"))
  :config
  (evil-collection-define-key 'normal 'dired-mode-map
    "h" 'dired-single-up-directory
    "l" 'dired-single-buffer))

(use-package dired-open
  :config
  ;; (add-to-list 'dired-open-functions #'dired-open-xdg t)

  (setq dired-open-extensions ' (("png" . "feh")
                                 ("pdf" . "org.kde.okular"))
        ))

(use-package python-mode
:hook (python-mode . lsp-deferred))
(use-package lsp-jedi
  :ensure t
  :config
  (with-eval-after-load "lsp-mode"
    (add-to-list 'lsp-disabled-clients 'pyls)
    (add-to-list 'lsp-enabled-clients 'jedi)))

;; (setq lsp-jedi-workspace-extra-paths
;;   (vconcat lsp-jedi-workspace-extra-paths
;;            ["/home/cryoss/dev/e-still/lib/python3.10/site-packages"]))
