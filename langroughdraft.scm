(define-datatype expression expression?
 (note-exp(alph char-alphabetic?))
 (rest-exp(sym symbol?))
 (measure-exp
       (exp1 expression?)
       (exp2 expression?)
       (exp3 expression?))
  (clef-exp
       (exp1 expression?))
 (key-exp
      (exp1 expression?)
      (exp2 expression?))
 (timesig-exp
      (exp1 expression?)
      (exp2 expression?)))

(define the-lexical-spec
    '((whitespace (whitespace) skip)
      (comment ("%" (arbno (not #\newline))) skip)
      (identifier
       (letter (arbno (or letter digit "_" "-" "?")))
       symbol)
      (number (digit (arbno digit)) number)
      (number ("-" digit (arbno digit)) number)
      ))

(define the-grammar
    '((program (expression) a-program)
      (expression (char) note-exp)
      (expression (symbol) rest-exp)
      (expression
        (expression "," expression "," expression)
        measure-exp)
      (expression
        ("(" expression ")" )
        clef-exp)
      (expression
       ("(" expression expression ")")
       key-exp)
      (expression
       ("(" expression "/" expression ")")
       timesig-exp)
      ))


(define scan&parse
     (sllgen:make-string-parser the-lexical-spec the-grammar))
