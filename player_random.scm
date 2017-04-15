#!/usr/bin/csi -s

(require-extension srfi-13)

(define bid-quantity 0)
(define bid-value 0)

(define (play move)
  (display move)
  (newline)
  (flush-output))

(define (loop)
  (let ((line (read-line)))
    (if (eof-object? line)
      0
      (let* ((parts (string-split line))
             (instruction (string->symbol (car parts))))
        (case instruction
          ((NEW_ROUND)
           (set! bid-quantity 0)
           (set! bid-value 6))
          ((PLAYER_BIDS)
           (set! bid-quantity (string->number (caddr parts)))
           (set! bid-value (string->number (cadddr parts))))
          ((PLAY)
           (if (and (> bid-quantity 0) (< (random 10) 4))
             (play "CHALLENGE")
             (play (string-append "BID " (number->string (+ 1 bid-quantity)) " " (number->string bid-value))))))
        (loop)))))

(loop)
