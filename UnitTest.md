# Unit Test

**Se ejecuta el test:**

(venv) PS C:\Users\juans\Documents\apps\blog> python manage.py test
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...FF
======================================================================
FAIL: test_no_questions2 (portfolio.tests.ViewTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\juans\Documents\apps\blog\portfolio\tests.py", line 28, in test_no_questions2
    self.assertEqual(response.status_code, 200)
AssertionError: 302 != 200

======================================================================
FAIL: test_past_question (portfolio.tests.ViewTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\juans\Documents\apps\blog\portfolio\tests.py", line 34, in test_past_question
    self.assertEqual(response.status_code, 200)
AssertionError: 302 != 200

----------------------------------------------------------------------
Ran 5 tests in 0.800s

FAILED (failures=2)
Destroying test database for alias 'default'...

**Se analizan los resultados:**

Los resultados arrojan tres casos correctos y dos intentos fallidos.

1. El primer test es correcto porque lo que se crea en la clase Project es lo que se recibe de la misma.
2. El segundo test es correcto porque se accede a la página solicitada.
3. El tercer test falla porque se le pide ir a la página principal del blog pero al no estar loggeado redirige a la de log in.
4. El cuarto test también falla por no poder acceder a la página principal del blog sin estar loggeado.
5. El quinto test es correcto ya que al loggearse primero luego puede acceder a la página principal del blog.