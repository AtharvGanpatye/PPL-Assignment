; N th element of list

(defun nth_element ()

	(print "Enter the size of list : ")
	(setq size (read))
	(print "Enter the list elements :  ")
	(setq i 1)
	(setq l '())
	(loop
		(setq x (read))
		(setq l (cons x l))
		(setq i (+ i 1))
		(when (> i size) (return))
	)
	(print l)
	(print "Enter the value of n : ")
	(setq n (read))
	(setq n (- size n))
	(setq val (nth n l))
	(print val)

)

;Factorial by Recursion
(defun fact_by_recur ()

	(format t "Factorial of a number by recursion. ~%")
	(format t "Enter a number ~%")
	(setq n (read))

	(defun fact (n)
		(if (<= n 1) 
			1
		(* n (fact (- n 1)))))


	(format t "Factorial by Recursion is : ~d"(fact n))

)

;Factorial by Iteration

(defun fact_by_iter ()

	(print "Factorial of a number by iteration.")
	(print "Enter a number :")
	(defvar n (read))
	(setq i 1)
	(setq result 1)
	(loop
		(setq result (* result i))
		(setq i (+ i 1))
		(when (> i n) (return))
	)
	(format t "Factorial by Iteration is : ~d" result)

)

;(nth_element )

;(fact_by_recur )

(fact_by_iter )



